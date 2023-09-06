"""
**Contador de Números Pares e Impares**: Desarrolla un programa que cuente cuántos números pares e impares hay en una lista de números.
"""
import os
import random
import time

def lista_automatica():
    # Se genera una lista automaticamente con un len automatico tambien, luego se pasa la lista como parametro a la funcion de pares_impares
    lista_automatica = []
    largo_lista = random.randint(2,20)
    
    while len(lista_automatica) < largo_lista:
        numeros_aleatorios = random.randint(1, 100)
        if numeros_aleatorios not in lista_automatica:
            lista_automatica.append(numeros_aleatorios)
        
    print(f"La lista sera de {largo_lista} numeros.")
    print(f"Esta es tu lista: {lista_automatica}")
    return pares_impares(lista_automatica)
    

def lista_user_comas():
    # El usuario introduce numeros separados por comas, se convierten a int y se retorna la funcion de par impar
    os.system("cls")
    print("Has elegido separados por comas")
    
    while True:
        input_user = input("Introduce los numeros que quieras separados por comas : ")
        try: 
            input_limpio = [int(num) for num in input_user.split(",")]
            print(f"tu lista es : {input_limpio}")
            break
               
        except ValueError:
            print("Error")
            
    return pares_impares(input_limpio)
    

def lista_user_enter():
     # El usuario introduce numeros separados enter
    os.system("cls")
    print("Has elegido enter tras enter")
    lista_enter = []
    print("Introduce los numeros de 1 en 1 con cada enter. ")
    input("Enter para continuar")
    
    while True:
        
        user = input("[00] Para salir. Introduce número: ")
        
        if user == "00":
            break
        
        try:
            numero = int(user)
            if numero not in lista_enter:
                lista_enter.append(numero)
                print(f"Tu lista contiene estos {lista_enter} numeros")
            else:
                print("Número repetido")
        except ValueError:
            print("Solo números... y de uno en uno")
        
    
    return pares_impares(lista_enter)
    
    
def pares_impares(lista):
    """
    Primero se recibe la lista del modo elegido
    Se hacen comprobaciones de la lista antes de seguir.
    Despues se cuentan los numeros impares y pares y se muestran, asi como tambien cuales son los pares e impares
    """
    
    if len(lista) == 0:
        print("Tu lista esta vacia.")
        return
    elif len(lista) == 1:
        print("No esta permitido solo tener un numero en la lista.")
        if 0 in lista:
                print("No se permite tener solo el 0 en la lista")
                return 
        return
    elif 0 in lista:
        print("No se permite tener uno o mas 0 en la lista. Lo eliminare.")
        lista.remove(0)
        
    numeros_pares = 0
    lista_de_pares = []
    numeros_impares = 0
    lista_de_impares = []
    
    for numeros in lista:
        if numeros % 2 == 0:
            numeros_pares += 1
            lista_de_pares.append(numeros)
        else:
            numeros_impares +=1
            lista_de_impares.append(numeros)
            
    print("Dejame pensar...")
    time.sleep(1)
    print("Ya tengo tu contador de pares e impares listo")
    print(f"Tienes un total de {numeros_pares} pares y {numeros_impares} impares")
    print("Te estoy generando la lista..")
    time.sleep(1)
    print(f"Los numeros pares de la lista son : {lista_de_pares}")
    print(f"Los numeros impares de la lista son : {lista_de_impares}")   
    
    
def lista_user():
    # Se pregunta al usuario como quiere añadir los numeros
    os.system("cls")
    print("Prefieres añadir los numeros")
    input_user = input("Separados por [C]omas o 1[A]1 Presionando enter?").lower()
    if input_user == "c":
        return lista_user_comas()
    elif input_user == "a":
        return lista_user_enter()
    else:
        print("Solo tenias que poner bien los caracteres")


def como_crear_lista():
    # Se pregunta al usuario si quiere crear el la lista o que se cree automaticamente.
    print("=> Quieres crear tu la lista o que se genere aleatoriamente? <=")
    
    user = None
    
    while user == None:
        user = input("[H]acer yo la lista\n"
                     "[G]enerar aleatoriamente\n" 
                     "[Q]SALIR \n").lower()
        
    if user == "h":
        os.system("cls")
        lista_user()
    elif user == "g":
        os.system("cls")
        lista_automatica()
    elif user == "q":
        print("Hasta otra!")
        exit()
    else:
        print("Por favor, solo introduce datos validos.")
        
    reintentar = None
    
    while reintentar == None:  
        reintentar = input("\n\nQuieres volver a cargar el programa? [S/N]").lower()
        
    if reintentar == "s":
        main()
    elif reintentar == "n":
        print("Saliendo del programa")
        exit()
    else:
        print("Solo es valido [S o N]")
    

def main():
    # Funcion Main principal
    os.system("cls")
    print("===> Vamos a contar de una lista los numeros pares e impares <===")
    como_crear_lista()
    

if __name__ == "__main__":
    main()