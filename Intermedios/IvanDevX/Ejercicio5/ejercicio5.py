"""
5. **Calculadora con Interfaz Gráfica** : Desarrolla una calculadora con una interfaz gráfica de usuario (GUI)
utilizando una biblioteca como Tkinter (o la que tu quieras). 
La calculadora debe permitir realizar operaciones aritméticas básicas y mostrar el resultado en la ventana.
"""

from tkinter import *


def crear_interfaz_calculadora():
    
    root = Tk()
    root.title("Calculadora Basica")
    # root.iconbitmap("calculadora.ico")
    root.resizable(0,0) #No deja cambiar el tamaño de ventana (0=x, 0=y)
    root.geometry("370x350")

    # Pantalla Input1
    pantalla = Entry(root, width=30 , bg="black", fg="white", borderwidth=5, font=("arial", 15, "bold")).grid(row=0, padx=5, pady=5, columnspan=5)

    # Botones numericos
    boton1 = Button(root, text="1", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
    boton2 = Button(root, text="2", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
    boton3 = Button(root, text="3", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
    boton4 = Button(root, text="4", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
    boton5 = Button(root, text="5", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
    boton6 = Button(root, text="6", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
    boton7 = Button(root, text="7", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
    boton8 = Button(root, text="8", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
    boton9 = Button(root, text="9", width=6, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
    boton0 = Button(root, text="0", width=13, height=2, bg="grey", fg="blue", font=("arial", 12, "bold"), cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    # Boton igual, punto, borrar ultimo y borrar todo
    boton_punto = Button(root, text=".", width=6, height=2, bg="grey27", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=4, column=2, padx=1, pady=1)
    boton_igual = Button(root, text="=", width=13, height=2, bg="green", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=4, column=3, columnspan=2, padx=1, pady=1)
    boton_borrar_ultimo = Button(root, text="<=", width=6, height=2, bg="darkred", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
    boton_borrar_todo = Button(root, text="AC", width=6, height=2, bg="red", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=4, padx=1, pady=1)

    # Botones Operaciones
    boton_sumar = Button(root, text="+", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
    boton_restar = Button(root, text="-", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=2, column=4, padx=1, pady=1)
    boton_dividir = Button(root, text="/", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
    boton_multiplicar = Button(root, text="*", width=6, height=2, bg="orange", fg="white", font=("arial", 13, "bold"), cursor="hand2").grid(row=3, column=4, padx=1, pady=1)

    root.mainloop()


def main():
    crear_interfaz_calculadora()


if __name__ == "__main__":
    main()