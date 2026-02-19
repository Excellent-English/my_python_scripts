# -*- coding: utf-8 -*-
"""
Puzzle 3×3 (lub dowolne N×N) w pygame – gotowy skrypt do wklejenia.

Funkcje:
- Drag & drop kafelków (przeciągnij i upuść).
- Snap-to-grid (wyrównanie do siatki po puszczeniu).
- Sprawdzanie wygranej.
- Timer i licznik ruchów.
- Tasowanie (klawisz R).
- Wyjście (ESC lub zamknięcie okna).
- Opcjonalne cięcie źródłowego obrazu na N×N kafelków (Pillow), jeśli ustawisz SOURCE_IMAGE.

Instrukcje:
1) Jeśli masz pocięte pliki crop_r_c.jpg (np. z naszej sesji):
   - Umieść je obok tego pliku.
   - Ustaw USE_SOURCE_IMAGE = False.
   - Uruchom: python puzzle.py

2) Jeśli chcesz ciąć 1 obraz w locie:
   - Zainstaluj: pip install pillow pygame
   - Ustaw USE_SOURCE_IMAGE = True i podaj nazwę w SOURCE_IMAGE (np. "telefon.jpg").
   - Ustaw GRID_ROWS i GRID_COLS (np. 3 i 3).
   - Uruchom: python puzzle.py
"""

import os
import sys
import random
from pathlib import Path
import pygame

# ==== KONFIGURACJA ====
GRID_ROWS = 3
GRID_COLS = 3
MARGIN = 0            # odstęp między kafelkami (px)

# Opcjonalne cięcie z jednego pliku (w locie). Jeśli False – wczyta crop_r_c.jpg.
USE_SOURCE_IMAGE = False
SOURCE_IMAGE = "source.jpg"     # używane tylko gdy USE_SOURCE_IMAGE = True
SAVE_CROPS_TO_DISK = False      # zapisz wycięte kafelki do plików crop_r_c.jpg (debug/preview)

# Kolory i UI
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
INFO_PANEL = True               # pokaż pasek informacji (czas, ruchy, instrukcje)
INFO_PADDING = 10
FONT_SIZE = 24

# Losowanie na starcie
SHUFFLE_ON_START = True


# ========= ŚCIEŻKI =========
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR  # możesz zmienić na BASE_DIR / "assets"


# ========= OPCJONALNE CIĘCIE Z OBRAZU =========
def slice_image_to_surfaces_pygame(image_path, rows, cols):
    """
    Tnie obraz (pygame) na rows×cols surfaces.
    Zwraca listę pygame.Surface w kolejności (r, c).
    """
    img = pygame.image.load(str(image_path))
    w, h = img.get_width(), img.get_height()
    tile_w, tile_h = w // cols, h // rows

    tiles = []
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * tile_w, r * tile_h, tile_w, tile_h)
            tile_surface = pygame.Surface((tile_w, tile_h), flags=pygame.SRCALPHA)
            tile_surface.blit(img, (0, 0), rect)
            tiles.append(tile_surface)
    return tiles, tile_w, tile_h


def slice_image_to_files_pillow(image_path, rows, cols):
    """
    Alternatywa: używa Pillow do pocięcia i zapisuje crop_r_c.jpg do ASSETS_DIR.
    Wywoływana tylko, jeśli Pillow jest dostępne i SAVE_CROPS_TO_DISK = True.
    """
    try:
        from PIL import Image
    except Exception:
        print("Pillow nie jest zainstalowany – pomijam zapisywanie cropów do plików.")
        return

    im = Image.open(image_path).convert("RGB")
    w, h = im.size
    tile_w, tile_h = w // cols, h // rows

    for r in range(rows):
        for c in range(cols):
            left = c * tile_w
            upper = r * tile_h
            right = left + tile_w
            lower = upper + tile_h
            crop = im.crop((left, upper, right, lower))
            out = ASSETS_DIR / f"crop_{r}_{c}.jpg"
            crop.save(out, quality=95)


# ========= LOGIKA PUZZLI =========
def layout_positions(tile_w, tile_h, rows, cols, margin):
    positions = []
    for r in range(rows):
        for c in range(cols):
            x = c * (tile_w + margin)
            y = r * (tile_h + margin)
            positions.append((x, y))
    return positions


