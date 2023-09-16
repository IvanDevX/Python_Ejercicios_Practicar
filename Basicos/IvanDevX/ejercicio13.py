"""
13. **Convertidor de Decimal a Binario** : 
Escribe un programa que convierta un número decimal ingresado por el usuario a su equivalente en sistema binario.
"""
# Web usada para saber como se convierten : https://ed.team/blog/sistemas-binarios-y-decimales


def binario_to_decimal(input_user):
    """
    1. Se crea una lista vacia. 
    2. Se hace un for para pasar cada numero a str y se añade a la lista numeros_reversos
    3. Se declaran 2 variables con valor 0 ( suma y potencia)
    4. Con un for se recorre cada numero de la lista numeros reversos y se crea una variable result
        que contiene el numero de la lista a entero *2 potencia de 0 en la primera iteracion, 
        que va subiendo la potencia con cada iteracion.
        Al final del for se va sumando los resultados
    5. Por ultimo se devuelve la suma
    
    """
    numeros_reversos = []
    for a in str(input_user):
        numeros_reversos.append(a)
        
    numeros_reversos.reverse()
    
    suma = 0
    potencia = 0
    
    for num in numeros_reversos:
        result = int(num) * 2 ** potencia
        suma += result
        potencia += 1
        
    return suma
        

def decimal_to_binario(input_user):
    """
    1. Se crea una lista vacia para almacenar los numeros
    2. A traves del while hasta que input_user valga 0 se ejecuta
    3. Dentro del while hacemos modulo de input user y añadimos el resto a la lista, a su vez cambiamos el valor de input user
    4. Con un bucle for vamos añadiendo a un str los numeros de la lista y los retornamos
    
    """
    lista_a_binario = []
    
    while input_user > 0:
        resto = input_user % 2
        lista_a_binario.append(resto)
        input_user = input_user // 2
    lista_a_binario.reverse()
    
    numero_binario = ""
    for a in lista_a_binario:
        numero_binario += str(a)
        
    return numero_binario


def ask_user():
    """
    1- Se le pregunta al usuario que conversion quiere hacer
    2- Se le pide que introduzca el numero que quiere convertir
    3- Se ejecuta la funciona pasando como parametro el numero del usuario
    4- Se devuelve el resultado de la funcion
    
    """
    try:
        input_user = int(input("[1] = Binario a Decimal \n"
                                "[2] = Decimal a Binario \n"
                                "Que quieres hacer? : "))
        if input_user == 1:
            print("Binario a Decimal elegido")
            input_user = int(input("Introduce tu numero : "))
            binario_resultado = binario_to_decimal(input_user)
            print(f"El numero binario {input_user} es : {binario_resultado} en decimal.")
            
        elif input_user == 2:
            print("Decimal a Binario elegido")
            input_user = int(input("Introduce tu numero : "))
            decimal_resultado = decimal_to_binario(input_user)
            print(f"El numero decimal {input_user} es : {decimal_resultado} en binario.")
    except ValueError:
        print("Solo numeros")
        ask_user()

def main():
    # Funcion principal
    print("Convertidor de Decimal a Binario y viceversa")
    ask_user()
    
    
if __name__ == "__main__":
    main()
