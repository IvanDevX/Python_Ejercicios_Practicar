"""
**Suma de dos números**: Escribe un programa en Python que solicite al usuario que ingrese dos números 
y luego muestre la suma de esos dos números en pantalla..
"""
#Funcion para crear la suma , pasandole el parametro de la variable del input usuario
def suma(input_numbers):
    resultado = input_numbers[0] + input_numbers[1]
    print(f"La suma total de: {input_numbers[0]} y {input_numbers[1]} es {resultado}")

#Funcion para preguntarle al usuario que introduzca dos numeros
def ask_user():
    #Creamos un bucle comentando al usuario lo que debe introducir, si se introduce algo diferente a lo solicitado, se manejan los errores
    while True:
        pregunta_user = input("Que numeros eliges? Recuerda, dos numeros separados por comas: ")
        
        number_separated = pregunta_user.split(",")
        try:
            new_numbers_separated = [int(number) for number in number_separated]
            if len(new_numbers_separated) != 2:
                print("Debes ingresar dos números porfavor")
            else: 
                return suma(new_numbers_separated)
            
        except ValueError:
            print("Por favor solo numeros y separados por coma.")
        
        
def main():
    print("Dime dos numeros aleatorios para sumarlos entre sí \n")
    print("Deben estar separados por comas: Ej: 45 , 90 \n")
    
    ask_user()
    
    

if __name__ == "__main__":
    main()