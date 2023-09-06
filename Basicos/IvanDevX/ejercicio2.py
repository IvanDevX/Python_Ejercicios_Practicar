"""
2. **Calculadora Simple**: Escribe un programa que realice
una operación matemática simple (suma, resta, multiplicación o división) con dos números ingresados por el usuario.
"""

import os
import time


def choose(numeros_limpios):
    print(" => Elige una Operacion")
    os.system("cls")
    
    # Bucle que te deja elegir que operacion aritmetica quieres hacer , por si queires sumar 
    # y restar los mismos numeros y tambien permite salir.
    
    while True:     
        print(f"\nTus numeros son {numeros_limpios[0]} y {numeros_limpios[1]}\n")
        
        operacion = input("[S]uma, [R]esta, [M]ultiplicar, o [D]ividir - [Q]para Salir: ").lower()
        if operacion == "s":
            print(f"El resultado es: {numeros_limpios[0] + numeros_limpios[1]}")
            
        elif operacion == "r":
            print(f"El resultado es: {numeros_limpios[0] - numeros_limpios[1]}")
            
        elif operacion == "m":
            if numeros_limpios[0] == 0 or numeros_limpios[1] == 0:
                print("Multiplicar por 0 es siempre 0")
            else:
                print(f"El resultado es: {numeros_limpios[0] * numeros_limpios[1]:.2f}")
                
        elif operacion == "d":
            if numeros_limpios[0] == 0 or numeros_limpios[1] == 0:
                print("No puedes dividir entre 0")
            else:
                print(f"El resultado es: {numeros_limpios[0] / numeros_limpios[1]:.2f}")
                
        elif operacion == "q":
            print("Borrando tus numeros... Saliendo de operacion")
            time.sleep(1)
            print("Saliendo de modulo de operaciones...\n"
                  "Redirigiendo a preguntar numeros")
            time.sleep(1)
            break
                
        else:
            print("Error: Introduce alguno de [S / R / M / D / Q]")
            
        
def ask_user():
    # Bucle que maneja errores y permite salir
    
    while True:
        os.system("cls")
        try:
            numeros_entrada = input("Ingresa 2 numeros separados por coma - [Q]para salir :").lower()
            if numeros_entrada == "q":
                print("Adios!")
                break
            numeros_convertidos = numeros_entrada.split(",")
            numeros_limpios = [int(numeros_convertidos[0]),int(numeros_convertidos[1])]
            print(f"Tus numeros son {numeros_limpios}")
            choose(numeros_limpios)
        except (ValueError, IndexError):
            print("Error: introduce 2 numeros separados por una , (coma)")
    
        
def main():
    # Funcion princial del programa
    print(" ====> Calculadora Simple <====")
    ask_user()
    

if __name__ == "__main__":
    main()