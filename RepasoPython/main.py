import tkinter as tk
from tkinter import ttk
import os
import random
from PIL import Image, ImageTk

screen1 = tk.Tk()
screen1.title("Adivina el Hiragana")
screen1.geometry("450x450")

dirhiragana = r"C:\Users\unaip\PycharmProjects\repaso\RepasoPython\hiragana"
hiraganas = os.listdir(dirhiragana)
max_intentos = 10
intentos = 0
contador = 0
imagenes_usadas = []
dir_calificaciones = r"C:\Users\unaip\PycharmProjects\repaso\RepasoPython\calificaciones"

resultado_label = ttk.Label(screen1, text="", wraplength=400)
resultado_label.pack(pady=10)

imagen_calificacion_label = ttk.Label(screen1)
imagen_calificacion_label.pack(pady=10)

def mostrar_resultado():
    global imagen_calificacion_label, resultado_label
    mensaje = ""
    imagen_calificacion = ""

    if contador < 5:
        mensaje = "Súspenso. Tú, sí tú, esfuerzate más o acabarás como yo."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino1-4.png")
    elif contador == 5:
        mensaje = "Suficiente. Oye, ten cuidado que ha sido por los pelos."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino5.PNG")
    elif contador == 6:
        mensaje = "Bien. Has estado bien."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino6.png")
    elif contador >= 7 and contador <= 8:
        mensaje = "Notable. De locos."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino7-8.PNG")
    elif contador >= 9:
        mensaje = "Sobresaliente. Veo que buscas la perfección."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino9-10.PNG")

    image_label.pack_forget()
    label_respuesta.pack_forget()
    entry_respuesta.pack_forget()
    cargarimg.pack_forget()

    resultado_label.config(text=f"Tu calificación es: {contador} - {mensaje}")

    imagen = Image.open(imagen_calificacion)
    imagen = imagen.resize((200, 200))
    photo = ImageTk.PhotoImage(imagen)
    imagen_calificacion_label.config(image=photo)
    imagen_calificacion_label.image = photo

def comprobar():
    global contador, intentos

    respuesta_usuario = respuesta.get().strip().lower()
    nombre_imagen = os.path.splitext(imagenes_usadas[intentos])[0]

    if respuesta_usuario == nombre_imagen.lower():
        contador += 1
        resultado_label.config(text="¡Correcto!", foreground="green")
    else:
        resultado_label.config(text=f"Incorrecto. Era: {nombre_imagen}", foreground="red")

    intentos += 1

    if intentos < max_intentos:
        actualizar_imagen()
    else:
        mostrar_resultado()

def actualizar_imagen():
    global imagenes_usadas
    while True:
        archivo_aleatorio = random.choice(hiraganas)
        if archivo_aleatorio not in imagenes_usadas:
            imagenes_usadas.append(archivo_aleatorio)
            break

    hiragana_random = os.path.join(dirhiragana, archivo_aleatorio)

    image = Image.open(hiragana_random).resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

image_label = ttk.Label(screen1)
image_label.pack(pady=10)

resultado_label = ttk.Label(screen1, text="")
resultado_label.pack(pady=10)

label_respuesta = ttk.Label(screen1, text="Ingrese su respuesta, por favor:")
label_respuesta.pack(pady=10)

respuesta = tk.StringVar()
entry_respuesta = ttk.Entry(screen1, width=35, textvariable=respuesta)
entry_respuesta.pack(padx=10, pady=10)
entry_respuesta.focus()

cargarimg = ttk.Button(screen1, text="Comprobar", command=comprobar)
cargarimg.pack(pady=10)

cerrar = ttk.Button(screen1, text="Cerrar", command=screen1.destroy)
cerrar.pack(pady=10)

actualizar_imagen()

screen1.mainloop()
