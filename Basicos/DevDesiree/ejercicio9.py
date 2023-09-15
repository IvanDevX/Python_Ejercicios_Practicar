"""
9. **Ordenar una Lista**: Desarrolla un programa que ordene una lista de números de menor a mayor.

"""

import os
from colorama import Fore
# El metodo sort ordena una lista original => lista.sort() y el metodo sorted te crea una nueva lista para usar en una variable => a = sorted(lista)

def ask_user():
    lista_limpia = []
    # Manejamos errores en cuanto a que deben ser solo numeros y separados por comas
    # Una vez sigue el bucle preguntamos al user de nuevo si quiere agregar mas numeros
    while True:
        try:
            answer = input("Que numeros deseas agregar a la lista? Separalos por comas: \n")
            lista = answer.split(",")
            lista_enteros = [int(numero) for numero in lista]
            order_list(lista_enteros, lista_limpia)  
    
        except ValueError:
            print(Fore.RED + "Por favor, ingresa una lista válida de números separados por comas \n" + Fore.RESET)
            
    
        new_answer = input(Fore.GREEN + "Deseas agregar mas numeros a la lista? [S] o [N]: \n" + Fore.RESET).lower()
        
        if new_answer == "s":
            os.system("cls")
        else:
            print("Okey, nos vemos!")
            break

# Pasamos los numeros a una lista limpia y luego utilizamos el metodo sort, para ordenar los numeros que ha introducido el usuario
def order_list(lista_enteros, lista_limpia):
    for number in lista_enteros:
        if number not in lista_limpia:
            lista_limpia.append(number)
    
    lista_limpia.sort()

    print(f"=====> Tu lista ordenada es: {lista_limpia} <=====")
    
    
def main():
    os.system("cls")
    print(Fore.BLUE + "Introduce los numeros en una lista, separados por comas y yo te la ordenare de menor a mayor \n" + Fore.RESET)
    ask_user()

if __name__ == "__main__":
    main()