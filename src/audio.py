import speech_recognition as sr
import time


def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.listen(source)
        try:
            print("Transcribiendo audio, espere unos segundos...")
            text = recognizer.recognize_google(audio_data, language="es-ES")
            time.sleep(1.5)
            return text
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"Error al solicitar el reconocimiento de voz; {e}"
