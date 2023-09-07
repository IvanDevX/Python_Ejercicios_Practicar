"""
4. **Adivina el numero**: Escribe un programa en Python que
genere un número aleatorio entre 1 y 100 (inclusive) y permita al usuario adivinar ese número. 

El programa debe proporcionar pistas al usuario indicando si el número a adivinar es mayor o menor que el número que ha ingresado.
Debe continuar permitiendo al usuario adivinar hasta que adivine el número correcto.

"""
import os
import random


def adivina_numero():
    print("Estoy pensando en un numero y tienes que adivinarlo. Es del 1 al 100 con ambos incluidos")
    numero_aleatorio = random.randint(0,100)
    intentos = 0
    lista_numeros_input = []
    
    while True:
        # bucle que maneja errores y comprueba si el usuario ha acertado y si el numero es repetido
        try:
            input_user = int(input("==> Dime un numero : "))
            
            if input_user == numero_aleatorio:
                os.system("cls")
                print(f"Tu numero / Numero maquina: {input_user}/{numero_aleatorio}")
                print(f"Numero de intentos : {intentos}")
                if intentos == 0:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Como? A la primera? What! Que fiera")
                
                elif intentos < 5:   
                    print("En menos de 5 intentos, no esta mal")
                    
                else:
                    print("Ole!! Has acertado por fin")
                    
                break
            elif numero_aleatorio < input_user:
                print(f"El numero que buscas es menor (<) a {input_user}")
                intentos += 1
            elif numero_aleatorio > input_user:
                print(f"El numero que buscas es mayor (>) a {input_user}")
                intentos += 1   
                   
            if input_user in lista_numeros_input:
                os.system("cls")
                print(f"El {input_user} ya lo habias dicho antes..")
                print("Tienes suerte que no te añada otro intento.")
                print(f"Los numeros que has dicho son {lista_numeros_input}")
                input("ENTER PARA CONTINUAR")
            else:
                lista_numeros_input.append(input_user)   
                 
        except ValueError:
            print("Solo es valido numeros.")
             
    
def generar_titulo(titulo):
    # generar titulo para que quede bonito visualmente
    print("\n" + "*" * len(titulo))
    print(titulo)
    print("*" * len(titulo) + "\n")


def main():
    os.system("cls")
    generar_titulo("=> Adivina el numero <=")
    adivina_numero()
    generar_titulo("=> Fin del Juego <=")
    

if __name__ == "__main__":
    main()