"""
1. **Encriptacion de texto** : Crea un modulo con los caracteres de encriptacion y desencriptacion y haz una aplicacion para cifrar un texto. 
Tambien puedes usar el cifrado Cesar
"""

from dictionary import character_dictionary as dictionary


def text_user():
    # Creamos un bucle WHILE infinito, para que en el caso de que el usuario quiera volver a hacer otra accion, le vuelva a preguntar, si presiona la Q cerrara el bucle
    # Preguntamos al user que opcion desea, y dependiendo de lo que responda, preguntaremos que quiere escribir y luego llamamos a la funcion correspondiente
    # Si el usuario introduce caracteres o numeros a la hora de escoger la opcion correspondiente, se le avisará de que escoja alguna de las opciones
    while True:
        
        choose_user = input("Que deseas hacer?: \n"
                             "[E]ncriptar \n"
                             "[D]esencriptar \n"
                             "[Q] para salir \n").lower()
        if choose_user == "e":
            ask_user = input("Que texto deseas encriptar?: \n")
            encrypt(ask_user)
        elif choose_user == "d":
            ask_user = input("Que texto deseas desencriptar?: \n")
            desencrypt(ask_user)
        elif choose_user == "q":
            print("Nos vemos! \n")
            break
        else:
            print("Elige alguna de las opciones! \n")
      
            
def encrypt(ask_user):
    """
    1.- Pasamos el parametro del texto del usuario y creamos una variable vacia (text)
    2.- Recorremos con un FOR el texto del usuario, y a cada iteracion se comprobara si cada letra de la palabra esta en la Clave - Valor del diccionario
    3.- Si es True, se añadira una letra aleatoria del Valor del diccionario que creamos en otro modulo a la variable vacia
    4.- Si no es True se añadira la misma letra escrita por el user, a la variable vacia
    5.- Se notificara al usuario con el mensaje de su frase encriptada
    """
    text = ""
    
    for a in ask_user:
        if a in dictionary:
            text += dictionary[a]
        else:
            text += a

    print(f"Tu frase encriptada es: {text} \n")


def desencrypt(ask_user):
    """
    1.- Pasamos el parametro del texto del usuario y creamos una variable vacia (text)
    2.- Recorremos con un FOR el texto del usuario, y a cada iteracion se comprobara si cada letra del texto esta en el Valor del diccionario
    3.- Si es True, se creara otro bucle FOR que iterará por la Clave y Valor al mismo tiempo del diccionario,
            Y se comprobara si el Valor del diccionario es igual a la letra recorrida del texto del user, si es True, se añadira la Valor del diccionario a la varible vacia (text)
    4.- Si no es True se añadira la misma letra escrita por el user, a la variable vacia (text)
    5.- Se notificara al usuario con el mensaje de su frase desencriptada
    """
    text = ""
    
    for a in ask_user:
        if a in dictionary.values():
            for clave, valor in dictionary.items():
                if valor == a:
                    text += clave
                    break
        
        else:
            text += a
    
    print(f"Tu frase desencriptada es: {text} \n")


def main():
    print("----> Dime una frase y te la encriptare o desencriptare <----")
    text_user()


if __name__ == "__main__":
    main()