"""
10. **Adivina la palabra**: (Ahorcado )Escribe un programa en Python que seleccione una palabra al azar de una lista de palabras predefinidas
y permita al usuario adivinar la palabra. La lista de palabras puede ser una lista que definas en tu programa.
Muestra una representación de la palabra en la que las letras se reemplacen por guiones bajos _. 
Por ejemplo, si la palabra es "python", la representación sería "_ _ _ _ _ _".

"""
import os
import random


def normas(palabra):
    # Decimos las normas y en funcion de los caracteres de la palabra a adivinar le damos al usuario unos intentos o otros.
    print("\n==>NORMAS<==\n")
    print("Solo tienes que introducir un caracter")
    print("Tu numero de intentos se vera modificado en funciona de la longitud de la palabra")
    print(f"Tu palabra tiene {len(palabra)} caracteres")
    if len(palabra) <= 5:
        intentos = 6
        print(f"y tienes {intentos} intentos")
    else:
        intentos = 12
        print(f"y tienes {intentos} intentos")
        
    input("Cuando estes listo presiona ENTER")
    os.system("cls")
    return intentos


def ahorcado():
    """
    1-Establecemos una lista de palabras y elegimos una aleatoriamente
    2-Creamos una lista vacia que sean _ en funcion del len de la palabra
    3-Mostrarmos las normas con los intentos
    4-Creamos una lista vacia para almancenar las palabras acertadas que ha dicho el usuario
    5-Iniciamos un bucle While y preguntamos al usuario el texto. 
        Tambien manejamos los errores y el numero de intentos, asi como si acierta la palabra
    
    """
    
    lista_palabras = ["python", "programacion", "cafe", "junior", "videojuegos", "teletrabajo", "ajedrez"]
    palabra = random.choice(lista_palabras)
    
    lista_vacia = ["_"] * len(palabra)
    
    intentos = normas(palabra)
    letras_adivinadas = []
    
    while intentos >= 0:
        
        print(" ".join(lista_vacia))
        print(f"\nLa palabra tiene {len(palabra)} caracteres")
        letra_user = input("Que letra eliges? : ").lower()
        
        if not letra_user.isalpha() or len(letra_user) != 1:
            print("Por favor, ingresa una unica letra válida.")
            continue
        
        if letra_user in letras_adivinadas:
            print(f"Ya adivinaste la letra '{letra_user}'.")
            
        elif letra_user in palabra:
            print(f"Has acertado la letra {letra_user}")
            letras_adivinadas.append(letra_user)
            for i in range(len(palabra)):
                if palabra[i] == letra_user:
                    lista_vacia[i] = letra_user
                        
        elif letra_user not in palabra:
            print(f"La letra {letra_user} no esta en la palabra")
            intentos -= 1
            print(f"Te quedan {intentos} intentos")
            
        if intentos == 0:
            print("GAME OVER. La palabra correcta era:", palabra)
            break
        
        if "_" not in lista_vacia:
            print("¡Has ganado! La palabra es:", palabra)
            break
           

def main():
    # Funcion Principal
    os.system("cls")
    print("¿¿Jugamos al Ahorcado??")
    ahorcado()


if __name__ == "__main__":
    main()