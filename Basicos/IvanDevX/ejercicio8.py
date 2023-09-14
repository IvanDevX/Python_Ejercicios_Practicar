"""
8. **Generador de Tablas de Multiplicar**: Escribe un programa que genere la tabla de multiplicar de un número ingresado por el usuario.
"""
import os

def generar_tabla(input_user):
    # Borra la consola y mediante un for multiplica el numero por cada iteracion de rango.
    os.system("cls")
    print(f"La tabla de multiplicar del {input_user} es: ")
    
    for a in range(1,11):
        print(f"{input_user} x {a} = {input_user * a}")
    

def ask_user():
    # Se le pregunta al usuario con un bucle while que numero quiere multiplicar y con el numero 0 rompe el while
    while True:
        try:
            input_user = int(input("\nIntroduce un numero y te hare su tabla de multiplicar - Introduce el 0 para salir."
                                   "\nTu numero es : "))
            if input_user == 0:
                print("Adios")
                break
            elif input_user < 0:
                print("Por favor, introduce un número positivo.")
            else:
                generar_tabla(input_user)
                
        except ValueError:
            print("Introduce solo un numero entero.")


def main():
    # Funcion principal
    os.system("cls")
    print(">>>Te voy a crear la tabla de multiplicar del numero que quieras.<<<")
    ask_user()

if __name__ == "__main__":
    main()