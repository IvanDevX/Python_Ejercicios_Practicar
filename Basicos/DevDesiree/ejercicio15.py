"""
15. **Calculadora de Suma de Series** : Escribe un programa que calcule la suma de una serie de números ingresados por el usuario. 
El usuario debe poder ingresar números uno por uno y detener la entrada cuando lo desee. 
El programa debe mostrar la suma total de los números ingresados.
"""
import os
from colorama import Fore


def ask_user_and_calc():
    """
    1.- Definimos variables save_number y number_list fuera del bucle
    2.- Creamos un bucle infinito con manejo de errores (si el user escribe una letra en vez de numero) y preguntamos al user que numero desea escribir
    3.- Luego le volvemos a preguntar si qiere añadir otro numero, y en el caso de que no quiera, pulsara 0 y se cerrara el bucle mostrando el resultado final
    4.- Si el usuario sigue añadiendo numeros, se añadiran y guardaran en una variable (save_number) que se iran sumando conforme siga el bucle
    5.- Se iran mostrando los numeros escogidos y al final se mostrara un mensaje final con la suma total de todos los numeros introducidos
    
    """
    save_number = 0
    numbers_list = []
    
    while True:
        try: 
            print(Fore.LIGHTMAGENTA_EX + "Escribe 0 Para terminar y hacer el calculo \n" + Fore.RESET)
            numbers_user = int(input("Introduce el numero para añadir: \n"))
            
            save_number += numbers_user
            
            if numbers_user == 0:
                break
            numbers_list.append(numbers_user)
            print(Fore.CYAN + f"Estos son tus numeros de momento: {numbers_list} \n" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Por favor introduce solo numeros! \n" + Fore.RESET)
            
    print(Fore.GREEN + f"Okey! La suma total de: {numbers_list} es: {save_number}" + Fore.RESET)
    
    
def main():
    os.system("cls")
    print("----> Bienvenido a tu calculadora de numeros en serie <---- \n"
          "Introduce una serie de numeros y te hare la suma total de todos ellos \n")
    ask_user_and_calc()
    
    
if __name__ == "__main__":
    main()