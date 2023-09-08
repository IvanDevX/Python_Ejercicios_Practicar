"""
5. **Conversión de Grados Celsius a Fahrenheit**: Escribe un programa que convierta grados Celsius a grados Fahrenheit.

"""

import os
from colorama import Fore


#El usuario debe elegir entre las opciones, que opcion de conversion quiere utilizar
def welcome_message():
    os.system("cls")
    while True:
        first_choose = input("Que eliges convertir? : \n" +
                            Fore.LIGHTMAGENTA_EX + "De Celsius a Fahreneiht [1] \n" + Fore.RESET +
                            Fore.BLUE + "De Fahrenheit a Celsius [2] \n" + Fore.RESET +
                            Fore.RED + "[Q para salir] \n" + Fore.RESET).lower()
        
        if first_choose == "1":
            conversion_fahrenheit()
        elif first_choose == "2":
            conversion_celsius()
        elif first_choose == "q":
            print("Nos vemos!!")
            break
        else:
            os.system("cls")
            print(Fore.RED + "Porfavor solo elige entre una de las opciones!! \n" + Fore.RESET)

#Convertimos los grados Fahrenheit a Celsius y manejamos errores
def conversion_celsius():
    os.system("cls")
    try:
        print(Fore.BLUE + "Has elegido la conversion de Fahrenheit a Celsius \n" + Fore.RESET )
        input_celsius = float(input("Ingresa los grados Fahrenheit para convertir a Celsius: \n"))
        
        result_celsius = (input_celsius - 32) * 5/9
        
        print(Fore.GREEN + f"Tu resultado de Fahrenheit a Celsius es: {result_celsius:.2f}º" + Fore.RESET)
    except ValueError:
        print(Fore.RED +"Ingresa solo numeros!! \n" + Fore.RESET)
        
    last_choose()

#Convertimos los grados Celsius a Fahrenheit y manejamos errores
def conversion_fahrenheit():
    os.system("cls")
    try:
        print( Fore.LIGHTMAGENTA_EX + "Has elegido la conversion de Celsius a Fahreneiht \n" + Fore.RESET)
        input_fahrenheit = float(input("Ingresa los grados Celsius para convertir a Fahrenheit: \n"))
        
        result_fahrenheit = (input_fahrenheit * 9/5) + 32
        print(Fore.GREEN + f"Tu resultado de Celsius a Fahrenheit es: {result_fahrenheit:.2f}º" + Fore.RESET)
        
    except ValueError:
        print(Fore.RED +"Ingresa solo numeros!! \n" + Fore.RESET)
   
    last_choose()
    
#Realiza una pregunta adicional de si desea continuar despues de la conversion previa
def last_choose():
    choose = input("\nDeseas realizar otra operacion? [S]i o [N]o: \n").lower()
    
    if choose == "s":
        welcome_message()
    elif choose == "n":
        print(Fore.BLUE + "Okey ! Un placer ! \n" + Fore.RESET)
        exit()
    else:
        print(Fore.RED + "Elige Si o No ! \n" + Fore.RESET)

def main():
    print("Bienvenido a tu calculadora de Celsius y Fahrenheit!! \n")
    welcome_message()


if __name__ == "__main__":
    main()