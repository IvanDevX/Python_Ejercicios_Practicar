"""
**Ordenar una Lista**: Desarrolla un programa que ordene una lista de números de menor a mayor.
"""

import os
import random


def ordenar_lista(user_input):
   # El metodo sort ordena la lista original lista.sort() y el metodo sorted(lista) te crea una nueva lista ordenada para usar en una variable
    
    lista = user_input.split(",")
    lista_enteros = [int(num)for num in lista]
        
    # lista_ordenada = sorted(lista_enteros)
    # print(lista_ordenada)
    lista_enteros.sort()
    print(f"La lista ordenada es {lista_enteros}")


def ask_user():
    #En bucle pregunta al usuario que numeros añadir y si quiere seguir creando listas ordenadas
    
    while True:
        try:
            user_input = input("Introduce una lista de numeros separados por coma : ")
            ordenar_lista(user_input)
            
        except ValueError:
            print("Solo numeros")
            
        user_input = input("Quieres ordenar otra lista? [S/N]").lower()
        if user_input == "s":
            os.system("cls")
        else:
            print("Hasta otra!")
            break


def ejemplo():
    lista_ejemplo = []
    
    for a in range(10):
        num = random.randint(1,50)
        if num not in lista_ejemplo:
            lista_ejemplo.append(num)
            
        
    print(f"Ejemplo de lista {lista_ejemplo}")
    lista_ejemplo.sort()
    print(f"Ordenada se veria asi : {lista_ejemplo}")
    print("Te toca!\n")


def main():
    # Funcion principal
    os.system("cls")
    print("Te ordeno la lista")
    ejemplo()
    ask_user()


if __name__ == "__main__":
    main()