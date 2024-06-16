import tkinter as tk
from tkinter import ttk, messagebox

class MenuBar:
    def __init__(self, root):
        self.root = root

        # Crear un objeto Style
        self.style = ttk.Style()

        # Configurar el estilo de la barra de menú
        self.style.theme_use('clam')
        self.style.configure('MenuBar.TMenubutton', background='#ADD8E6')  # Configurar el color de fondo a azul claro

        # Crear un objeto Menu
        self.menu_bar = tk.Menu(root)

        # Crear los menús principales
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.dictionary_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.config_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Configurar los menús principales
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Diccionario", menu=self.dictionary_menu)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        self.menu_bar.add_cascade(label="Configuración", menu=self.config_menu)

        # Agregar opciones al menú Archivo
        self.file_menu.add_command(label="Abrir", command=self.show_advertencia)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Agregar opciones al menú Diccionario
        self.dictionary_menu.add_command(label="Buscar", command=self.show_advertencia)
        self.dictionary_menu.add_command(label="Añadir", command=self.show_advertencia)
        self.dictionary_menu.add_command(label="Eliminar", command=self.show_advertencia)

        # Agregar opciones al menú Ayuda
        self.help_menu.add_command(label="Acerca de", command=self.show_help_message)

        # Agregar opciones al menú Configuración
        self.config_menu.add_command(label="Opción 1", command=self.show_advertencia)
        self.config_menu.add_command(label="Opción 2", command=self.show_advertencia)

        # Configurar la barra de menú en la ventana principal
        root.config(menu=self.menu_bar)

    def show_help_message(self):
        # Diccionario con las etiquetas y sus explicaciones
        etiquetas = {
            "ADJ": "Adjetivos",
            "ADP": "Adposiciones",
            "ADV": "Adverbios",
            "AUX": "Verbos auxiliares",
            "CONJ": "Conjunciones",
            "CCONJ": "Conjunciones de coordinación",
            "DET": "Determinantes",
            "INTJ": "Interjecciones",
            "NOUN": "Sustantivos",
            "NUM": "Numerales",
            "PART": "Partículas",
            "PRON": "Pronombres",
            "PROPN": "Nombres propios",
            "PUNCT": "Signos de puntuación",
            "SCONJ": "Conjunciones subordinadas",
            "SYM": "Símbolos",
            "VERB": "Verbos",
            "X": "Otros",
            "Total Words": "Total de palabras",
            "N Sentences": "Número de oraciones",
            "Avg Words/Sentence": "Promedio de palabras por oración",
            "PM": "Palabras malsonantes",
            "PG": "Palabras mayores a 6 letras"
        }

        # Formatear el mensaje de ayuda
        mensaje = "Este programa está desarrollado para el análisis de texto a partir de parámetros, los cuales son:\n\n"
        for etiqueta, descripcion in etiquetas.items():
            mensaje += f"{etiqueta}: {descripcion}\n"

        # Mostrar el cuadro de diálogo de ayuda
        messagebox.showinfo("Ayuda", mensaje)
    
    def show_advertencia(self):
        messagebox.showinfo("Advertencia", "Lo sentimos, esta funcionalidad está en desarrollo. Pronto estará disponible.")