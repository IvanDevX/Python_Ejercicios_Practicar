import tkinter as tk
from tkinter import ttk
import requests
import json

# Variables globales
provincias_data = []  # Almacenar datos de provincias
selected_codpro = None  # Almacenar el valor de CODPRO seleccionado


def download_data():
    url = "https://www.el-tiempo.net/api/json/v2/home"
    url2 = "https://www.el-tiempo.net/api/json/v2/provincias"
    response = requests.get(url)

    # Guardar los datos en un archivo JSON local
    with open("home.json", "w") as json_file1:
        json.dump(response.json(), json_file1)
    progress_bar["value"] = 50
    
    response = requests.get(url2)
    # Guardar los datos en un archivo JSON local
    with open("provincias.json", "w") as json_file2:
        json.dump(response.json(), json_file2)
        
    # Actualizar la barra de progreso al 100%
    progress_bar["value"] = 100
    load_data()


def load_data():
    try:
        # Cargar datos desde el archivo JSON local
        with open("home.json", "r") as json_file1:
            data = json.load(json_file1)
            # Asegurarse de que "provincias" es una lista de diccionarios
            if "provincias" in data and isinstance(data["provincias"], list):
                provincias_data = data["provincias"]
                # Obtener los nombres de las provincias
                ciudades_combobox["values"] = [prov["NOMBRE_PROVINCIA"] for prov in provincias_data]
                ciudades_combobox.set(provincias_data[0]["NOMBRE_PROVINCIA"])
                
                
                status_label.config(text="Datos cargados con éxito")
            else:
                status_label.config(text="Estructura de datos incorrecta")
    except FileNotFoundError:
        status_label.config(text="Archivo de datos no encontrado")


def select_provincia():
    selected_provincia = ciudades_combobox.get()
    with open("home.json", "r") as json_file1:
        data = json.load(json_file1)
        
        provincias_data = data["provincias"]
    # Buscar el valor de "CODPROV" correspondiente a la provincia seleccionada
    selected_codpro = None
    for prov in provincias_data:
        if prov["NOMBRE_PROVINCIA"] == selected_provincia:
            selected_codpro = prov["CODPROV"]
            break

    # Llamar a la funcioon que necesita el valor de CODPRO
    if selected_codpro is not None:
        otra_funcion(selected_codpro , selected_provincia)


def otra_funcion(selected_codpro , selected_provincia):
    # Esta funcin recibe el valor de CODPRO y puede usarlo como sea necesario
    print(f"El valor de CODPROV es: {selected_codpro}")
    nombre_elegido_label.config(text=f"Has seleccionado {selected_provincia}")
    
    url3 = f"https://www.el-tiempo.net/api/json/v2/provincias/{selected_codpro}"
    response = requests.get(url3)
    data3 = response.json()
    print(url3)
    
    for ciudades in data3["ciudades"]:
        
        if ciudades["idProvince"] == selected_codpro:
            estado = ciudades["stateSky"]["description"]
            temperatura_max = ciudades["temperatures"]["max"]
            temperatura_min = ciudades["temperatures"]["min"]
        
            estado_label.config(text=f"Estado del cielo: {estado}")
            temperatura_max_label.config(text=f"Temperatura máxima: {temperatura_max}°C")
            temperatura_min_label.config(text=f"Temperatura mínima: {temperatura_min}°C")
        
    
root = tk.Tk()
root.title("Aplicacion del tiempo")
root.resizable(0, 0)
root.geometry("400x300")

# Barra de progreso
progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
progress_bar.pack(pady=10)

# Etiqueta de estado
status_label = tk.Label(root, text="")
status_label.pack()

# Botón para descargar datos
download_button = ttk.Button(root, text="Descargar datos", command=download_data)
download_button.pack(pady=10)

# Combobox para seleccionar la provincia
ciudades_combobox = ttk.Combobox(root)
ciudades_combobox.pack(pady=10)

# Botón para seleccionar
select_button = ttk.Button(root, text="Seleccionar", command=select_provincia)
select_button.pack()

# Etiquetas para mostrar los datos del clima
estado_label = tk.Label(root, text="")
estado_label.pack()
nombre_elegido_label = tk.Label(root, text="")
nombre_elegido_label.pack()
temperatura_max_label = tk.Label(root, text="")
temperatura_max_label.pack()
temperatura_min_label = tk.Label(root, text="")
temperatura_min_label.pack()


root.mainloop()