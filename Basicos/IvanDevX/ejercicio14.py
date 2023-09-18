"""
14. **Conversor de Moneda** : Escribe un programa que convierta una cantidad de dinero en una moneda a otra. 
El usuario debe ingresar la cantidad, la moneda de origen y la moneda de destino, y el programa debe proporcionar la conversión.
"""

def conversiones(tasas_de_cambio, moneda_origen, moneda_destino, cantidad):
    try:
        tasa_origen_usd = tasas_de_cambio[moneda_origen]
        tasa_destino_usd = tasas_de_cambio[moneda_destino]
    except KeyError:
        print("Moneda no válida.")
        return

    cantidad_en_usd = cantidad / tasa_origen_usd
    cantidad_convertida = cantidad_en_usd * tasa_destino_usd

    print(f"Tus {cantidad} {moneda_origen} son al cambio {cantidad_convertida:.2f} {moneda_destino}")

    if input("Salir o continuar? [S]para salir ").lower() == "s":
        exit()  
    


def ask_user():
    """
    1-Se crea un diccionario con las monedas mas usadas y su cambio
    2- Se hace una variable para acceder a las monedas y mostrarlas para que el usuario sepa las disponibles
    3- En un bucle se pregunta al usuario su moneda, la moneda de origen y la cantidad
    4- Si la informacion introducida por el usuario concuerda con el diccionario le pregunta si la informacion es correcta
    5- Al ser correcta va a la funcion conversion para devolver la conversion

    """
    
    tasas_de_cambio = {
        'USD': 1.0,      # Dólar estadounidense
        'EUR': 0.94,     # Euro
        'GBP': 0.81,     # Libra esterlina
        'JPY': 147.62,   # Yen japonés
        'CAD': 1.35,     # Dólar canadiense
        'AUD': 1.55,     # Dólar australiano
        'CHF': 0.90,     # Franco suizo
        'CNY': 7.29,     # Yuan chino
        'INR': 83.21,    # Rupia india
        'RUB': 96.35,    # Rublo ruso
        'BRL': 4.85,     # Real brasileño   
    }
    
    lista_monedas = [moneda for moneda in tasas_de_cambio]
     
    while True:
        print(f"Las monedas que tenemos disponibles son : {lista_monedas}")
        input_moneda_origen = input("Ingrese la moneda de origen (por ejemplo, EUR): ").upper()
        input_moneda_destino = input("Ingrese la moneda de destino (por ejemplo, USD): ").upper()
        input_moneda_cantidad = float(input("Que cantidad quieres convertir? EJ : 19.95 => : "))
        
        if input_moneda_origen == input_moneda_destino:
            print(f"Pues nose... sera lo mismo ?")
        
        elif input_moneda_origen in tasas_de_cambio and input_moneda_destino in tasas_de_cambio:
        
            print(f"Tienes tus {input_moneda_cantidad} {input_moneda_origen} y los quieres convertir a {input_moneda_destino}")
        
            if input("La informacion es correcta? [Y/N] : ").lower() =="y":
                
                conversiones(tasas_de_cambio, input_moneda_origen, input_moneda_destino, input_moneda_cantidad)
                
        else:
            print("Revisa la informacion porfavor")


def main():
    # Funcion principal
    print("Conversor de monedas")
    ask_user()


if __name__ == "__main__":
    main()