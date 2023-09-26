"""
5. **Calculadora con Interfaz Gráfica** : Desarrolla una calculadora con una interfaz gráfica de usuario (GUI) utilizando una biblioteca como Tkinter (o la que tu quieras). 
        La calculadora debe permitir realizar operaciones aritméticas básicas y mostrar el resultado en la ventana.
"""

from tkinter import *

root = Tk()
root.title("Calculadora")
# root.iconbitmap("ico_calculator.ico")
root.resizable(0,0) # Evita que se pueda redimensionar el tamaño de la pantalla
root.geometry("290x390")

pantalla_calculadora = Entry(root, width=25, bg="grey", fg="white", borderwidth=5, font=("arial", 15, "bold")).grid(row=0, padx=2, pady=2, columnspan=4)

# Botones numericos
boton_1 = Button(root, text="1", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_0 = Button(root, text="0", width=6, height=3, bg="white", fg="red", font=("arial", 12, "bold"), cursor="hand2").grid(row=4, column=1, padx=1, pady=1)


# Botones simbolos
boton_igual = Button(root, text="=", width=12, height=2, bg="green", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=5, column=2, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=6, height=3, bg="grey", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=4, column=0, padx=1, pady=1)

# Botones operaciones
boton_sumar = Button(root, text="+", width=6, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_restar = Button(root, text="-", width=6, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_multiplicar = Button(root, text="x", width=6, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=4, column=3, padx=1, pady=1)
boton_dividir = Button(root, text="/", width=6, height=3, bg="orange", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=4, column=2, padx=1, pady=1)

# Botones funcionales
boton_limpiar = Button(root, text="Clear", width=12, height=2, bg="red", fg="white", font=("arial", 12, "bold"), cursor="hand2").grid(row=5,columnspan=2, padx=1, pady=1)


def main():

    root.mainloop()


if __name__ == "__main__":
    main()