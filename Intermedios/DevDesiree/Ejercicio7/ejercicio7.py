"""
7. **Aplicación de Clima** : Utiliza una API de pronóstico del tiempo para desarrollar una aplicación que permita a los usuarios ingresar una ubicación 
                            y obtener información actualizada sobre el clima.

   Puedes usar la que quieras o esta : [link](https://www.el-tiempo.net/api)
"""

from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from api_weather import API_KEY

# Configuramos el tamaño , titulo, y color de fondo de la ventana
tk = Tk()
tk.title("Aplicación del tiempo")
tk.geometry("450x285")
tk.resizable(0,0)
tk.configure(background='black')

# Configura la ventana mas transparente
tk.attributes("-alpha", 0.9)


def get_weather(weather):
    """
    1.- Guardamos en las variables la informacion de la seccion seleccionada de la API
    2.- en la URL_ICON guardamos la url donde se alojan los iconos de la pagina openweathermap: "https://openweathermap.org/img/wn/{icon_weather}@2x.png"
    """
    name_city = weather["name"]
    description = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    temp_min = weather["main"]["temp_min"]
    temp_max = weather["main"]["temp_max"]
    icon_weather = weather["weather"][0]["icon"]
    URL_ICON = f"https://openweathermap.org/img/wn/{icon_weather}@2x.png"
    
    # Mostramos los valores de la llamada de la API previamente en una variable ya declarada
    location_value_label.config(text=name_city)
    description_value_label.config(text=description.capitalize())
    actual_temp_value_label.config(text=f"{temp}°C")
    temp_min_value_label.config(text=f"{temp_min}°C")
    temp_max_value_label.config(text=f"{temp_max}°C")
    
    # Limpia el error_label si ya existe
    error_label.config(text="", background="black")
   
   # Carga la imagen de icono_weather
    response = requests.get(URL_ICON, stream=True)
    image = Image.open(response.raw)
    photo = ImageTk.PhotoImage(image)
    
    # Muestra la imagen en un label y mantiene la referencia al objeto PhotoImage, para evitar que la imagen no se muestre
    icon_label.config(image=photo)
    icon_label.photo = photo  

def weather_json():
    """
    1.- Manejamos errores en el caso de que no exista una ciudad de la API
    2.- Solicita a la API con el input del usuario, la ciudad
    3.- Configuramos los parametros de la API
    4.- Llamamos a la funcion get_weather pasandole como parametro el resultado de la API en formato JSON
    """
    try:
        entry_city = input_city.get()
        API_key = API_KEY
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"q": entry_city, "appid": API_key, "units": "metric", "lang": "es"}
        response = requests.get(URL, params=parametros)
        weather = response.json()
        get_weather(weather)

    except KeyError:
        # Muestra el mensaje de error en el error_label
        error_label.config(text="No se encuentra esa ubicación")
    

# Label de las ubicacion, input y boton
city_ubication = ttk.Label(tk, background="black", foreground="gray", text="Escribe la ubicación:", font=("arial", 12))
city_ubication.grid(row=1, column=0, columnspan=3, pady=5 )

input_city = ttk.Entry(tk, font=11)
input_city.grid(row=2,column=0, padx=5, pady=5, columnspan=3)

btn_search = ttk.Button(tk, text = "Búsqueda!", command=weather_json)
btn_search.grid(row=2, column=2)

# Se crea un Label para mostrar errores
error_label = ttk.Label(tk, text="", foreground="red" , state=HIDDEN, background="black", font=("arial", 11))
error_label.grid(row=3,column=0, columnspan=3)

# Labels con sus titulos
location_label = ttk.Label(tk, text="Ubicación:", background="black", foreground="white", font=("arial", 11))
location_label.grid(row=4, column=0, padx=20)

description_label = ttk.Label(tk, text="Descripción:", background="black", foreground="white", font=("arial", 11))
description_label.grid(row=4, column=1, padx=20)

actual_temp_label = ttk.Label(tk, text="Tiempo actual:", background="black", foreground="white", font=("arial", 11))
actual_temp_label.grid(row=4, column=2, padx=20)

temp_min_label = ttk.Label(tk, text="Temp. mínima:", background="black", foreground="green", font=("arial", 11))
temp_min_label.grid(row=6, column=0, padx=20)

temp_max_label = ttk.Label(tk, text="Temp.máxima:", background="black", foreground="red", font=("arial", 11))
temp_max_label.grid(row=6, column=1, padx=20)

icon_weather_label = ttk.Label(tk, text="Leyenda:", background="black", foreground="white", font=("arial", 11))
icon_weather_label.grid(row=6, column=2, padx=20)

# Labels para mostrar los valores del clima
location_value_label = ttk.Label(tk, text="", background="black", foreground="white", font=("arial", 11))
location_value_label.grid(row=5, column=0, pady=20)

description_value_label = ttk.Label(tk, text="", background="black", foreground="white", font=("arial", 11))
description_value_label.grid(row=5, column=1, pady=20)

actual_temp_value_label = ttk.Label(tk, text="", background="black", foreground="white", font=("arial", 11))
actual_temp_value_label.grid(row=5, column=2, pady=20)

temp_min_value_label = ttk.Label(tk, text="", background="black", foreground="white", font=("arial", 11))
temp_min_value_label.grid(row=7, column=0)

temp_max_value_label = ttk.Label(tk, text="", background="black", foreground="white", font=("arial", 11))
temp_max_value_label.grid(row=7, column=1)

icon_label = ttk.Label(tk, background="black")
icon_label.grid(row=7, column=2)

tk.mainloop()