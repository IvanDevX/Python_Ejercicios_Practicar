"""
4. **Adivina el numero**: Escribe un programa en Python que genere un número aleatorio entre 1 y 100 (inclusive) y permita al usuario adivinar ese número. 
El programa debe proporcionar pistas al usuario indicando si el número a adivinar es mayor o menor que el número que ha ingresado.
Debe continuar permitiendo al usuario adivinar hasta que adivine el número correcto.

"""

import random
import os
from colorama import Fore, Style 


    
#Creamos pregunta para que el usuario introduzca el numero
def pregunta_user():
    return int(input("¿Que numero estoy pensando ahora mismo?:\n "))

#Comparamos si la respuesta del user esta en la lista que muestra los numeros que ha ido diciendo, si no está se añade, y si coincide no se añadirá
def comparar_repes(user_ask, recuento_numeros):
    
    if user_ask not in recuento_numeros:
        recuento_numeros.append(user_ask)
    else:
        print(Fore.RED + f"Además, el numero {user_ask} ya lo has dicho! \n" + Style.RESET_ALL)
        
    print(f"Los numeros que has dicho son: {recuento_numeros} ")

#Comparamos los numeros del usuario para ver si coinciden con el de la maquina, si es menor o mayor al numero pensado por la maquina te dara una pista
#Tenemos manejo de errores en el caso de que no se introduzca un numero
def comparar_numeros():
    number_machine = random.randint(1,100)
    contador = 0
    recuento_numeros = []
    while True:
        try:
            user_ask = pregunta_user()
            os.system("cls")
            if user_ask == number_machine:
                print(Fore.GREEN + f"Ole!! Felicidades! Has acertado que era el numero {number_machine} " + Style.RESET_ALL)
                print(f"Has hecho un total de {contador} intentos\n")
                break
            elif user_ask < number_machine:
                print(Fore.BLUE + f"Mmm... te diria que mas arriba del {user_ask}\n" + Style.RESET_ALL)
                comparar_repes(user_ask, recuento_numeros)
            elif user_ask > number_machine:
                print(Fore.BLUE + f"Nop, esta un poco mas abajo del {user_ask}\n +" + Style.RESET_ALL)
                comparar_repes(user_ask, recuento_numeros)
            contador +=1
        except ValueError:
            print("Debe ser un numero!\n")
            
        print(f"Llevas {contador} intentos")
            
def main():
    os.system("cls")
    print("Bienvenido al juego de adivina al numero! Debes acertar el numero que estoy pensando ahora mismo.. \n"
          "Te dare algunas pistas si es menor o mayor al numero que me has dicho, suerte! \n")
    input("¡Vamos a comenzar!, Cuando estes listo, pulsa ENTER")
    os.system("cls")
    comparar_numeros()
    
    
    
if __name__ == "__main__":
    main()