"""
5. **Calculadora con Interfaz Gráfica** : Desarrolla una calculadora con una interfaz gráfica de usuario (GUI) utilizando una biblioteca como Tkinter (o la que tu quieras). 
        La calculadora debe permitir realizar operaciones aritméticas básicas y mostrar el resultado en la ventana.
"""

from tkinter import *



root = Tk()
root.title("Calculadora Básica")
# root.iconbitmap("ico_calculator.ico")
root.resizable(0,0) # Evita que se pueda redimensionar el tamaño de la pantalla
root.geometry("340x390")

pantalla_calculadora = Entry(root, width=25, bg="grey", fg="white", borderwidth=5, font=("arial", 18, "bold"))
pantalla_calculadora.grid(row=0, padx=1, pady=1, columnspan=4)


def enviar_boton(valor):
    """
    1.- Obtenemos el valor de la pantalla y la borramos
    2.- Añadimos el resultado del numero anterior con el nuevo
    """
    numero_anterior = pantalla_calculadora.get()
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(0,str(numero_anterior) + str(valor))
    

def igual():
    """
    1.- Creamos la variable num2 Global
    2.- Con esa misma variable guardamos lo que hay en pantalla y luego borramos la pantalla
    3.- Creamos unas condiciones dependiendo del simbolo que recoja la pantalla y haremos la operacion pertinente
    4.- Manejamos errores en el caso que haya algun fallo mostraremos un Error en la pantalla de la calculadora
    """
    try:
        global num2
        num2 = pantalla_calculadora.get()
        pantalla_calculadora.delete(0, END)
        if operacion == "+":
            pantalla_calculadora.insert(0, num1 + float(num2))
        if operacion == "-":
            pantalla_calculadora.insert(0, num1 - float(num2))
        if operacion == "*":
            pantalla_calculadora.insert(0, num1 * float(num2))
        if operacion == "/":
            pantalla_calculadora.insert(0, num1 / float(num2))
    except NameError:
        pantalla_calculadora.insert(0, "Error")


def suma():
    """
    1.- Declaramos la variables globales num1 y operacion
    2.- En la variable num1 guardamos lo que hay en la pantalla
    3.- Convertimos el numero que se ha guardado a Float y borramos la pantalla
    4.- Guardamos el simbolo + en la variable operacion
    """
    global num1
    global operacion
    num1 = pantalla_calculadora.get()
    num1 = float(num1)
    pantalla_calculadora.delete(0, END)
    operacion = "+"
    
def resta():  
    """
    1.- Declaramos la variables globales num1 y operacion
    2.- En la variable num1 guardamos lo que hay en la pantalla
    3.- Convertimos el numero que se ha guardado a Float y borramos la pantalla
    4.- Guardamos el simbolo - en la variable operacion
    """
    global num1
    global operacion
    num1 = pantalla_calculadora.get()
    num1 = float(num1)
    pantalla_calculadora.delete(0, END)
    operacion = "-"


def multiplicar():
    """
    1.- Declaramos la variables globales num1 y operacion
    2.- En la variable num1 guardamos lo que hay en la pantalla
    3.- Convertimos el numero que se ha guardado a Float y borramos la pantalla
    4.- Guardamos el simbolo * en la variable operacion
    """
    global num1
    global operacion
    num1 = pantalla_calculadora.get()
    num1 = float(num1)
    pantalla_calculadora.delete(0, END)
    operacion = "*"


def dividir():
    """
    1.- Declaramos la variables globales num1 y operacion
    2.- En la variable num1 guardamos lo que hay en la pantalla
    3.- Convertimos el numero que se ha guardado a Float y borramos la pantalla
    4.- Guardamos el simbolo / en la variable operacion
    """
    global num1
    global operacion
    num1 = pantalla_calculadora.get()
    num1 = float(num1)
    pantalla_calculadora.delete(0, END)
    operacion = "/"
    
    
def limpiar_pantalla():
    # Esta funcion limpia la pantalla
    pantalla_calculadora.delete(0, END)
    
    
def limpiar_ultimo_numero():
    # Esta funcion limpia el ultimo numero escrito en la pantalla
    estado_pantalla = pantalla_calculadora.get()
    
    if len(estado_pantalla):
        pantalla_nuevo_estado = estado_pantalla[:-1]
        limpiar_pantalla()
        pantalla_calculadora.insert(0, pantalla_nuevo_estado)
    else:
        limpiar_pantalla()
        pantalla_calculadora.insert(0, "Error")

# Botones numericos
boton_1 = Button(root, text="1", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(9)).grid(row=3, column=2, padx=1, pady=1)
boton_0 = Button(root, text="0", width=7, height=3, bg="gray27", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda: enviar_boton(0)).grid(row=4, column=1, padx=1, pady=1)

# Botones simbolos
boton_igual = Button(root, text="=", width=15, height=2, bg="green", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=igual).grid(row=5, column=2, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=7, height=3, bg="grey", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=lambda:enviar_boton(".")).grid(row=4, column=0, padx=1, pady=1)

# Botones operaciones
boton_sumar = Button(root, text="+", width=7, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=suma).grid(row=2, column=3, padx=1, pady=1)
boton_restar = Button(root, text="-", width=7, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=resta).grid(row=3, column=3, padx=1, pady=1)
boton_multiplicar = Button(root, text="x", width=7, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=multiplicar).grid(row=4, column=3, padx=1, pady=1)
boton_dividir = Button(root, text="/", width=7, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=dividir).grid(row=4, column=2, padx=1, pady=1)

# Botones funcionales
boton_limpiar = Button(root, text="Clear", width=15, height=2, bg="red", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=limpiar_pantalla).grid(row=5,columnspan=2, padx=1, pady=1)
boton_borrar_ultimo_numero = Button(root, text="←", width=7, height=3, bg="red", fg="white", font=("arial", 12, "bold"), cursor="hand2", command=limpiar_ultimo_numero).grid(row=1,column=3, padx=1, pady=1)


root.mainloop()

