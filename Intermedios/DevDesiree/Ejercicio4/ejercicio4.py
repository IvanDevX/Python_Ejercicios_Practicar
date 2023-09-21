"""
4. **Juego de Piedra, Papel o Tijera** : Implementa el clásico juego de piedra, papel o tijera en Python. 
        Permite que el usuario juegue contra la computadora y lleva un registro de las victorias y derrotas.
"""
import random
import os


def choose_machine():
    """
    1.- Creamos una lista con opciones
    2.- Guardamos en una variable (choose_machine) la eleccion aleatoria que escoge la maquina
    3.- Retornamos la variable choose_machine
    """
    options = ["Piedra", "Papel", "Tijera"]
    
    choose_machine = random.choice(options)

    print(f"Maquina ha elegido: {choose_machine} \n")

    return choose_machine


def choose_user():
    """
    1.- Creamos un bucle WHILE true con la pregunta al usuario de que opcion desea elegir
    2.- Dependiendo de que opcion elija el usuario, se retornara una palabra concreta: EJ: Papel. 
        Si no se elige opcion valida, se volvera a preguntar al usuario
    """
    while True:
        ask_user = input("Tienes que elegir entre Piedra, Papel, Tijera, a ver quien gana \n"
                        "Que eliges?: \n"
                        "[P]iedra \n"
                        "P[a]pel \n"
                        "[T]ijera \n").lower()
        os.system("cls")
        if ask_user == "p":
            print("Has elegido Piedra \n")
            return "Piedra"
        elif ask_user == "a":
            print("Has elegido Papel \n")
            return "Papel"
        elif ask_user == "t":
            print("Has elegido Tijera \n")
            return "Tijera"
        else:
            print("Elije una de las opciones! \n")
            
        
def game():
    """
    1.- Se crean 4 variables que son contadores de victorias y derrotas del usuario y la maquina
    2.- Creamos un bucle WHILE True que llamara a las funciones choose_user y choose_machine y se guardan en variables para poder ser llamadas a continuacion
    3.- Se comparan las variables de las respuestas del user y maquina y se mostrara quien gana o pierde dependiendo de la eleccion de cada uno
    4.- Ademas del resultado sumara +1 al contador de victoria o derrota dependiendo quien gane y se mostrara al final de cada juego
    5.- Se vuelve a preguntar al usuario si quiere volver a jugar, si es afirmativo empieza de nuevo el bucle
    """
    counts_win_user = 0
    counts_win_machine = 0
    counts_lose_user = 0
    counts_lose_machine = 0
    
    while True:
        print("Turno de User: \n")
        user_choice = choose_user()
        
        print("Turno de Maquina: \n")
        machine_choice = choose_machine()
        
        if user_choice == machine_choice:
            print("Habeis empatado!! \n")
            
        elif (user_choice == "Piedra" and machine_choice == "Tijera") or \
            (user_choice == "Papel" and machine_choice == "Piedra") or \
            (user_choice == "Tijera" and machine_choice == "Papel"):
            
            print("El usuario a ganado! Felicidades! \n")
            
            counts_win_user += 1
            counts_lose_machine += 1
        else:
            print("La maquina a ganado!! Lo siento, has perdido! \n")
            
            counts_win_machine += 1
            counts_lose_user += 1
        
        print(f"Usuario lleva : {counts_win_user} victoria(s) y {counts_lose_user} derrota(s) \n"
            f"Maquina lleva : {counts_win_machine} victoria(s) y {counts_lose_machine} derrota(s) \n")
        

        another_game = input("Quieres volver a jugar? [S] / [N]: \n").lower()
        
        if another_game != "s":
            print("Nos vemos! Gracias por jugar! \n")
            break
    
        os.system("cls")      


def main():
    os.system("cls")
    print("============================================\n"
          "Bienvenidos al juego Piedra, Papel o Tijera \n"
          "============================================ \n")
    game()
    
    
if __name__ == "__main__":
    main()