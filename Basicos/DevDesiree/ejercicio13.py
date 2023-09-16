"""
13. **Convertidor de Decimal a Binario** : 
Escribe un programa que convierta un número decimal ingresado por el usuario a su equivalente en sistema binario.

"""
import os
from colorama import Fore

def ask_user():
    # Preguntamos al usuario que opcion escoger, y en base a esa opcion ira a la funcion correspondiente
    choose_user = input("¿Que eliges convertir?: \n"
                        "De [B]inario a Decimal \n"
                        "De [D]ecimal a Binario \n").lower()
    
    if choose_user == "b":
        print("Has seleccionado de Binario a Decimal! \n")
        binary_to_decimal()
    elif choose_user == "d":
        print("Has seleccionado de Decimal a Binario! \n")
        decimal_to_binary()
    else:
        print(Fore.RED + "Elige una de esas opciones! \n" + Fore.RESET)
        ask_user()
        
        
def binary_to_decimal():
    """
    1.- Guardamos la respuesta del user en una variable, y esa variable la guardamos en otra pero invirtiendo los digitos
    2.- Creamos 2 variables de potencia y suma
    3.- Creamos un FOR que recorra el numero introducido por el user, y a cada iteracion guardamos el resultado de la operacion en la variable (resultado)
    4.- Incrementamos en 1 por cada iteracion la variable potencia para que cambie en la operacion 
    5.- Tambien guardamos en una variable (suma) el resultado de cada iteracion de la variable (resultado) y lo vamos sumando hasta acabar el bucle
    """
    try:
        input_user = input("Que numero deseas convertir a Decimal?: \n ")
        input_reverse = input_user[::-1]
        
        print(input_reverse)
        
        potencia = 0
        suma = 0
        
        for a in input_reverse:
            resultado = int(a) * 2 ** potencia
            potencia += 1
            suma += resultado
            
        print(f"El resultado de Binario a Decimal es: {suma}") 
    except ValueError:
        print( Fore.RED + "Por favor, solo numeros! \n" + Fore.RESET)
        binary_to_decimal()
    
    
def decimal_to_binary():
    """
    1.- Creamos una lista vacia (a_binario) y guardamos la respuesta del user en una variable
    2.- Creamos un Bucle WHILE con la condicion que mientras el input del user sea mayor a 0 siga ejecutandose
    3.- Dentro del bucle creamos una variable (resto) que guarda la operacion de un resto
    4.- Guardamos ese resto en la lista vacia que creamos antes
    5.- Modificamos la variable input_user por cada iteraccion con el resultado del mismo dividido entre dos 
    6.- Al acabar el bucle, le damos la vuelta a la lista que le hemos ido agregando el resto
    7.- Creamos una variable vacia (numero_binario) y hacemos un bucle FOR que vaya iterando y sumando los numeros agregados de esa lista entre si para obtener el resultado
    """
    try:
        a_binario = []
        input_user = int(input("Que numero deseas convertir a Binario?: \n "))
        
        while input_user > 0:
            resto = input_user % 2
            a_binario.append(resto)
            input_user = input_user // 2
            
        a_binario.reverse()
        
        numero_binario = ""
        
        for a in a_binario:
            numero_binario += str(a)
        
        print(f"El resultado es Decimal a Binario es : {numero_binario}") 
    except ValueError:
        print( Fore.RED + "Por favor, solo numeros! \n" + Fore.RESET)
        decimal_to_binary()
        

def main():
    os.system("cls")
    print("====> Bienvenido a tu conversor de Binario a Decimal y Viceversa! <====")
    ask_user()


if __name__ == "__main__":
    main()