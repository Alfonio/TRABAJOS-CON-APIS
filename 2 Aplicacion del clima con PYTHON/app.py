import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

import ttkbootstrap

# Funcion obtener info de OpenWeatherMap API
def obtener_clima(ciudad):
    Api_key = "d3022145cc724b5ba81f7bbe0756b9cb"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={Api_key}&lang=es&units=metric"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Error", "Ciudad no encontrada/No existe")
        return None

    clima = res.json()
    
    if 'cod' in clima and clima['cod'] == '404':
        messagebox.showerror("Error", "Ciudad no encontrada/No existe")
        return None

    icono_id = clima['weather'][0]['icon']
    temp_actual = clima['main']['temp']
    temp_min = clima['main']['temp_min']
    temp_max = clima['main']['temp_max']
    vel_viento = clima['wind']['speed']  # Nueva línea para obtener la velocidad del viento
    descripcion = clima['weather'][0]['description'].capitalize()
    ciudad = clima['name']
    pais = clima['sys']['country']
    
    iconos_url = f"https://openweathermap.org/img/wn/{icono_id}.png"
    return (iconos_url, temp_actual, temp_min, temp_max, vel_viento, descripcion, ciudad, pais)

# Funcion para buscar el clima por pais   
def buscador():
    ciudad = Ciudad_entrada.get()
    resultado = obtener_clima(ciudad)     
    if resultado is None:
        return

    iconos_url, temp_actual, temp_min, temp_max, vel_viento, descripcion, ciudad, pais = resultado
    Label_localizacion.configure(text=f"{ciudad}, {pais}", fg="blue")
    
    response = requests.get(iconos_url)
    if response.status_code == 200:
        image_data = response.content
        imagen = Image.open(BytesIO(image_data))
        imagen = imagen.resize((100, 100), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        Icono_label.configure(image=imagen)
        Icono_label.image = imagen
    else:
        print("Error al descargar la imagen")

    Label_temperatura.configure(text=f"Temp. actual: {temp_actual:.2f}°C\n"
                                       f"Temp. mínima: {temp_min:.2f}°C\n"
                                       f"Temp. máxima: {temp_max:.2f}°C\n"
                                       f"Vel. viento: {vel_viento} m/s", fg="green")  # Mostrar la velocidad del viento
    
    Label_descripcion_clima.configure(text=f"Descripción: {descripcion}", fg="brown")

# Nombre del tema, titulo de la app y el tamaño
root = ttkbootstrap.Window(themename="morph")
root.title("App Clima")
root.geometry("1920x1080")

# Input para poner nombre de ciudad indicada por usuario
Ciudad_entrada = ttkbootstrap.Entry(root, font="Helvetica 18")
Ciudad_entrada.pack(pady=10) 

# Boton de busqueda del clima
Boton_busqueda = ttkbootstrap.Button(root, text="Buscar", command=buscador, bootstyle="warning")
Boton_busqueda.pack(pady=10)

# Label para mostrar nombre-ciudad
Label_localizacion = tk.Label(root, font="Helvetica 25", fg="blue")
Label_localizacion.pack(pady=20)

# Label mostrar icono-clima
Icono_label = tk.Label(root)
Icono_label.pack()

# Label mostrar-temperatura
Label_temperatura = tk.Label(root,font="Helvetica 20", fg="green")
Label_temperatura.pack()

# Label descripcion-clima
Label_descripcion_clima = tk.Label(root,font="Helvetica 20", fg="brown")
Label_descripcion_clima.pack()

root.mainloop()
