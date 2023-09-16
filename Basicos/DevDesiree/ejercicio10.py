"""
10. **Adivina la palabra**: (Ahorcado) Escribe un programa en Python que seleccione una palabra al azar de una lista de palabras predefinidas y permita al usuario adivinar la palabra. 
La lista de palabras puede ser una lista que definas en tu programa.
Muestra una representación de la palabra en la que las letras se reemplacen por guiones bajos _. Por ejemplo, si la palabra es "python", la representación sería "_ _ _ _ _ _".

"""
import random
import os
from colorama import Fore

#Dependiendo de la longitud de la palabra, si es mas de 6 caracteres tendra 11 intentos, de lo contrario solo tendra 6
def normas(palabra):
    intentos = 0
    print("Introduce un solo caracter. \n"
          "Si la longitud de la palabra tiene 6 o mas caracteres tendras 11 intentos \n"
          "Si es menor a 6 caracteres tendras 6 intentos \n")
    
    if len(palabra) < 6:
        intentos = 6
        print(Fore.BLUE + f"Tienes {intentos} intentos" + Fore.RESET)
    elif len(palabra) >= 6:
        intentos = 11
        print(Fore.BLUE +f"Tienes {intentos} intentos" + Fore.RESET)
    
    input("Presiona ENTER para continuar...")
    os.system("cls")
    return intentos
    

"""
1.- En esta funcion declaramos una lista estatica con ciertos elementos, hacemos un .choice para elegir una palabra al azar y guardarla en una variable
2.- Haremos una lista con tantas "_" como longitud de letras tenga la palabra elegida, luego la convertimos a string con el metodo .join
3.- Creamos un bucle y en el preguntamos al user la letra que quiere escoger, utilizando ciertas condiciones para que no se introduzca ni un numero ni mas de una caracter
4.- Si la letra escogida esta dentro del indice de la palabra oculta, se sustituira la letra del user en el indice concreto de la palaba secreta,
    ademas de que se guardara esa letra en una lista vacia, para posteriormente realizar una comprobacion y un aviso por si el user vuelve a poner la misma letra que habia acertado
5.- En el caso de fallar la letra, se restara un intento, y si agota todos los intentos se saldra del bucle y acabara el juego
6.- De lo contrario el programa notifica al usuario que ha ganado 
"""
def ahorcado():
    lista_palabras = ["chocolate", "gato", "peluche", "pollito", "jamon", "python", "jugar"]
    palabra = random.choice(lista_palabras)
    
    representacion = ["_"] * len(palabra)
    letras_acertadas = []
    intentos = normas(palabra)
    while intentos >= 0:
        print("Esta es la palabra que debes adivinar:", " ".join(representacion))
        
        user_ask = input("Que letra escoges?: \n").lower()
        
        if not user_ask.isalpha() or len(user_ask) != 1:
            print( Fore.RED + "\nPor favor, ingresa una sola letra y que no sea un numero \n" + Fore.RESET)
            continue
        
        if user_ask in letras_acertadas:
                print(Fore.LIGHTMAGENTA_EX + f"Ya has puesto la letra {user_ask} \n" + Fore.RESET)
        
        elif user_ask in palabra:
            print(Fore.GREEN + f"Has acertado la letra {user_ask}! \n" + Fore.RESET)
            letras_acertadas.append(user_ask)
            for i in range(len(palabra)):
                if palabra[i] == user_ask:
                    representacion[i] = user_ask
        else:
            intentos -= 1
            print(Fore.RED +f"Esa no es!, Te quedan {intentos} intentos \n"+ Fore.RESET)
        
        if "_" not in representacion:
            print(Fore.GREEN + f">>>> Has acertado!! La palabra es {palabra}. Felicidades! <<<<" + Fore.RESET)
            break
            
        if intentos == 0:
            print(Fore.LIGHTCYAN_EX + f"Te quedaste sin intentos!, la palabra era {palabra}" + Fore.RESET)
            break
               
                    
def main():
    os.system("cls")
    print("=======> Bienvenido al juego del Ahorcado! <======= \n")
    
    ahorcado()
    

if __name__ == "__main__":
    main()