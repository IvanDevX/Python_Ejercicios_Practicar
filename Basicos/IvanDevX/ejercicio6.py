"""
**Detección de Números Primos**: Desarrolla un programa que determine si un número ingresado por el usuario es primo o no.
"""

def ask_user():
    # Pregunta al usuario y maneja excepciones
    try:
        input_user = int(input("Cual es tu numero? : "))
        if comprobar_premio(input_user):
            print(f"{input_user} es un número primo.")
        else:
            print(f"{input_user} no es un número primo.")
    except ValueError:
        print("Solo se permiten numeros.")
    

def comprobar_premio(input_user):
    """
    Comprueba si el numero del usuario es primo.
    Un numero primo es un numero que SOLO es divisible por 1 y por el mismo, tiene que ser natural y mayor a 2.
    Todo numero mayor a 2 se comprueba y si el modulo es 0 sale del bucle y determina que no es primo
    Mientras el modulo sea 0 se incrementara el num hasta igualar al numero de usuario
    De esta forma hacemos que cuando detecte que es un numero no primo salga del bucle y no haga tantos ciclos
    
    """
    if input_user <= 1:
        return False
    elif input_user == 2:
        return True
    else:
        num = 2
        cont = 0
        while num < input_user and cont == 0:
            resto = input_user % num
            if resto == 0:
                cont += 1
            num+= 1
            
        if cont == 0:
            return True
        else:
            return False

            
def main():
    # Funcion principal
    print("Dime un numero y te digo si es primo")
    ask_user()


if __name__ == "__main__":
    main()
    