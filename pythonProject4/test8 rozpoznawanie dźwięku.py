import speech_recognition as sr
import pyaudio

# Inicjalizacja recognizera
recognizer = sr.Recognizer()

# Użycie mikrofonu jako źródła dźwięku
with sr.Microphone() as source:
    print("Powiedz coś...")
    # Przestój, aby mikrofon się ustabilizował
    recognizer.adjust_for_ambient_noise(source)
    # Nagrywanie dźwięku
    audio = recognizer.listen(source)

try:
    # Rozpoznawanie mowy z wykorzystaniem Google Web Speech API
    text = recognizer.recognize_google(audio, language="en-GB")
    print("Rozpoznano: " + text)
except sr.UnknownValueError:
    print("Nie można było rozpoznać mowy")
except sr.RequestError as e:
    print(f"Błąd połączenia z usługą rozpoznawania mowy: {e}")