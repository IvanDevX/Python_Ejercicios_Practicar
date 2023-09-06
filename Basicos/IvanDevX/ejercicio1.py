"""
**Suma de dos números**: Escribe un programa en Python que solicite al usuario que ingrese dos números 
y luego muestre la suma de esos dos números en pantalla..
"""
def conversion_datos():
    # Bucle que maneja errores si el usuario no introduce lo que se pide
    # el metodo isdigit() verifica si una cadena consiste en caracteres numéricos.
    while True:
        try:
            input_usuario = input("Recuerda separados por , | EJ: 2, 18 ==> : ")
            input_limpio = input_usuario.split(",")
            if len(input_limpio) !=2 or not input_limpio[0].isdigit() or not input_limpio[1].isdigit():
                print("Solo 2 numeros! Separados por ,")
            else:
                suma_numeros(input_limpio)
                break
        except ValueError:
            print("--Error--")
        

def suma_numeros(input_limpio):
    # Suma de los numeros introducidos por el usuario
    print("Procedemos a sumar los 2 numeros.")
    result = int(input_limpio[0]) + int(input_limpio[1])
    print(f"La suma de {input_limpio[0]} y {input_limpio[1]} es: {result}")
    

def main():
    # Funcion princial del programa
    print(" ====> Vamos a sumar 2 numeros! <====")
    print("Podrias darme 2 numeros separados por coma(,)?")
    conversion_datos()
        

if __name__ == "__main__":
    main()