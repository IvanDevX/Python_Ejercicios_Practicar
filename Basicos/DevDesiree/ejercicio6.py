"""
6. **Detección de Números Primos**: Desarrolla un programa que determine si un número ingresado por el usuario es primo o no.

"""


#Preguntamos al usuario que numero ha de ingresar, manejamos errores en el caso de que el usuario introduzca algo que no sea un numero
def ask_user():
    try:
        answer = int(input("Ingresa un numero: \n"))
        return answer
    except ValueError:
        print("Solo se permiten numeros \n")
    

"""
Comprueba si el numero del usuario es primo.
Un numero primo es un numero que SOLO es divisible por 1 y por el mismo, tiene que ser natural y mayor a 2.
Todo numero mayor a 2 se comprueba y si el modulo es 0 sale del bucle y determina que no es primo
Mientras el modulo sea 0 se incrementara el i hasta llegar al anterior al numero de usuario
De esta forma hacemos que cuando detecte que es un numero no primo salga del bucle y no haga tantos ciclos
    
"""
def esPrimo(number_answer):
    
    if number_answer <= 1:
        print(f"{number_answer} no es primo")
    elif number_answer == 2:
        print(f"{number_answer} es primo")
        
    else:
        cont = 0
        i = 2
        while i < number_answer and cont == 0:
            resto = number_answer % i 
            if resto == 0:
                cont +=1
            i += 1 
        
        if cont == 0:
            print(f"{number_answer} es primo")
        else:
            print(f"{number_answer} no es primo")
        
        
def main():
    print("Bienvenido a tu programa para determinar numeros primos\n"
          "Ingresa un numero y te diré si es primo o no \n")
    number_answer = ask_user()
    
    if number_answer:
        esPrimo(number_answer)
    
if __name__ == "__main__":
    main()