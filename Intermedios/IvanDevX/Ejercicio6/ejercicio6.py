"""
6. **Generador de Tarjetas de Visita** : Desarrolla un programa que permita a los usuarios ingresar información personal,
    como nombre, cargo y detalles de contacto, y luego genere tarjetas de visita en formato PDF que puedan imprimirse.
"""

# pip install reportlab
# pip install Pillow

"""
Las librerias..

Tkinter: Para crear la interfaz gráfica de usuario (GUI).
filedialog: Para permitir al usuario seleccionar una imagen.
canvas de ReportLab: Para generar archivos PDF y agregar contenido a ellos.
landscape y A8 de ReportLab: Para definir el tamaño y la orientación de la página del PDF.
Image y ImageTk de Pillow: Para manipular imágenes y mostrarlas en la GUI.
"""
from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A8   # A8 = (52*mm,74*mm) - landscape = apaisado
from PIL import Image, ImageTk
import os #se importa os, para borrar el archivo temporal que se crea con la imagen

def cargar_imagen():
    """
    1-Esta función se llama cuando se hace clic en el botón "Cargar Imagen".
    2-Abre un cuadro de diálogo de selección de archivos para que el usuario elija una imagen.
    3-Redimensiona la imagen a 80x80 píxeles y la muestra en un widget Label (imagen_label) en la GUI de tkinter.
    4-Almacena la imagen en una variable global imagen_seleccionada para su uso posterior.
    """
    global imagen_seleccionada
    imagen_ruta = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg")])
    if imagen_ruta:
        imagen = Image.open(imagen_ruta)
        imagen = imagen.resize((80, 80), Image.BILINEAR)
        imagen_tk = ImageTk.PhotoImage(imagen)
        
        # Configura la imagen en el widget imagen_label
        imagen_label.config(image=imagen_tk)
        imagen_label.image = imagen_tk
        
        imagen_seleccionada = imagen  # Almacena la imagen en la variable global


def generar_tarjeta():
    """
    1-Esta función se llama cuando se hace clic en el botón "Generar Tarjeta".
    2-Obtiene los datos ingresados por el usuario: nombre, cargo, correo electrónico y teléfono.
    3-Define el tamaño de la página PDF como A8 en orientación apaisada y crea un archivo PDF con el nombre de la persona.
    4-Dibuja un cuadro y agrega texto en el PDF con la información ingresada por el usuario.
    5-Comprueba si hay una imagen seleccionada y la agrega al PDF, si no tambien lo crea sin imagen.
    6-Muestra un mensaje de éxito y borra la imagen temporal después de usarla.
    """
    # Coger los datos del los inputs
    nombre = nombre_input.get()
    cargo = cargo_input.get()
    email = email_input.get()
    telefono = telefono_input.get()
    
    w,h = A8 #w 147.40157480314963 y h 209.76377952755908
    
    # Crear un PDF para la tarjeta de visita con el nombre de la persona
    pdf_filename = f"{nombre}_tarjeta_visita.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=landscape(A8))

    # Dibujar el cuadrado centrado
    c.rect(10, 10, h-20, w-20)
    
    # Ajustamos el tamaño de letra
    c.setFont("Helvetica", 8)
    
    # Pintamos el texto ... 0,0 es Abajo izquierda y 0,10 es subiendo altura del texto y por cada linea pintamos una linea fina
    c.setStrokeColorRGB(0.5, 0.5, 0.5) #Para el color de la linea
    c.setLineWidth(0.5) #Grosor lineas
    c.drawString(15, 80, f"Nombre : {nombre}")
    c.line(15 , 75 , 150 , 75)
    
    c.drawString(15, 60, f"Cargo : {cargo}")
    c.line(15 , 55 , 150 , 55)
    
    c.drawString(15, 40, f"Email : {email}")
    c.line(15 , 35 , 150 , 35)
    
    c.drawString(15, 20, f"Telefono : {telefono}")
    c.line(15 , 15 , 150 , 15)
    
    # Comprueba si hay una imagen seleccionada
    try:
        if imagen_seleccionada:
            imagen_path = "temp_imagen.png"
            imagen_seleccionada.save(imagen_path)  # Guarda la imagen temporalmente como un archivo PNG
            c.drawImage(imagen_path, h-55, w-55, width=40, height=40)
            
            # Elimina la imagen temporal después de usarla
            os.remove(imagen_path)
    except NameError:
        pass
    
    c.save()
    
    # Mostrar un mensaje de éxito
    resultado_label.config(text=f"Tarjeta generada como '{pdf_filename}'")


# Diseño de GUI.
"""
Se crea la ventana principal (root) y se configura su título, tamaño y restricciones de redimensionamiento.
Se crean etiquetas y campos de entrada para ingresar el nombre, cargo, correo electrónico y teléfono.
Se crea un botón "Cargar Imagen" para cargar una imagen.
Se muestra una etiqueta de "Cargando imagen..." que se actualiza cuando se carga una imagen.
Se crea un botón "Generar Tarjeta" para generar la tarjeta de visita.
Se muestra una etiqueta resultado_label para mostrar el mensaje de éxito.
"""
root = Tk()
root.title("Generador de Tarjetas de Visita")
root.resizable(0,0) #No deja cambiar el tamaño de ventana (0=x, 0=y)
root.geometry("300x380")

# Inputs de entrada, como un formulario

# Nombre
nombre_label = Label(root, text="Nombre: *")
nombre_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
nombre_input = Entry(root)
nombre_input.grid(row=0, column=1, padx=10, pady=10)

# Cargo
cargo_label = Label(root, text="Cargo: *")
cargo_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
cargo_input = Entry(root)
cargo_input.grid(row=1, column=1, padx=10, pady=10)

# Email
email_label = Label(root, text="Correo Electrónico: *")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_input = Entry(root)
email_input.grid(row=2, column=1, padx=10, pady=10)

# Telefono
telefono_label = Label(root, text="Telefono: *")
telefono_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
telefono_input = Entry(root) 
telefono_input.grid(row=3, column=1, padx=10, pady=10)

# Botón para cargar una imagen
cargar_imagen_button = Button(root, text="Cargar Imagen", command=cargar_imagen)
cargar_imagen_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar la imagen
imagen_label = Label(root, text="Cargando imagen...", padx=10, pady=10)
imagen_label.grid(row=5, column=0, columnspan=2)

# Botón para generar la tarjeta de visita
generar_button = Button(root, text="Generar Tarjeta", command=generar_tarjeta , state="active")
generar_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = Label(root, text="")
resultado_label.grid(row=7, column=0, columnspan=2)

root.mainloop()