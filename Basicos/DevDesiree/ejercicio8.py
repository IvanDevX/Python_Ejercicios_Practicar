"""
8. **Generador de Tablas de Multiplicar**: Escribe un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

"""

import os

#Preguntamos al user que numero desea operar, y creamos las condiciones y manejo de errores dentro de un bucle, el cual se cerrara al crearse la condicion de escribir el 0
def user_ask():
    
    while True:
        try:
           number_user = int(input("Que numero deseas multiplicar?: [0] para salir \n"))
           
           if number_user == 0:
               print("Nos vemos!")
               break
           else:
            choosen_number(number_user)
           
        except ValueError:
            print("Solo numeros, por favor!")

#Con el numero seleccionado recorremos los numeros dentro de un rango que se multiplicaran por el numero escogido por el user
def choosen_number(number_user):
    os.system("cls")
    for a in range(1,11):
        print(f"{number_user} x {a} = {number_user * a}")
        
        
def main():
    os.system("cls")
    print("======> Bienvenido a tu calculadora! <======\n"
          "Introduce un numero y te lo multiplicare por la tabla correspondiente \n")
    user_ask()
if __name__ == "__main__":
    main()