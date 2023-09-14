"""
7. **Lista de Números Únicos**: Crea una función que tome una lista de números y devuelva una lista con valores únicos, eliminando duplicados.

"""
import os

#Preguntamos al usuario que numeros agregar, una vez introducidos, los separamos por comas y creamos una lista de numeros enteros
def ask_user():
    lista_limpia = []
    #Manejamos errores en cuanto a que deben ser solo numeros y separados por comas
    while True:
        try:
            answer = input("Que numeros deseas agregar a la lista? Separalos por comas: \n")
            lista = answer.split(",")
            lista_enteros = [int(numero) for numero in lista]
            remove_duplicates(lista_enteros, lista_limpia)  
    
        except ValueError:
            print("Por favor, ingresa una lista válida de números separados por comas")
            
    
        new_answer = input("Deseas agregar mas numeros a la lista? [S] o [N]: \n").lower()
        
        if new_answer == "s":
            os.system("cls")
        else:
            print("Okey, nos vemos!")
            break
        
#Recorremos la lista de los numeros agregados previamente, y si hay un numero que no se encuentra en esa lista, se añadira a una nueva lista limpia
def remove_duplicates(lista_enteros, lista_limpia):
    for number in lista_enteros:
            if number not in lista_limpia:
                lista_limpia.append(number)
    print(f"Tu lista es: {lista_limpia}")
    
       
def main():
    os.system("cls")
    print("Repite numeros que quieras, yo eliminare todos los numeros repetidos de esa lista \n")
    
    ask_user()
    

if __name__ == "__main__":
    main()
    
    