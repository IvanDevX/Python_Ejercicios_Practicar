"""
1. **Encriptacion de texto** : Crea un modulo con los caracteres de encriptacion y desencriptacion
y haz una aplicacion para cifrar un texto. Tambien puedes usar el cifrado Cesar
"""

from caracteres import diccionario_caracteres as dictionary


def encriptar(texto_user):
    """
    1- Recorrer la frase del usuario y comprobar si la clave coincide , si coincide se devuelve el valor
    
    """
    frase = ""
    print(f"Tu texto es : {texto_user}")
    
    for a in texto_user:
        if a in dictionary:
            frase += dictionary[a]
        else:
            frase += a
            
    print(f"Tu frase encriptada es : {frase}")
            
    return frase


def desencriptar(texto_user):
    """
    1- Recorrer la frase del usuario y si el caracter esta en el valor del diccionario, recorrer el diccionario y sustituir 
        el caracter por su clave en vez de su valor.
    
    """
    frase = ""
    print(f"Tu texto es : {texto_user}")
    
    for a in texto_user:
        if a in dictionary.values():
            for clave, valor in dictionary.items():
                if valor == a:
                    frase += clave
                    break  
        else:
            frase += a   
            
    print(f"Tu frase desencriptada es : {frase}")
            
    return frase


def comprobar_texto(texto_user):
    # Pequeñas comprobaciones por si el texto esta vacio o con espacios en blanco
    if not texto_user.strip():
        print("No se permite texto vacío o espacios en blanco")
        exit()


def texto_user():
    # Preguntar al usuario que quiere, y en funcion de su respuesta hacer una funcion o otra.
    try:
        input_user = input("¿Quieres [E]ncriptar o [D]esencriptar tu texto? [E / D] : ").lower()
        if input_user == "e":
            texto_user = input("Que texto quieres encriptar?")
            comprobar_texto(texto_user)
            encriptar(texto_user)
            
            
        elif input_user == "d":
            texto_user = input("Que texto quieres desencriptar?")
            comprobar_texto(texto_user)
            desencriptar(texto_user)
            
        else:
            print("No has elegido ninguna opcion disponible")
            
    except ValueError:
        print("Introduce solo texto.")


def main():
    # Funcion principal
    print("Encriptemos / Desencriptemos el texto que me digas")
    texto_user()


if __name__ == "__main__":
    main()
