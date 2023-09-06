"""
3. **Contador de Números Pares e Impares**: Desarrolla un programa que cuente cuántos números pares e impares hay en una lista de números.

"""
import random
import os

#Preguntamos al usuario que numeros desea añadir a la lista y comprobamos los pares e impares
def ask_user():
    respuesta_user = input("Que numeros deseas agregar a la lista? Separalos por comas: ")
    os.system("cls")
    
    lista_user = respuesta_user.split(",")
    lista_limpia = [int(numero) for numero in lista_user]
    
    print(f"Esta es tu lista: {lista_limpia}, hay un total de {len(lista_limpia)} elementos")
    count_pairs = 0
    count_odd = 0
    for number in lista_limpia:
        if number % 2 == 0:
            count_pairs += 1
        else:
            count_odd += 1 
    print(f"En total en tu lista hay ({count_pairs}) numero(s) par(es), y ({count_odd}) numero(s) impar(es) \n")
    input(" ===> Presiona ENTER para continuar... <=== ")
    os.system("cls")
    another_repeat()
    
#Creamos una lista automaticamente con un tamaño al azar entre 2 y 20
#Comprobamos que el numero que no este en la lista se añada a la lista y una vez hecha la comprobacion si está o no, miramos si es par o impar
def auto_list():
    list_auto = []
    length_list = random.randint(2,20)
    
    count_pairs = 0
    count_odd = 0
    
    while len(list_auto) < length_list:
        random_number = random.randint(1,100)
        if random_number not in list_auto:
            list_auto.append(random_number)
            
            if random_number % 2 == 0:
                count_pairs += 1
            else:
                count_odd += 1
                
    print(f"Esta es la lista: {list_auto}, hay un total de {len(list_auto)} elementos \n")
    print(f"En total en la lista generada hay ({count_pairs}) numero(s) par(es), y ({count_odd}) numero(s) impar(es) \n")
    input(" ===> Presiona ENTER para continuar... <=== ")
    os.system("cls")
    another_repeat()

#Se define una funcion para la eleccion de crear la lista random o hacerla uno mismo, depende cual elijas activara dicha funcion
def user_choose():
    choose_user = input("Deseas crear la tu la lista, o te la genero aleatoriamente? \n"
                        "[C] - Crear yo la lista \n"
                        "[G] - Generame tu la lista \n").lower()
    os.system("cls")
    if choose_user == "c":
        ask_user()
    elif choose_user == "g":
        auto_list()
    else:
        print("Elige una de las dos opciones!")
        user_choose
      
#Funcion para repetir pregunta si quiere volver a iniciar el programa o salirse
def another_repeat():
    while True:
        another_option = input("Entonces... Deseas repetir el programa [S] o [N]? ===> ").lower()
        if another_option == "s":
            print("Okey! Te volvere a preguntar entonces! ")
            os.system("cls")
            user_choose()
        elif another_option =="n":
            print("Vale! Un placer!")
            break
        else:
            os.system("cls")
            print("Porfavor responde con [S] o [N]")
            
        
def main():
    print("===> Bienvenido al contador de numeros pares e Impares! \n"
          "Te preguntare que numeros deseas ingresar o de lo contrario yo te mostrare una lista aleatoria de numeros \n"
          "Una vez creada la lista, te dire cuales son los numeros pares e impares de esa lista <=== \n")
    input(" ===> Presiona ENTER para continuar... <=== ")
    os.system("cls")
    user_choose()
    

if __name__ == "__main__":
    main()