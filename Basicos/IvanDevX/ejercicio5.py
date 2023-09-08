"""
5. **Conversión de Grados Celsius a Fahrenheit**: Escribe un programa que convierta grados Celsius a grados Fahrenheit.
"""

import os


def celsius_a_fahrenheit(celsius):
    # Conversion de celsius a fahrenheit
    os.system("cls")
    print("Has elegido de Celsius a Fahrenheir")
    formula_a_celsius = (celsius * 9/5) + 32
    return print(f"{celsius}°C son {formula_a_celsius:.2f}°F")


def fahrenheit_a_celsius(fahrenheit):
    # Conversion de fahrenheit a celsius
    os.system("cls")
    print("Has elegido Fahrenheir a Celsius")
    formula_a_fagrenheit = (fahrenheit - 32) * 5/9
    return print(f"{fahrenheit}°C son {formula_a_fagrenheit:.2f}°F")


def volver_programa():
    # Volver a ejecutar el programa si el usuario quiere
    user_ask = input("\n\nQuieres volver a ejecutar el programa?\n"
                     "[Y]es or [N]o : \n").lower()
    
    if user_ask == "y":
        os.system("cls")
        main()
        
    else:
        print("Ha sido un placer! Adios")
        

def conversiones(temp_user):
    # Darle al usuario una opcion a elegir
    os.system("cls")
    print(f"Tu has escrito : {temp_user}°")
    
    while True:
        try: 
            user_ask = int(input("¿Que opcion eliges?\n"
                            "1- Celsius a Fahrenheit \n"
                            "2- Fahrenheir a Celsius \n"
                            "3- Salir \n"
                            "==> : "))
            if user_ask:
                break
            
        except ValueError:
            print("Introduce solo las opciones disponibles.")
        
    if user_ask == 3:
        print("Adios!")
        exit()

    elif user_ask == 1:
        celsius_a_fahrenheit(temp_user)
        
    elif user_ask == 2:
        fahrenheit_a_celsius(temp_user)
    else:
        print("Solo las opciones disponibles")
       
    volver_programa()


def pregunta_user():
    # Preguntar por la temperatura que quiere convertir
    os.system("cls")
    
    while True:
        try:
            temp_user = float(input("Introduce la temperatura : "))
            if temp_user is not None:
                conversiones(temp_user)
            
            break
            
        except ValueError:
            print("\nSolo es valido usar numeros y si son decimales separados por .")
            print("El formato correcto es : 23 o 23.4\n")
        


def main():
    # Main principal
    print("==> Bienvenido al conversor de temperatura Celsius / Fahrenheit y viceversa <==")
    pregunta_user()
    

if __name__ == "__main__":
    main()