def snap_to_cell(x, y, tile_w, tile_h, rows, cols, margin):
    c = round(x / (tile_w + margin))
    r = round(y / (tile_h + margin))
    c = max(0, min(cols - 1, c))
    r = max(0, min(rows - 1, r))
    return r, c


def cell_to_xy(r, c, tile_w, tile_h, margin):
    x = c * (tile_w + margin)
    y = r * (tile_h + margin)
    return x, y


def is_solved(tiles, tile_w, tile_h, rows, cols, margin):
    for t in tiles:
        x, y = t["rect"].topleft
        r, c = snap_to_cell(x, y, tile_w, tile_h, rows, cols, margin)
        if (r, c) != t["home"]:
            return False
    return True


def load_tiles_from_crops(rows, cols):
    """Wczytuje crop_r_c.jpg BEZ convert(), zwraca listę 'surowych' surfaces i wymiary kafelka."""
    sample_path = ASSETS_DIR / "crop_0_0.jpg"
    if not sample_path.exists():
        raise FileNotFoundError(f"Nie znaleziono {sample_path}. Upewnij się, że pliki crop_r_c.jpg leżą obok skryptu "
                                f"lub włącz USE_SOURCE_IMAGE, aby ciąć w locie.")

    sample = pygame.image.load(str(sample_path))  # bez convert()
    tile_w, tile_h = sample.get_width(), sample.get_height()

    surfaces = []
    for r in range(rows):
        for c in range(cols):
            fn = ASSETS_DIR / f"crop_{r}_{c}.jpg"
            if not fn.exists():
                raise FileNotFoundError(f"Brakuje pliku: {fn}")
            surf = pygame.image.load(str(fn))  # bez convert()
            surfaces.append(surf)
    return surfaces, tile_w, tile_h


def build_tiles(surfaces, rows, cols, tile_w, tile_h):
    """Z powierzchni (już w formacie ekranu) buduje strukturę kafelków."""
    tiles = []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            surf = surfaces[idx]
            tiles.append({
                "image": surf,
                "home": (r, c),
                "rect": pygame.Rect(0, 0, tile_w, tile_h),
                "drag": False,
                "offset": (0, 0),
            })
    return tiles


def shuffle_tiles(tiles, positions):
    """Tasuje pozycje kafelków (proste przetasowanie)."""
    random_positions = positions[:]
    random.shuffle(random_positions)
    for t, (x, y) in zip(tiles, random_positions):
        t["rect"].topleft = (x, y)


