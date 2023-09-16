"""
11. **Conteo de Vocales** : Desarrolla un programa que cuente cuántas vocales (a, e, i, o, u) hay en una cadena de texto ingresada por el usuario, 
independientemente de si las letras son mayúsculas o minúsculas. 
Tambien puedes añadir que cuente cuantos espacios, comas y puntos ahi.
"""
import os
from colorama import Fore


# Creamos una lista con vocales y contadores de caracteres especiales, luego creamos un bucle que pregunte al usuario que frase quiere escribir.
# Realizamos comprobacion si introduce un campo vacio. 
# Si todo esta bien se hara un bucle FOR comparando cada letra de la frase dentro de la lista de vocales y si coinciden se sumaran al contador
# Tambien se comprueban con condicionales si coinciden con los caracteres que se piden y si es asi, se sumaran al contador
def conteo():
    lista_vocales = ["a", "e" , "i" , "o" , "u"]
    vocales = 0
    espacios = 0
    comas = 0
    puntos = 0
    
    while True:
        respuesta = input("Introduce una frase, [Q] para salir: ==> \n").lower()
        
        if len(respuesta) == 0:
            print(Fore.RED + "No dejes el campo vacio! \n" + Fore.RESET)
            
        elif respuesta == "q":
            print("Nos vemos!")
            break   
        else:
            for letras in respuesta:
                if letras in lista_vocales:
                    vocales += 1
                elif letras == " ":
                    espacios += 1
                elif letras == ",":
                    comas += 1
                elif letras == ".":
                    puntos += 1
                
            print(f"Tu frase contiene: {vocales} vocal[es], {espacios} espacio[s], {comas} coma[s] y {puntos} punto[s] \n")
    

def main():
    os.system("cls")
    print("Voy a contar cuantas vocales, espacios, comas y puntos hay en tu frase \n")
    conteo()

if __name__ == "__main__":
    main()