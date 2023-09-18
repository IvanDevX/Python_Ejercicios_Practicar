"""
14. **Conversor de Moneda** : Escribe un programa que convierta una cantidad de dinero en una moneda a otra. 
El usuario debe ingresar la cantidad, la moneda de origen y la moneda de destino, y el programa debe proporcionar la conversión.
"""

import os


def choosen_user():
    """
    1.- Establecemos un diccionario con diferentes monedas y valores, recorremos cada valor para mostrar la lista completa de monedas en el print
    2.- Preguntamos al user que moneda de origen y destino quiere convertir y la cantidad, las retornamos para usar posteriormente
    3.- Manejamos errores por si el user introduce una string a la hora de preguntar la cantidad
    """
    tasas_de_cambio = {
        "USD": 1.0,    # Dólar estadounidense
        "EUR": 0.85,   # Euro
        "GBP": 0.73,   # Libra esterlina británica
        "JPY": 110.35, # Yen japonés
        "CAD": 1.26,   # Dólar canadiense
        "AUD": 1.36,   # Dólar australiano
        "CHF": 0.92,   # Franco suizo
    }
    lista_monedas = [moneda for moneda in tasas_de_cambio]
    
    print(f"Tienes estas monedas para elegir: {lista_monedas} \n")
    
    try:
        moneda_origen = input("Elige cual será la moneda de origen, (ej: USD) : \n").upper()
        moneda_destino = input("Y cual es la moneda de destino? (ej: GBP): \n").upper()
        ask_user_quantity = float(input("¿Cual es la cantidad a convertir?: \n"))
        
        return moneda_origen,moneda_destino,ask_user_quantity, tasas_de_cambio
    except ValueError:
        print("Por favor introduce solo numeros")
        

def conversion(moneda_origen, moneda_destino, ask_user_quantity, tasas_de_cambio):
    """
    1.- Pasamos los parametros las elecciones del usuario, junto con la lista de las monedas
    2.- Creamos diferentes condiciones , por si la moneda elegida de destino y origen es la misma, avisara al user
    3.- Si es correcto, comprobara si existe la moneda introducida por el user dentro del diccionario de monedas
    4.- Si esta correcto, creara la operacion correspondiente para el cambio de moneda
    5.- Si la moneda introducida no es la misma que hay en el diccionario , dara aviso de error
    """
    if moneda_origen == moneda_destino:
        print("Creo que quieres cambiar la misma moneda! \n")  
    elif moneda_origen in tasas_de_cambio and moneda_destino in tasas_de_cambio:
        cantidad_convertida = ask_user_quantity * (tasas_de_cambio[moneda_origen] / tasas_de_cambio[moneda_destino])
        
        print(f"Tu conversion de {moneda_origen} a {moneda_destino} son: {cantidad_convertida:.2f} {moneda_destino} \n")
    else:
        print("Un error ha ocurrido, esa moneda no se encuentra \n")
        
    
def main():
    os.system("cls")
    print("----> Soy tu conversor de monedas <---- \n"
          "Elige que tipo de conversion de moneda a moneda quieres escoger, introduce la cantidad y te lo convertiré \n")
    
    """
    Creamos un bucle WHILE infinito en TRUE en el que si el user acaba la conversion, puede decidir si hacer otra de nuevo
    De no ser asi, el bucle pasara a FALSE y parará
    Manejamos errores (Puede mejorarse)
    """
    while True:
        try:
            moneda_origen, moneda_destino, cantidad, tasas_de_cambio = choosen_user()
            conversion(moneda_origen, moneda_destino, cantidad, tasas_de_cambio)
            continuar = input("¿Quieres hacer otra conversión? (S/N): \n").lower()
            if continuar != 's':
                print("Nos vemos!")
                break
            os.system("cls")
        except TypeError:
            print("Se ha roto \n")
        
    
if __name__ == "__main__":
    main()
    
    
