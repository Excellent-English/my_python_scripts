from gtts import gTTS
import io
import pygame
import time


def read_word(word):
    tts = gTTS(text=word, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    # Czeka, aż dźwięk się odtworzy
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)


# Główna pętla programu
while True:
    word = input("Wpisz słowo (lub wpisz 'exit', aby zakończyć): ")
    if word.lower() == 'exit':
        break
    read_word(word)