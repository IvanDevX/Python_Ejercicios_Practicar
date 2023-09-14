"""
**Lista de Números Únicos**: Crea una función que tome una lista de números y devuelva una lista con valores únicos, eliminando duplicados.
"""
import os


def limpiar_lista(user_input , lista_limpia):
    # Coge la lista de str , la corta por la , y luego cambia el numero a int. Al final la imprime
    
    lista = user_input.split(",")
    lista_enteros = [int(num)for num in lista]
        
    for a in lista_enteros:
        if a not in lista_limpia:
            lista_limpia.append(a)
    print(f"Tu lista es {lista_limpia}:")


def ask_user():
    # Crea la lista vacia limpia y en bucle pregunta al usuario que numeros añadir y si quiere seguir añadiendo
    lista_limpia = []
    while True:
        try:
            user_input = input("Introduce una lista de numeros separados por coma : ")
            limpiar_lista(user_input , lista_limpia)
            
        except ValueError:
            print("Solo numeros")
            
        user_input = input("Quieres añadir mas numeros? [S/N]").lower()
        if user_input == "s":
            os.system("cls")
        else:
            print("Hasta otra!")
            break


def main():
    # Funcion principal
    os.system("cls")
    print("Elimino los duplicados de tu lista numerica")
    ask_user()


if __name__ == "__main__":
    main()