import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import random

class JuegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Juegos")
        self.root.geometry("600x600")

        self.establecer_fondo("menujuegos.png")

        self.crear_botones()

    def establecer_fondo(self, ruta_imagen):
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((600, 600), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")
        self.canvas.image = self.fondo

    def crear_botones(self):
        botones_frame = tk.Frame(self.canvas, bg='blue')
        botones_frame.place(relx=0.5, rely=0.55, anchor='center')

        btn_juego1 = tk.Button(botones_frame, text="Piedra, Papel o Tijera", command=self.abrir_juego1,
                                font=("Helvetica", 25, "bold"), fg="white", bg="black",
                                activebackground="#D02090", activeforeground="white")
        btn_juego1.pack(pady=(10, 10), fill="x")

        btn_juego2 = tk.Button(botones_frame, text="Adivina el número", command=self.abrir_juego2,
                                font=("Helvetica", 25, "bold"), fg="white", bg="black",
                                activebackground="#D02090", activeforeground="white")
        btn_juego2.pack(pady=(10, 10), fill="x")

        btn_juego3 = tk.Button(botones_frame, text="Traduce la palabra", command=self.abrir_juego3,
                                font=("Helvetica", 25, "bold"), fg="white", bg="black",
                                activebackground="#D02090", activeforeground="white")
        btn_juego3.pack(pady=(10, 10), fill="x")

    def abrir_juego1(self):
        self.root.withdraw()
        juego1_window = Toplevel(self.root)
        Juego1(juego1_window)

    def abrir_juego2(self):
        self.root.withdraw()
        juego2_window = Toplevel(self.root)
        Juego2(juego2_window)

    def abrir_juego3(self):
        self.root.withdraw()
        juego3_window = Toplevel(self.root)
        Juego3(juego3_window)

class Juego1:
    def __init__(self, window):
        self.window = window
        self.window.title("Piedra, Papel o Tijera")
        self.window.geometry("600x600")

        self.establecer_fondo("ppt.jpeg")

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        self.canvas.create_text(300, 50, text="Piedra, Papel o Tijera", font=("Helvetica", 30, "bold", "italic"), fill="black")

        self.botones_frame = tk.Frame(self.canvas, bg='blue')
        self.canvas.create_window(300, 250, window=self.botones_frame)

        self.crear_botones()

    def establecer_fondo(self, ruta_imagen):
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((600, 600), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

    def crear_botones(self):
        btn_piedra = tk.Button(self.botones_frame, text="Piedra", font=("Helvetica", 20), command=lambda: self.jugar("Piedra"))
        btn_papel = tk.Button(self.botones_frame, text="Papel", font=("Helvetica", 20), command=lambda: self.jugar("Papel"))
        btn_tijera = tk.Button(self.botones_frame, text="Tijera", font=("Helvetica", 20), command=lambda: self.jugar("Tijera"))

        btn_piedra.pack(pady=10)
        btn_papel.pack(pady=10)
        btn_tijera.pack(pady=10)

        self.resultado_texto = self.canvas.create_text(300, 400, text="", font=("Helvetica", 20, "bold"), fill="black")

    def jugar(self, eleccion_usuario):
        opciones = ['Piedra', 'Papel', 'Tijera']
        eleccion_computadora = random.choice(opciones)
        resultado = ""

        if eleccion_usuario == eleccion_computadora:
            resultado = "Empate"
        elif (eleccion_usuario == 'Piedra' and eleccion_computadora == 'Tijera') or \
             (eleccion_usuario == 'Papel' and eleccion_computadora == 'Piedra') or \
             (eleccion_usuario == 'Tijera' and eleccion_computadora == 'Papel'):
            resultado = "¡Has ganado!"
        else:
            resultado = "Has perdido."

        self.canvas.itemconfig(self.resultado_texto, text=f"Máquina: {eleccion_computadora}\n{resultado}")

class Juego2:
    def __init__(self, window):
        self.window = window
        self.window.title("Adivina el Número")
        self.window.geometry("600x600")

        self.establecer_fondo("adivinanum.jpeg")

        self.numero_a_adivinar = random.randint(0, 200)
        self.intentos = 3

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        self.canvas.create_text(300, 50, text="Adivina el Número", font=("Helvetica", 30, "bold", "italic"), fill="black")

        self.resultado_texto = self.canvas.create_text(300, 150, text="", font=("Helvetica", 18, "bold"), fill="black")

        self.entrada = tk.Entry(self.window, font=("Helvetica", 18))
        self.canvas.create_window(300, 250, window=self.entrada)

        self.boton_adivinar = tk.Button(self.window, text="Adivinar", command=self.adivinar_numero, font=("Helvetica", 18))
        self.canvas.create_window(300, 300, window=self.boton_adivinar)

    def establecer_fondo(self, ruta_imagen):
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((600, 600), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

    def adivinar_numero(self):
        adivinanza = self.entrada.get()

        if not adivinanza.isdigit():
            self.canvas.itemconfig(self.resultado_texto, text="Por favor, introduce un número válido.")
            return

        adivinanza = int(adivinanza)

        if adivinanza < self.numero_a_adivinar:
            self.intentos -= 1
            self.canvas.itemconfig(self.resultado_texto, text=f"El número es mayor. Te quedan {self.intentos} intentos.")
        elif adivinanza > self.numero_a_adivinar:
            self.intentos -= 1
            self.canvas.itemconfig(self.resultado_texto, text=f"El número es menor. Te quedan {self.intentos} intentos.")
        else:
            self.canvas.itemconfig(self.resultado_texto, text="¡Muy bien, lo adivinaste!")
            self.boton_adivinar.config(state=tk.DISABLED)
            return

        if self.intentos <= 0:
            self.canvas.itemconfig(self.resultado_texto, text=f"Lo siento, has perdido. El número era {self.numero_a_adivinar}.")
            self.boton_adivinar.config(state=tk.DISABLED)

class Juego3:
    def __init__(self, window):
        self.window = window
        self.window.title("Traduce la palabra")
        self.window.geometry("600x600")

        self.establecer_fondo("traduce.jpeg")

        self.palabras = {
            "apple": "manzana",
            "banana": "plátano",
            "grape": "uva",
            "orange": "naranja",
            "pear": "pera",
            "watermelon": "sandía",
            "strawberry": "fresa",
            "blueberry": "arándano",
            "peach": "durazno",
            "kiwi": "kiwi",
        }

        self.palabras_aleatorias = random.sample(list(self.palabras.keys()), 10)
        self.puntuacion = 0

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        self.canvas.create_text(300, 50, text="Traduce la palabra", font=("Helvetica", 30, "bold", "italic"), fill="black")

        self.resultado_texto = self.canvas.create_text(300, 150, text="", font=("Helvetica", 18, "bold"), fill="black")

        self.entrada = tk.Entry(self.window, font=("Helvetica", 18))
        self.canvas.create_window(300, 250, window=self.entrada)

        self.boton_enviar = tk.Button(self.window, text="Enviar", command=self.verificar_traduccion, font=("Helvetica", 18))
        self.canvas.create_window(300, 300, window=self.boton_enviar)

        self.mostrar_pregunta()

    def establecer_fondo(self, ruta_imagen):
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((600, 600), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

    def mostrar_pregunta(self):
        self.palabra_actual = self.palabras_aleatorias.pop()
        self.canvas.itemconfig(self.resultado_texto, text=f"¿Cómo se dice '{self.palabra_actual}' en español?")

    def verificar_traduccion(self):
        traduccion_usuario = self.entrada.get()
        traduccion_correcta = self.palabras[self.palabra_actual]

        if traduccion_usuario.lower() == traduccion_correcta:
            self.puntuacion += 1
            resultado = "¡Correcto!"
        else:
            resultado = f"Incorrecto. La traducción correcta es '{traduccion_correcta}'."

        self.canvas.itemconfig(self.resultado_texto, text=f"{resultado}\nPuntuación: {self.puntuacion}")

        if self.palabras_aleatorias:
            self.mostrar_pregunta()
        else:
            self.canvas.itemconfig(self.resultado_texto, text=f"Juego terminado. Puntuación final: {self.puntuacion}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoApp(root)
    root.mainloop()
