"""
3. **Reconocimiento de Voz**: Crea un programa que utilice una biblioteca de reconocimiento de voz, como SpeechRecognition, para convertir el habla del usuario en texto.
    Luego, realiza alguna acción en función de los comandos de voz del usuario, como abrir una página web o realizar una búsqueda en línea. 
    Sientete libre de usar expresiones regulares.
"""
from speech_recog import speak, hear_me
import re
import webbrowser


def identify_name(text):
    """
    1.- Creamos una lista de posibles respuesta del usuario, para recoger con Regex, el nombre que nos diga el usuario
    2.- Recorremos cada elemento de la lista, añadimos la que coincida mencionada por el usuario en una variable (name)
    3.- Manejamos los errores en el caso de que no se encuentre el elemento en la lista y retornamos la edad
    """
    name = None
    patterns = ["me llamo ([A-za-z]+)", "mi nombre es ([A-za-z]+)", "^([A-za-z]+)$"]
    
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def identify_age(text):
    """
    1.- Creamos una lista de posibles respuesta del usuario, para recoger con Regex, la edad que nos diga el usuario
    2.- Recorremos cada elemento de la lista, añadimos la que coincida mencionada por el usuario en una variable (age)
    3.- Manejamos los errores en el caso de que no se encuentre el elemento en la lista y retornamos el nombre
    """
    age = None
    patterns = ["tengo ([0-9]+)", "mi edad es ([0-9]+)", "^([0-9]+)$", "^([0-9]+) años"]
    
    for pattern in patterns:
        try:
            age = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return age


def user_name():
    """
    1.- Con la funcion speak, preguntamos al usuario por su nombre y la guardamos en una variable (name_user)
    2.- Luego pasamos la variable del nombre del usuario como parametro a la funcion identify_name
    3.- Saludaremos al usuario con su nombre
    4.- Retornamos la variable name_user
    """
    speak("Cual es tu nombre?")
    
    name_user = hear_me()
    name_user = identify_name(name_user)
    
    print(f"Hola {name_user}")
    speak(f"Hola {name_user}, encantada")

    return name_user


def age_user():
    """
    1.- Con la funcion speak, preguntamos al usuario por su nombre y la guardamos en una variable (age_user)
    2.- Luego pasamos la variable del nombre del usuario como parametro a la funcion identify_age
    3.- Le diremos al user la quedad que nos ha dicho
    4.- Creamos una condicion dependiendo de si la edad que nos ha dicho el usuario es menor o mayor a 40, nos dira una respuesta diferente
    5.- Retornamos la variable age_user
    """
    speak("Que edad tienes?")
    
    age_user = hear_me()
    age_user = identify_age(age_user)
    
    print(f"Tienes {age_user} años")
    speak(f"Tienes {age_user} años")
    
    if age_user:
        age_user = int(age_user)
        if age_user < 40:
            speak("Que joven eres!")
        elif age_user > 40:
            speak("Que rapido pasa el tiempo")

    return age_user


def open_browser(name_user):
    """
    1.- Preguntamos al usuario que pagina quiere abrir
    2.- Guardamos el sitio mencionado en una variable (url_site)
    3.- Con el modulo webbrowser indicaremos que pagina web abrir con el sitio mencionado por el usuario
    """
    speak(f"Vale {name_user}, voy abrirte una pagina web, cual deseas abrir?")
    
    url_site = hear_me()
    
    print(f"Okey, abriendo {url_site}")
    speak(f"Abriendo {url_site}")
    webbrowser.open(f"www.{url_site}.com")
    
    
def main():
    print("----> Bienvenido al Reconocimiento de Voz <----")
    speak("Bienvenido al Reconocimiento de Voz")
    
    name_user = user_name()
    age_user()
    open_browser(name_user)
    
    
if __name__ == "__main__":
    main()