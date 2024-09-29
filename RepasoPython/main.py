import tkinter as tk
from tkinter import ttk
import os
import random
from PIL import Image, ImageTk

# Inicializa la ventana principal de la aplicación
screen1 = tk.Tk()
screen1.title("Adivina el Hiragana")
screen1.geometry("600x600")

# Directorio que contiene las imágenes de Hiragana
dirhiragana = r"C:\Users\unaip\PycharmProjects\repaso\RepasoPython\hiragana"
hiraganas = os.listdir(dirhiragana)
max_intentos = 10  # Límite de imágenes
intentos = 0  # Contador de intentos
contador = 0  # Contador de respuestas correctas
imagenes_usadas = []  # Lista para llevar un registro de las imágenes mostradas

# Directorio para las imágenes de calificación
dir_calificaciones = r"C:\Users\unaip\PycharmProjects\repaso\RepasoPython\calificaciones"

# Etiquetas para el mensaje de resultado y la imagen de calificación
resultado_label = ttk.Label(screen1, text="", wraplength=400)
resultado_label.pack(pady=10)

imagen_calificacion_label = ttk.Label(screen1)  # Etiqueta para la imagen de calificación
imagen_calificacion_label.pack(pady=10)

# Función para mostrar el resultado y la imagen
def mostrar_resultado():
    global imagen_calificacion_label, resultado_label
    mensaje = ""
    imagen_calificacion = ""

    if contador < 5:
        mensaje = "Súspenso. Tú, sí tú, esfuerzate más o acabarás como yo."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino1-4.png")  # Imagen para suspenso
    elif contador == 5:
        mensaje = "Suficiente. Oye, ten cuidado que ha sido por los pelos."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino5.PNG")  # Imagen para suficiente
    elif contador == 6:
        mensaje = "Bien. Has estado bien."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino6.png")  # Imagen para bien
    elif contador >= 7 and contador <= 8:
        mensaje = "Notable. De locos."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino7-8.PNG")  # Imagen para notable
    elif contador >= 9:
        mensaje = "Sobresaliente. Veo que buscas la perfección."
        imagen_calificacion = os.path.join(dir_calificaciones, "pingüino9-10.PNG")  # Imagen para sobresaliente


    image_label.pack_forget()
    label_respuesta.pack_forget()
    entry_respuesta.pack_forget()
    cargarimg.pack_forget()

    resultado_label.config(text=f"Tu calificación es: {contador} - {mensaje}")

    # Cargar y mostrar la imagen de calificación
    imagen = Image.open(imagen_calificacion)
    imagen = imagen.resize((200, 200))
    photo = ImageTk.PhotoImage(imagen)
    imagen_calificacion_label.config(image=photo)
    imagen_calificacion_label.image = photo  # Mantiene una referencia para evitar la recolección de basura

# Función para verificar la respuesta del usuario
def comprobar():
    global contador, intentos

    # Obtiene la respuesta del usuario
    respuesta_usuario = respuesta.get().strip().lower()
    nombre_imagen = os.path.splitext(imagenes_usadas[intentos])[0]

    if respuesta_usuario == nombre_imagen.lower():
        contador += 1
        resultado_label.config(text="¡Correcto!", foreground="green")
    else:
        resultado_label.config(text=f"Incorrecto. Era: {nombre_imagen}", foreground="red")

    intentos += 1  # Incrementa el contador de intentos

    # Actualiza la imagen o muestra el resultado final si se alcanzó el límite
    if intentos < max_intentos:
        actualizar_imagen()
    else:
        mostrar_resultado()

# Función para actualizar la imagen
def actualizar_imagen():
    global imagenes_usadas
    # Escoge una imagen aleatoria que no ha sido usada
    while True:
        archivo_aleatorio = random.choice(hiraganas)
        if archivo_aleatorio not in imagenes_usadas:
            imagenes_usadas.append(archivo_aleatorio)
            break

    hiragana_random = os.path.join(dirhiragana, archivo_aleatorio)

    # Carga una nueva imagen
    image = Image.open(hiragana_random).resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Mantiene una referencia para evitar la recolección de basura

# Crea los widgets en el orden deseado
image_label = ttk.Label(screen1)
image_label.pack(pady=10)

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

# Inicializa la primera imagen
actualizar_imagen()

# Inicia el bucle principal de eventos
screen1.mainloop()
