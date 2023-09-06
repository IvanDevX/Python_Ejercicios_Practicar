"""
2. **Calculadora Simple**: Escribe un programa que realice una operación matemática simple (suma, resta, multiplicación o división) con dos números ingresados por el usuario.
"""
import os


def choose_user():
    
    while True:
        
        try:
            pregunta_user = input("Ingresa dos números separados por coma: ")

            # Divide la entrada del usuario en dos números separados
            number_separated = pregunta_user.split(",")
            
            numeros_limpios = [int(number_separated[0]), int(number_separated[1])]
            
            pregunta_calculo = input("Que operacion deseas realizar?: \n"
                                    "[S]uma \n"
                                    "[R]esta \n"
                                    "[M]ultiplicacion \n"
                                    "[D]ivision \n").lower()
            os.system("cls")  
            if pregunta_calculo == "s":
                print("Tu operacion elegida es la suma")
                return print(f"La suma entre {numeros_limpios[0]} + {numeros_limpios[1]} es: {numeros_limpios[0] + numeros_limpios[1]}")
            elif pregunta_calculo == "r":
                print("Tu operacion elegida es la resta")
                return print(f"La resta entre {numeros_limpios[0]} - {numeros_limpios[1]} es: {numeros_limpios[0] - numeros_limpios[1]}") 
            elif pregunta_calculo == "m":
                print("Tu operacion elegida es la multiplicacion")
                return print(f"La multiplicacion entre {numeros_limpios[0]} x {numeros_limpios[1]} es: {numeros_limpios[0] * numeros_limpios[1]}")
            elif pregunta_calculo == "d":
                print("Tu operacion elegida es la division")
                if numeros_limpios[0] == 0 or numeros_limpios[1] == 0:
                    return print("No puedes dividir entre 0")
                else:
                    return print(f"La division entre {numeros_limpios[0]} / {numeros_limpios[1]} es: {numeros_limpios[0] / numeros_limpios[1]:.2f}")
            else:
                print("Por favor, elige una de las opciones")
                
        except IndexError:
            print("Por favor, necesito dos numeros")
        except ValueError:
            print("Por favor, deben ser numeros")

            
def main():
    print("---> Bienvenido a tu calculadora, ingresa dos números y elige que tipo de operacion que quieres hacer <--- \n")
    choose_user()
    while True:
        otra_operacion = input("¿Deseas realizar otra operación? [S]i o [N]o: ").lower()
        os.system("cls")
        if otra_operacion == "s":
            choose_user()
        else:
            print("Nos vemos!")
            break
os.system("cls")
   
if __name__ == "__main__":
    main()