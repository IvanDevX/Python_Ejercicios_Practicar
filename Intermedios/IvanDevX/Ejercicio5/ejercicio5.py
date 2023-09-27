"""
5. **Calculadora con Interfaz Gráfica** : Desarrolla una calculadora con una interfaz gráfica de usuario (GUI)
utilizando una biblioteca como Tkinter (o la que tu quieras). 
La calculadora debe permitir realizar operaciones aritméticas básicas y mostrar el resultado en la ventana.
"""

from tkinter import *


def enviar_boton(valor):
    """
    1- Recogemos el valor de la pantalla y la borramos, luego añadimos a la pantalla el resultado anterior y el nuevo numero.
    """
    anterior = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, str(anterior) + str(valor))


def igual():
    """
    1-Recogemos valor de la pantalla y lo llevamos a la variable global num2
    2-Borramos pantalla 
    3-Condicionales depende de la operacion hace una operacion y otra
    4-Esta en un bloque try/except para manejar errores, por ejemplo si le das a la operacion antes de poner numeros.
    
    """
    try:
        global num2
        num2 = pantalla.get()
        pantalla.delete(0, END)
        if operacion == "+":
            pantalla.insert(0, num1 + float(num2))
        elif operacion == "-":
            pantalla.insert(0, num1 - float(num2))
        elif operacion == "/":
            pantalla.insert(0, num1 / float(num2))
        elif operacion == "*":
            pantalla.insert(0, num1 * float(num2))
    except NameError:
        pantalla.insert(0, "Error")
            
        
def suma():
    """
    Coge el numero en pantalla , borra la pantalla , lo transforma a float y a la variable operacion le da su signo
    """
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "+"
   
    
def resta():
    """
    Coge el numero en pantalla , borra la pantalla , lo transforma a float y a la variable operacion le da su signo
    """
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "-"


def division():
    """
    Coge el numero en pantalla , borra la pantalla , lo transforma a float y a la variable operacion le da su signo
    """
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "/"


def multiplicacion():
    """
    Coge el numero en pantalla , borra la pantalla , lo transforma a float y a la variable operacion le da su signo
    """
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "*"  
    
def borrartodo():
    """
    Borra toda la pantalla
    """
    pantalla.delete(0, END)
    
def borrar1():
    """
    Guarda lo que hay en pantalla, y verificando la longitud borra el ultimo caracter, borra pantalla y luego añade la variable con el nuevo estado
    """
    pantalla_estado = pantalla.get()
    if len(pantalla_estado):
        pantalla_nuevo_estado = pantalla_estado[:-1]
        borrartodo()
        pantalla.insert(0, pantalla_nuevo_estado)
    else:
        borrartodo()
        pantalla.insert(0, "Error")
    
    
"""
Iniciamos Tk
Le damos titulo y configuraciones
Asignamos la pantalla y los botones con grid o malla en posicionamiento
A cada boton le damos la funcion que le corresponda.

"""
root = Tk()
root.title("Calculadora Basica")
# root.iconbitmap("calculadora.ico")
root.resizable(0,0) #No deja cambiar el tamaño de ventana (0=x, 0=y)
root.geometry("360x280")

# Pantalla Input1
pantalla = Entry(root, width=30 , bg="black", fg="white", borderwidth=5, font=("arial", 15, "bold"))
pantalla.grid(row=0, padx=5, pady=5, columnspan=5)

# Botones numericos
boton1 = Button(root, text="1", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2", 
                command=lambda : enviar_boton(1)).grid(row=1, column=0, padx=1, pady=1)
boton2 = Button(root, text="2", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(2)).grid(row=1, column=1, padx=1, pady=1)
boton3 = Button(root, text="3", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(3)).grid(row=1, column=2, padx=1, pady=1)
boton4 = Button(root, text="4", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(4)).grid(row=2, column=0, padx=1, pady=1)
boton5 = Button(root, text="5", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(5)).grid(row=2, column=1, padx=1, pady=1)
boton6 = Button(root, text="6", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(6)).grid(row=2, column=2, padx=1, pady=1)
boton7 = Button(root, text="7", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(7)).grid(row=3, column=0, padx=1, pady=1)
boton8 = Button(root, text="8", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(8)).grid(row=3, column=1, padx=1, pady=1)
boton9 = Button(root, text="9", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(9)).grid(row=3, column=2, padx=1, pady=1)
boton0 = Button(root, text="0", width=13, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2",
                command=lambda : enviar_boton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# Boton igual, punto, borrar ultimo y borrar todo
boton_punto = Button(root, text=".", width=6, height=2, bg="grey27", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                     command=lambda : enviar_boton(".")).grid(row=4, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=13, height=2, bg="green", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                     command=igual).grid(row=4, column=3, columnspan=2, padx=1, pady=1)
boton_borrar_ultimo = Button(root, text="<=", width=6, height=2, bg="darkred", fg="white", font=("arial", 12, "bold"), cursor="hand2",
                             command=borrar1).grid(row=1, column=3, padx=1, pady=1)
boton_borrar_todo = Button(root, text="AC", width=6, height=2, bg="red", fg="white", font=("arial", 12, "bold"), cursor="hand2",
                           command=borrartodo).grid(row=1, column=4, padx=1, pady=1)

# Botones Operaciones
boton_sumar = Button(root, text="+", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                     command=suma).grid(row=2, column=3, padx=1, pady=1)
boton_restar = Button(root, text="-", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                      command=resta).grid(row=2, column=4, padx=1, pady=1)
boton_dividir = Button(root, text="/", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                       command=division).grid(row=3, column=3, padx=1, pady=1)
boton_multiplicar = Button(root, text="*", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2",
                           command=multiplicacion).grid(row=3, column=4, padx=1, pady=1)

root.mainloop()
