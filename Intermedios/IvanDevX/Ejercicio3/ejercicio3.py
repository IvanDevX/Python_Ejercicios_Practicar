"""
3. **Reconocimiento de Voz**: Crea un programa que utilice una biblioteca de reconocimiento de voz, 
como SpeechRecognition, para convertir el habla del usuario en texto. 
Luego, realiza alguna acción en función de los comandos de voz del usuario, 
como abrir una página web o realizar una búsqueda en línea. Sientete libre de usar expresiones regulares.
"""
# Importamos el modulo que hemos creado donde estan las funciones de escuchar y hablar.
from speak_hearme import speak, hear_me
import re #Expresiones regulares
import webbrowser #Para abrir el navegador por defecto, con la url
import requests 

def identify_name(text):
    """
    Con expresiones regulares recorremos posibles respuestas que pueda dar el usuario y solo guardamos lo importante
    Luego retornamos name
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
    Con expresiones regulares recorremos posibles respuestas que pueda dar el usuario y solo guardamos lo importante
    Luego retornamos age
    """
    age = None
    patterns = ["tengo ([0-9]+)", "mi edad es ([0-9]+)", "^([0-9]+)$"]
    for pattern in patterns:
        try:
            age = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return age
    

def name_user():
    #Preguntamos al usuario su nombre y lo pasamos por regex para solo almacenar su nombre
    intro_name = "Me puedes decir tu nombre?"
    print(intro_name) ,speak(intro_name)
    name = hear_me()
    name = identify_name(name)
    return name
    
    
def age_user():
    #Preguntamos al usuario su edad y lo pasamos por regex para solo almacenar su edad. Luego depende la edad decimos una frase
    intro_age = "Me puedes decir tu edad?"
    print(intro_age) ,speak(intro_age)
    age = hear_me()
    age = identify_age(age)
    range_edad = ""
    ageint = int(age)
    if ageint < 25:
        range_edad = "Que joven"
    elif ageint > 25 and ageint < 40:
        range_edad = "Todo un adulto ya!"
    else:
        range_edad = "Como pasan los años eh"
    return age, range_edad


def action_user():
    # En este caso abrimos una web. Si el usuario dice milanuncios. El programa abrira la web, previa verificaion de status 200
    intro_action = "Voy a abrir una pagina web, que pagina quieres que abra?"
    print(intro_action) ,speak(intro_action)
    url = hear_me()
    url_completa = f"https://www.{url}.com"
    
    if is_valid_url(url_completa):
        print(f"Abriendo {url}") ,speak(f"Abriendo {url}")
        webbrowser.open(url_completa)
    else: 
        print("No puedo abrir esa web, no existe") ,speak("No puedo abrir esa web, no existe")

    
def is_valid_url(a):
    # Verifica la web del usuario a ver si existe
    try:
        response = requests.get(a)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def main():
    """
    1. Damos la bienvenida al usuario tanto por texto como por voz
    2. Almacenamos los datos, como la edad y el nombre
    3. Mostramos y decimos un mensaje con los datos del usuario
    4. Lanzamos la action de abrir una pagina web que el usuario diga.
    
    """
    bienvenida = "Hola, Vamos a convertir tu voz a texto."
    print(bienvenida) ,speak(bienvenida)
    name = name_user()
    age, range_edad = age_user()
    frase = f"Hola {name} me dices que tienes {age}. {range_edad}"
    print(frase) ,speak(frase)
    action_user()


if __name__ == "__main__":
    main()