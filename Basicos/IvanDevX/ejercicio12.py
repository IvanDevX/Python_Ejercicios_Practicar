"""
12. **Generador de Contraseñas** : Escribe un programa que genere contraseñas seguras. 
El programa debe permitir al usuario especificar la longitud de la contraseña y si desea incluir letras mayúsculas,
    letras minúsculas, números y caracteres especiales.
"""

import random
import string

def generate_password(longitud, mayus, minus, numeros, especial):
    """
    1. Recibimos los paremetros y si son TRUE usando la libreria string añadimos a password todos los caracteres
    2. Unas comprobaciones de si es todo FALSE 
    3. Si alguna o todas son TRUE se genera la contraseña. 
    4. Con un buble for elige un caracter random de password y lo añade a un string vacio que con cada iteracion va añadiendo
        caracteres en funcion del rango ( longitud ) y al final retorna la contraseña
    """
    password = ""
    if mayus:
        password += string.ascii_uppercase
    if minus: 
        password += string.ascii_lowercase
    if numeros:
        password += string.digits
    if especial:
        password += string.punctuation
        
    if not password:
        print("Debes seleccionar al menos un tipo de caracter para la contraseña.")
    else:   
        print(f"Mezclando {password} ....")
        passw_generate = ""
        
        for a in range(longitud):
            aleatorio = random.choice(password)
            passw_generate += aleatorio
        
        return passw_generate
        

def questions_user():
    """
    1. Pregunta al usuario la longitud de la contraseña y si queire mayusculas, minusculas, numeros y caracteres especiales
    2. Si las respuestas son s se trata como un TRUE para luego usarlo en generate_password
    3. Se guarda el return de la funcion en una variable y luego se muestra al usuario.
    4. Si no tiene nada la contraseña se envia un error.    
    """
    
    longitud = int(input("Que longitud de contraseña quieres? Ej: 12 . => "))
    mayus = input("Quieres MAYUSCULAS en tu contraseña? [S/N] => ").lower() == "s"
    minus = input("Quieres minusculas en tu contraseña? [S/N] => ").lower() == "s"
    numeros = input("Quieres numeros en tu contraseña? [S/N] => ").lower() == "s"
    especial = input("Quieres caracteres especiales en tu contraseña? [S/N] => ").lower() == "s"
    
    passw_generate = generate_password(longitud, mayus, minus, numeros, especial)
    
    if passw_generate:
        print(f"Te he generado esta contraseña : {passw_generate} ")
    elif not passw_generate:
        print("Un error ha ocurrido, vuelve a intentarlo.")

    
def main():
    # Funcion principal
    print("Generador de Contraseñas Seguras")
    questions_user()
    
    
if __name__ == "__main__":
    main()
