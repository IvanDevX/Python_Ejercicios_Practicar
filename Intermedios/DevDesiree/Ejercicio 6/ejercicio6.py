"""
6. **Generador de Tarjetas de Visita** : Desarrolla un programa que permita a los usuarios ingresar información personal, 
                                            como nombre, cargo y detalles de contacto,
                                            y luego genere tarjetas de visita en formato PDF que puedan imprimirse.
"""

import tkinter as tk
from tkinter import ttk
from reportlab.lib.pagesizes import landscape, A8 
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
from tkinter import filedialog
import os

# Configuracion de la ventana principal
root = tk.Tk()
root.title("Generador de Tarjetas de Visita")
root.geometry("400x400")
root.config(bg="gray85")


def buscar_imagen():
    """
    1.- Declaramos 3 variables globales
    2.- Creamos una variable con las dimensiones del avatar que se mostrara en la ventana
    3.- Creamos la variable "file_path", donde se guardara el nombre del archivo que hemos seleccionado, y solo mostramos imagenes, con el tipo de archivo especificado
    4.- Declaramos la variable "avatar" para abrir y guardar la imagen, y luego la redimensionamos, luego la transformamos con el PhotoImage
    5.- Verificamos si "file_path" no está vacio (si el usuario selecciono un archivo), antes de intentar abrir la imagen, para evitar errores
    6.- Luego mostramos la imagen y la ruta en la interfaz grafica
    """
    global avatar_tk
    global avatar
    global file_path
    
    redimension_image = (100, 100)
    
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de Imagen", "*.png *.jpg *.jpeg")])
    
    if file_path:
        avatar = Image.open(file_path)
        avatar = avatar.resize(redimension_image, Image.LANCZOS)
        avatar_tk = ImageTk.PhotoImage(avatar)
        
        
        label_2 = ttk.Label(root, image=avatar_tk)
        label_2.pack()
        
        avatar_label = ttk.Label(root, text=file_path)
        avatar_label.pack()
    

# Funcion para crear el PDF con los datos ingresados
def create_pdf():
    # Obtiene los datos ingresados por el usuario
    nombre = nombre_entry.get()
    cargo = cargo_entry.get()
    contacto = contacto_entry.get()
    
    # Guardamos las dimensiones de altura y anchura del modulo A8 que importamos
    w,h = A8
    
    # Define el nombre del archivo PDF
    nombre_archivo = 'tarjeta_visita.pdf'

    # Crea el PDF
    c = canvas.Canvas(nombre_archivo, pagesize=landscape(A8))

    # Dibuja un rectangulo como marco de la tarjeta
    c.rect(10, 10, h-20, w-20)
    
    # Configuramos la fuente y el tamaño de la fuente
    c.setFont("Times-Roman", 9)
    
    """
    Manejamos errores:
    En este caso si no hay un avatar seleccionado nos dejara crear la tarjeta de visita sin imagen
    Ya que sin try/except no nos dejaba crear la tarjeta de visita sin imagen y el programa partía mostrando el error: NameError
    """
    try:
        if avatar_tk is not None:
            """
            1.- Creamos una condicion en el caso de que la imagen de avatar no este vacia
            2.- Volvemos a crear la imagen, redimensionarla, y la guardamos con un nombre especifico para crear una copia
            3.- Luego la dibujamos en el pdf en unas coordenadas y con una dimension especificada
            4.- A continuacion, borraremos la copia "avatar.png" que se creo anteriormente en nuestro equipo
            """
            avatar_img = Image.open(file_path)
            avatar_img = avatar_img.resize((60, 60), Image.LANCZOS)
            avatar_img_path = "avatar.png"
            avatar_img.save(avatar_img_path)
            c.drawImage(avatar_img_path, h-55, w-55, width=40, height=40)
            
            os.remove(avatar_img_path)
    except NameError:
        pass  
    
    # Agrega el contenido del texto
    contenido = [
        f"Nombre: {nombre}",
        f"Cargo: {cargo}",
        f"Contacto: {contacto}", 
    ]
    
    # Recorremos cada linea del contenido (nombre,cargo,contacto..) para posteriormente dibujar cada linea debajo de la otra
    y = 70
    for linea in contenido:
        c.drawString(15, y, linea)
        y -= 20  # Mueve la posicion hacia arriba para la siguiente linea
        
    # Guardamos el documento
    c.save()

    # Muestra un mensaje de confirmacion
    result_label.config(text="Tarjeta de visita generada correctamente.")


# Se crean las etiquetas y campos de entrada para los datos
nombre_label = ttk.Label(root, text="Nombre:")
nombre_label.pack()
nombre_entry = ttk.Entry(root)
nombre_entry.pack()

cargo_label = ttk.Label(root, text="Cargo:")
cargo_label.pack()
cargo_entry = ttk.Entry(root)
cargo_entry.pack()

contacto_label = ttk.Label(root, text="Email:")
contacto_label.pack()
contacto_entry = ttk.Entry(root)
contacto_entry.pack()

avatar_label = ttk.Label(root, text="Avatar:")
avatar_label.pack()

btn_buscar = ttk.Button(root, text= "Buscar Imagen", command=buscar_imagen)
btn_buscar.pack()

# Boton para generar el PDF
generate_button = ttk.Button(root, text="Generar Tarjeta de Visita", command=create_pdf)
generate_button.pack()

# Etiqueta para mostrar el resultado
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
