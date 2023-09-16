"""
12. **Generador de Contraseñas** : Escribe un programa que genere contraseñas seguras. 
El programa debe permitir al usuario especificar la longitud de la contraseña y si desea incluir letras mayúsculas, letras minúsculas, números y caracteres especiales.

"""
import random
import string
import os


   
def generate_pass(longitud, mayusculas, minusculas, numeros, caracteres):
    """
    1.- Creamos una variable vacia de password, en la que si el usuario a dicho que quiere agregar ciertos elementos desde la otra funcion, se añadiran los elementos seleccionados a esa variable
    2.- En el caso de no haberse introducido ningun elemento dara error
    3.- Si todo va bien, se usa un FOR recorriendo con un range la longitud que nos ha dado el usuario
    4.- Se agrega una variable password_generate que contiene los elementos seleccionados al azar y se guardan ahi
    5.- Despues se va sumando cada elemento de password_generate a otra variable (password_final) para poder agregarlos todos sin que se sobreescriban
    """ 
    password = ""
    if mayusculas:
        password += string.ascii_uppercase
    if minusculas:
        password += string.ascii_lowercase
    if numeros:
        password += string.digits
    if caracteres:
        password += string.punctuation
    
    
    if not password:
        print("Introduce al menos uno de los caracteres para poder crear la contraseña. \n")  
        user_questions()  
    else:     
        print("Vale! Generando Contraseña...... \n")
        password_final = ""
        for ch in range(longitud):
            password_generate = random.choice(password)
            password_final += password_generate
            
        print(f"Esta es tu contraseña generada: {password_final}")   
       
        
def user_questions():
    # Se pregunta al usuario una serie de preguntas, que luego se llevaran como parametro a la funcion generate_pass
    # Dependiendo de si el usuario responde si o no, se daran las variables como TRUE si selecciona "s" y FALSE si selecciona "n"
    longitud = int(input("Que longitud de contraseñas deseas => \n"))
    mayusculas = input("Quieres añadir Mayusculas? [S] / [N] => \n").lower() == "s"
    minusculas = input("Quieres añadir Minusculas? [S] / [N] => \n").lower() == "s"
    numeros = input("Quieres añadir Numeros? [S] / [N] => \n").lower() == "s"
    caracteres = input("Quieres añadir Caracteres Especiales? [S] / [N] => \n").lower() == "s"
    
    generate_pass(longitud, mayusculas, minusculas, numeros, caracteres)
    
     
def main():
    os.system("cls")
    print("======> Bienvenido a tu generador de contraseñas seguras <====== \n")
    user_questions()
    

if __name__ == "__main__":
    main()