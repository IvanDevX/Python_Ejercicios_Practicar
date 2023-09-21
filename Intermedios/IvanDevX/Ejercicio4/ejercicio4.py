"""
4. **Juego de Piedra, Papel o Tijera** : Implementa el clásico juego de piedra, papel o tijera en Python. 
Permite que el usuario juegue contra la computadora y lleva un registro de las victorias y derrotas.
"""
import os
import random


def resultado(user, machine):
    """
    1- Se compara el valor de user y el valor de machine y se dice si gana o no
    2- En este caso se comparan las 3 formas posibles de que un usuario pueda ganar y si no es derrota.
    3- Se retorna el valor para luego usarlo.
    """
    if user == machine:
        ganador = "empate"
        
    elif (user == "piedra" and machine == "tijera") or \
        (user == "papel" and machine == "piedra") or  \
        (user == "tijera" and machine == "papel"):
        ganador = "user"
        
    else: 
        ganador = "machine"
        
    return ganador


def resumen_final(partidas, victorias_user, derrotas_user, victorias_machine, derrotas_machine, puntuacion_user, puntuacion_machine):
    """
    Recogemos las variables y las usamos para mostrar un mensaje final con todas las estadisticas
    
    """
    os.system("cls")
    print("Aqui te muestro el resumen")
    print(f"Se han jugado {partidas} partidas")
    print(f"El usuario ha ganado {victorias_user} veces y ha perdido {derrotas_user} veces")
    print(f"La maquina ha ganado {victorias_machine} veces y ha perdido {derrotas_machine} veces")
    print(f"Las puntuaciones han sido : {puntuacion_user} Puntos user y {puntuacion_machine} Puntos maquina")
    
    if puntuacion_user == puntuacion_machine:
        print("Habeis quedado igual de puntacion")
    elif puntuacion_user > puntuacion_machine:
        print("El usuario ha ganado")
    elif puntuacion_user < puntuacion_machine:
        print("Maquina ha ganado!")
        
    print("Gracias por jugar!")   


def turn_user():
    """
    Preguntamos al usuarios que elige y si no es ninguna de las opciones posibles le volvemos a preguntar.
    """
    print("Es tu turno, que eliges?")
    while True:
        user_choice = input(("Que eliges?")).lower()
        
        if user_choice == "piedra" or user_choice == "pi":
            return "piedra"
            
        elif user_choice == "papel" or user_choice == "pa":
            return "papel"
            
        elif user_choice == "tijera" or user_choice == "ti":
            return "tijera"
            
        else:
            print("No es correcto, intentalo de nuevo.")
              

def turn_machine(opciones):
    """
    Turno de la maquina, se pasan las opciones y elige 1.
    """
    machine = random.choice(opciones)
    return machine
    

def juego():
    """
    1- Inicio de juego dando las normas
    2- Se declaran las variables
    3- Con un bucle While se pregunta al usuario y a la maquina y dice quien gana esa ronda.
    4- Al final te da opcion a continuar otra partida o salir
    5- Cuando sales lanza una funcion con el resumen de la partida.    
    """
    print("Las normas son simples.")
    print("Puedes poner Piedra, o pi , Papel o pa, tijera o ti")
    print("Habra contador de derrotas y Victorias")
    print("Suerte!")
    
    opciones = ["piedra", "papel", "tijera"]
    victorias_user = 0 
    derrotas_user = 0
    victorias_machine = 0
    derrotas_machine = 0
    puntuacion_user = 0
    puntuacion_machine = 0
    partidas = 0
    
    while True:
        
        user_choice = turn_user()
        machine_choice = turn_machine(opciones)
        
        print(f"Usuario ha elegido : {user_choice.capitalize()} y maquina ha elegido : {machine_choice.capitalize()}")
        
        resultados = resultado(user_choice, machine_choice)
        partidas += 1
        
        
        if resultados == "user":
            print("Gana User")
            victorias_user += 1
            derrotas_machine += 1
            puntuacion_user += 1
        elif resultados == "machine":
            print("Gana Maquina")
            victorias_machine += 1
            derrotas_user += 1
            puntuacion_machine += 1
        elif resultados == "empate":
            print("Empate!!")
            pass
        
        if input("Otra partida? [S]i o [N]o").lower() == "n":
            print("Fin del juego")
            break
        
        os.system("cls")
        
    resumen_final(partidas, victorias_user, derrotas_user, victorias_machine, derrotas_machine, puntuacion_user, puntuacion_machine)    
  
    
def titulo(text):
    # Funcion que le pasas un texto y te pone * tanto arriba como abajo de la longitud de dicho texto
    print("*" * len(text)) , print(text) , print("*" * len(text))
    

def main():
    # Funcion principal
    os.system("cls")
    titulo("Piedra , papel, tijera")
    juego()
    

if __name__ == "__main__":
    main()