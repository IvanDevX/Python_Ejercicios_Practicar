"""
6. **Generador de Tarjetas de Visita** : Desarrolla un programa que permita a los usuarios ingresar información personal,
    como nombre, cargo y detalles de contacto, y luego genere tarjetas de visita en formato PDF que puedan imprimirse.
"""

# ////////////
# *****ESTE EJERCICIO ES EL MISMO PERO AÑADIENDO MASK SOBRE IMAGEN Y DISABLED BOTON CUANDO NO HAY DATOS EN LOS INPUTS****


# pip install reportlab
# pip install Pillow

from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A8   # A8 = (52*mm,74*mm) - landscape = apaisado
from PIL import Image, ImageTk, ImageDraw
import tempfile


def actualizar_boton_generar():
    # Verificar si todos los campos de entrada tienen contenido
    if nombre_input.get() and cargo_input.get() and email_input.get() and telefono_input.get():
        generar_button.config(state="normal")  # Habilitar el botón
        resultado_label.config(text="Puedes Generar tu tarjeta.")
    else:
        generar_button.config(state="disabled")  # Deshabilitar el botón
        resultado_label.config(text=" Todos los campos son obligatorios.")


def cargar_imagen():
    global imagen, temp_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg")])
    if file_path:
        imagen_pillow = Image.open(file_path)
        imagen_pillow.thumbnail((100, 100))  # Redimensiona la imagen si es demasiado grande

        # Crear una mascara con las mismas dimensiones y modo de color que la imagen
        mask = Image.new('L', imagen_pillow.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, *imagen_pillow.size), fill=255)

        # Aplicar la mascara a la imagen
        imagen_pillow.putalpha(mask)

        # Crear un archivo temporal para la imagen
        temp_image_path = tempfile.mktemp(suffix=".png")
        imagen_pillow.save(temp_image_path, format="PNG")

        imagen = ImageTk.PhotoImage(imagen_pillow)
        imagen_label.config(image=imagen)
        imagen_label.image = imagen


def generar_tarjeta():
    
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
        if 'temp_image_path' in globals():
            c.drawImage(temp_image_path, h-55, w-55, width=40, height=40)
            
    except NameError:
        pass
    
    c.save()
    
    # Mostrar un mensaje de éxito
    resultado_label.config(text=f"Tarjeta generada como '{pdf_filename}'")


# Diseño de GUI.
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
generar_button = Button(root, text="Generar Tarjeta", command=generar_tarjeta , state="disable")
generar_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = Label(root, text="")
resultado_label.grid(row=7, column=0, columnspan=2)

nombre_input.bind("<KeyRelease>", lambda event: actualizar_boton_generar())
cargo_input.bind("<KeyRelease>", lambda event: actualizar_boton_generar())
email_input.bind("<KeyRelease>", lambda event: actualizar_boton_generar())
telefono_input.bind("<KeyRelease>", lambda event: actualizar_boton_generar())

root.mainloop()