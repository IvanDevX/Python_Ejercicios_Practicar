# pip install SpeechRecognition (reconocer voz)
import speech_recognition as sr
# pip install pyttsx3 (para que el programa hable)
import pyttsx3


engine = pyttsx3.init()
engine.setProperty("rate" , 180)
engine.setProperty("voice", "spanish")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    # obtiene audio del microfono y lo transforma en texto
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estoy escuchando")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-Es')
            return text
        except sr.UnknownValueError:
            print('No te he entendido')