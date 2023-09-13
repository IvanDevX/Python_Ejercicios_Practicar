"""
6. **Detección de Números Primos**: Desarrolla un programa que determine si un número ingresado por el usuario es primo o no.

"""



def ask_user():
    try:
        answer = int(input("Ingresa un numero: "))
        return answer
    except ValueError:
        print("Solo se permiten numeros")
    

#Comprueba si el numero es primo
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
          "Ingresa un numero y te diré si es primo o no")
    number_answer = ask_user()
    
    if number_answer:
        esPrimo(number_answer)
    
if __name__ == "__main__":
    main()