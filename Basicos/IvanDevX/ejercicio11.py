"""
11. **Conteo de Vocales** : Desarrolla un programa que cuente cuántas vocales (a, e, i, o, u) hay en una cadena de texto ingresada por el usuario,
independientemente de si las letras son mayúsculas o minúsculas. 
Tambien puedes añadir que cuente cuantos espacios, comas y puntos ahi.

"""

def conteo(frase , ask_user):
    # Declaramos las variables y la lista y con un for iteramos por cada letras y 
    # depende de cada letra y su condicion vamos sumando por cada iteracion. Al final mostramos los datos.
    vocales = 0
    puntos = 0
    espacios = 0
    comas = 0
    lista_vocales = ["a","e","i","o","u"]
    
    for letras in frase:
        if letras in lista_vocales:
            vocales += 1
        if letras == ".":
            puntos +=1
        elif letras == " ":
            espacios +=1
        elif letras == ",":
            comas +=1
            
    print("Ya termine de contar")
    print(f"En tu frase :  ({ask_user}) hay : \n"
          f"{vocales} vocales \n"
          f"{puntos} puntos \n"
          f"{espacios} espacios \n"
          f"{comas} comas. \n")


def frase_user():
    # Con un bucle While preguntamos al usuario la frase y si le parece bien , en caso negativo le pedira que escriba la frase.
    # Despues de alguna comprobacion le pasamos a la funcion conteo la frase del usuario y la frase en minusculas para su conteo.
    while True:
        
        ask_user = input("Escribe tu frase a continuacion [Q]para salir : ==> ")
        frase_minusculas = ask_user.lower()
        if frase_minusculas == "q":
            print("Adios!!")
            break
        
        elif ask_user == "":
            print("Eh!! Frase Vacia. Introduce algo.. o [Q] para salir")
            
        else:
            print("mmmm")
            confirmacion = input(f"Tu frase es : ({ask_user}) es correcta? : [S/N]").lower()
            if confirmacion == "s":
                conteo(frase_minusculas , ask_user)
            

def main():
    # Funcion principal
    print("Voy a contar cuantas vocales, cuantos puntos y comas hay en tu frase")
    frase_user()
    
    
if __name__ == "__main__":
    main()