import os
import sys

def resource_path(relative_path):
    try:
        # Dla EXE wygenerowanego przez PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Dla uruchamiania z PyCharma
        current_file = os.path.abspath(__file__)
        allclasses_folder = os.path.dirname(current_file)
        base_path = os.path.dirname(allclasses_folder)

    return os.path.join(base_path, relative_path)


# poprzednia wersja, gdyby ta wyżej nie działała prawidłowo

# import os
# import sys
#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except AttributeError:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