# ========= GŁÓWNA APLIKACJA =========
def main():
    pygame.init()
    pygame.display.set_caption("Puzzle")

    # 1) Wczytaj/konstruktuj surfaces BEZ convert(), poznaj wymiary
    if USE_SOURCE_IMAGE:
        src = ASSETS_DIR / SOURCE_IMAGE
        if not src.exists():
            print(f"Nie znaleziono pliku źródłowego: {src}")
            sys.exit(1)
        raw_surfaces, tile_w, tile_h = slice_image_to_surfaces_pygame(src, GRID_ROWS, GRID_COLS)

        # opcjonalnie zapisz do plików (debug/preview)
        if SAVE_CROPS_TO_DISK:
            slice_image_to_files_pillow(src, GRID_ROWS, GRID_COLS)
    else:
        raw_surfaces, tile_w, tile_h = load_tiles_from_crops(GRID_ROWS, GRID_COLS)

    # 2) Ustal layout i docelowy rozmiar okna
    positions = layout_positions(tile_w, tile_h, GRID_ROWS, GRID_COLS, MARGIN)
    grid_width = positions[-1][0] + tile_w
    grid_height = positions[-1][1] + tile_h

    info_height = 0
    if INFO_PANEL:
        # Rezerwujemy miejsce na panel informacji u góry
        info_height = FONT_SIZE + 2 * INFO_PADDING

    WIDTH = grid_width
    HEIGHT = grid_height + info_height

    # 3) Ustaw okno (ważne: przed convert())
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE)

    # 4) Dopiero teraz convert() – surfaces w formacie ekranu
    surfaces = [s.convert_alpha() if s.get_alpha() else s.convert() for s in raw_surfaces]

    # 5) Zbuduj structures kafelków i rozmieść
    tiles = build_tiles(surfaces, GRID_ROWS, GRID_COLS, tile_w, tile_h)

    # Przesuń siatkę o wysokość paska info (jeśli aktywny)
    # (logika kafelków będzie rysowana od (0, info_height))
    def apply_info_offset(rects, dy):
        for t in tiles:
            t["rect"].move_ip(0, dy)

    apply_info_offset(tiles, info_height)

    # Pozycje „w świecie gry” (z offsetem info panelu)
    positions_with_offset = [(x, y + info_height) for (x, y) in positions]

    if SHUFFLE_ON_START:
        shuffle_tiles(tiles, positions_with_offset)
    else:
        # Ustaw domyślnie w kolejności
        for t, (x, y) in zip(tiles, positions_with_offset):
            t["rect"].topleft = (x, y)

    dragging_tile = None
    solved = False
    move_count = 0
    start_ticks = pygame.time.get_ticks()  # start timera (ms)

    def draw_info_bar():
        # tło panelu
        pygame.draw.rect(screen, (20, 20, 20), (0, 0, WIDTH, info_height))
        # tekst
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        elapsed_sec = elapsed_ms // 1000
        mins = elapsed_sec // 60
        secs = elapsed_sec % 60
        status = "Ułóż puzzle (przeciągnij i upuść). R – tasuj, ESC – wyjście."
        if solved:
            status = "Ułożone! 🎉  R – zagraj ponownie, ESC – wyjście."
        text = f"Czas: {mins:02}:{secs:02}   Ruchy: {move_count}   {status}"
        surf = font.render(text, True, TEXT_COLOR)
        screen.blit(surf, (INFO_PADDING, INFO_PADDING))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    # reset/tasowanie
                    shuffle_tiles(tiles, positions_with_offset)
                    solved = False
                    move_count = 0
                    start_ticks = pygame.time.get_ticks()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not solved:
                    mx, my = event.pos
                    # sprawdź od końca (ostatni narysowany – na wierzchu)
                    for t in reversed(tiles):
                        if t["rect"].collidepoint(mx, my):
                            dragging_tile = t
                            t["drag"] = True
                            ox = mx - t["rect"].x
                            oy = my - t["rect"].y
                            t["offset"] = (ox, oy)
                            # przenieś na wierzch (zachowaj kolejność rysowania)
                            tiles.remove(t)
                            tiles.append(t)
                            break

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if dragging_tile:
                    t = dragging_tile
                    # snap to grid (uwzględnij offset panelu info!)
                    r, c = snap_to_cell(
                        t["rect"].x,
                        t["rect"].y - info_height,  # odejmij offset
                        tile_w, tile_h,
                        GRID_ROWS, GRID_COLS,
                        MARGIN
                    )
                    x, y = cell_to_xy(r, c, tile_w, tile_h, MARGIN)
                    t["rect"].topleft = (x, y + info_height)
                    t["drag"] = False
                    dragging_tile = None
                    move_count += 1
                    solved = is_solved(tiles, tile_w, tile_h, GRID_ROWS, GRID_COLS, MARGIN)

            elif event.type == pygame.MOUSEMOTION:
                if dragging_tile and dragging_tile["drag"]:
                    mx, my = event.pos
                    ox, oy = dragging_tile["offset"]
                    dragging_tile["rect"].x = mx - ox
                    dragging_tile["rect"].y = my - oy

        # Rysowanie
        screen.fill(BG_COLOR)

        if INFO_PANEL:
            draw_info_bar()

        # obszar siatki (opcjonalnie można narysować delikatne linie komórek)
        # for r in range(GRID_ROWS + 1):
        #     y = info_height + r * (tile_h + MARGIN)
        #     pygame.draw.line(screen, (60,60,60), (0, y), (WIDTH, y), 1)
        # for c in range(GRID_COLS + 1):
        #     x = c * (tile_w + MARGIN)
        #     pygame.draw.line(screen, (60,60,60), (x, info_height), (x, info_height + grid_height), 1)

        for t in tiles:
            screen.blit(t["image"], t["rect"])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)