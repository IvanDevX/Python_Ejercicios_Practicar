"""
15. **Calculadora de Suma de Series** : Escribe un programa que calcule la suma de una serie de números ingresados por el usuario.
El usuario debe poder ingresar números uno por uno y detener la entrada cuando lo desee. 
El programa debe mostrar la suma total de los números ingresados.
"""

def ask_user_and_calculated():
    """
    1- Se declaran variables y lista vacia
    2- Con un While se pregunta al usuario que introduzca un numero y con un try se manejan errores
    3- Por cada iteracion del bucle se va sumando a la varible suma_total los int del usuario y a la vez se guardan en una lista.
    4- Al final muestra la suma total y los numeros que ha ido facilitando.
    """
    
    print("Dame numeros de 1 en 1 y te digo el total de todo.")
    
    suma_total = 0
    numeros_escritos = []
    
    while True:
        print("Si quieres salir y mostrar el total pulsa el 0")
        try:
            number = int(input("El numero es? : "))
            if number == 0:
                break
            suma_total += number
            numeros_escritos.append(number)
            
        except ValueError:
            print("Introduce solo numeros enteros.")
            
    print("Calculando....")
    print(f"Tus numeros han sido : {numeros_escritos}")
    print(f"La suma total de toda la serie es : {suma_total}")
        

def main():
    # Funcion Principal
    print("Calculadora de suma en Serie")
    ask_user_and_calculated()


if __name__ == "__main__":
    main()