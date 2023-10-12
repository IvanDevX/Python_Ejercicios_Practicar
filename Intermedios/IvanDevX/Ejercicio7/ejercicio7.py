"""
7. **Aplicación de Clima** : Utiliza una API de pronóstico del tiempo para desarrollar una aplicación que 
permita a los usuarios ingresar una ubicación y obtener información actualizada sobre el clima.

"""
# Importacion de Librerias
from tkinter import *
from tkinter import ttk
import requests


def open_new_window(today, tomorrow):
    """
    Le viene como parametros el texto de hoy y mañana
    Crea y abre una nueva ventana vinculada a la principal y muestra los datos de hoy y mañana
    """
    new_window = Toplevel(root)
    new_window.title("Estado de hoy y mañana")

    today_status = Text(new_window, wrap=WORD, width=140, height=10)
    today_status.insert(END, today)
    today_status.pack()

    tomorrow_status = Text(new_window, wrap=WORD, width=140, height=15)
    tomorrow_status.insert(END, tomorrow)
    tomorrow_status.pack()

    close_button = ttk.Button(new_window, text="Cerrar Ventana", command=new_window.destroy)
    close_button.pack(pady=10)


def show_temps(selected_codpro):
    """
    Se pasa como parametro el codigo de la provincia que se usa en la api
    Se busca el json en esa url y se recorren todo el diccionario
    Cuando encuentra la que corresponde con la elegida muestra los datos 
    """
    url_code_provincias = f"https://www.el-tiempo.net/api/json/v2/provincias/{selected_codpro}"
    progress_bar.pack()
    bar_status(50)
    response = requests.get(url_code_provincias)
    data_provincias = response.json()
    bar_status(100)
    
    for ciudades in data_provincias["ciudades"]:
        
        if ciudades["idProvince"] == selected_codpro:
            estado = ciudades["stateSky"]["description"]
            temperatura_max = ciudades["temperatures"]["max"]
            temperatura_min = ciudades["temperatures"]["min"]
        
            estado_label.config(text=f"Estado del cielo: {estado}")
            temperatura_max_label.config(text=f"Temperatura máxima: {temperatura_max}°C")
            temperatura_min_label.config(text=f"Temperatura mínima: {temperatura_min}°C")
            
    progress_bar.pack_forget()


def selection_cuidades(lista_provincias):
    """
    Hace un get de la eleccion del usuario y recorre las provincias, hasta dar con la elegida por el usuario.
    Luego lanza la funcion para mostrar las temperaturas con el codigo de provincia.
    """
    
    user = ciudades_combobox.get()
    for prov in lista_provincias:
        if prov["NOMBRE_PROVINCIA"] == user:
            selec_prov = prov["NOMBRE_PROVINCIA"]
            selected_codpro = prov["CODPROV"]
            nombre_elegido_label.config(text=f"Has elegido {selec_prov}")
            print(selec_prov)
            show_temps(selected_codpro)        


def show_data(data):
    """
    Guarda en variables el texto de la api del tiempo general en españa de hoy y mañana, para luego pasarlo como parametro
    Recorre la data y busca la key de provincias, 
    Luego las recorre y guarda en otra lista los nombres de las provincias.
    En el combobox muestra esa lista con las provincias.
    Cuando el usuario selecciona una , lanza la funcion de selection_ciudades,
    Tambien muestra el boton de Resumen que tiene una funcion especifica
    
    """
    progress_bar.pack_forget()
    download_data.pack_forget()
    
    today = data["today"]["p"]
    tomorrow = data["tomorrow"]["p"]
    
    lista_provincias = data["provincias"]  
    nombres_provincias = [prov["NOMBRE_PROVINCIA"] for prov in lista_provincias]
    ciudades_combobox["values"] = nombres_provincias
    ciudades_combobox.config(state="readonly")  # "readonly" para evitar edición
    ciudades_combobox.bind("<<ComboboxSelected>>", lambda event: selection_cuidades(lista_provincias))
    resume_btn.pack(pady=10)
    resume_btn.config(text="Resumen de Hoy y Mañana en España" , command=lambda: open_new_window(today, tomorrow))
    
    
def get_data():
    """
    Solicita a la API los datos necesarios y si todo esta bien muestra el mensaje, si no muestra el mensaje de error.
    
    """
    bar_status(50)
    try:
        URL = "https://www.el-tiempo.net/api/json/v2/home"
        response = requests.get(URL)
        
        if response.status_code == 200:
            data = response.json()
            status_label.config(text="Datos obtenidos con exito")
            bar_status(100)
        else:
            status_label.config(text=f"Error al obtener datos (Estado {response.status_code})")

        show_data(data)
    except:
        status_label.config(text=f"Error {response.status_code} Vuelve a Intentarlo")
        progress_bar["value"] = 0


def bar_status(rango):
    # Simulacion barra de descarga
    for i in range(1, rango + 1):
        progress_bar["value"] = i
        root.update_idletasks() #Actualizar

    if rango == 100:
        status_label.config(text="Descarga completa")
    
# Creacion de la ventana de tkinter
root = Tk()
root.title("Aplicacion del tiempo")
root.resizable(0,0) #No deja cambiar el tamaño de ventana (0=x, 0=y)
root.geometry("400x300")

progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
progress_bar.pack(pady=10)

download_data = ttk.Button(root, text="Descargar datos", command=get_data)
download_data.pack(pady=10)

resume_btn = ttk.Button(root)
resume_btn.pack_forget()

# Etiqueta de estado
status_label = ttk.Label(root, text="Esperando descarga")
status_label.pack()

# Combobox para seleccionar la provincia
ciudades_combobox = ttk.Combobox(root ,state=DISABLED)
ciudades_combobox.pack(pady=10)

# Etiquetas para mostrar los datos del clima
nombre_elegido_label = ttk.Label(root, text="")
nombre_elegido_label.pack()
estado_label = ttk.Label(root, text="")
estado_label.pack()
temperatura_max_label = ttk.Label(root, text="")
temperatura_max_label.pack()
temperatura_min_label = ttk.Label(root, text="")
temperatura_min_label.pack()


root.mainloop()