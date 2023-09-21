import speech_recognition as sr    
import pyttsx3

# Configuramos los parametros de velocidad y el idioma de reconocimiento a Español para la funcion speak()
engine = pyttsx3.init()
engine.setProperty("rate", 240)
engine.setProperty("voice", "spanish")


def speak(text):
    # Transforma el texto que escribamos a audio
    engine.say(text)
    engine.runAndWait()


def hear_me():
    # Obtiene audio del microfono y lo transforma en texto
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estoy escuchando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-Es')
            return text
        except sr.UnknownValueError:
            print('No te he entendido')
