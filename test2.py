import cv2
import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Captura de Imagen")

        # Iniciar la cámara
        self.vid = cv2.VideoCapture(video_source)

        # Botón para tomar la captura de la imagen
        self.btn_snapshot = tk.Button(window, text="Tomar Foto", command=self.snapshot)
        self.btn_snapshot.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para guardar la imagen capturada
        self.btn_save = tk.Button(window, text="Guardar Foto", command=self.save_snapshot)
        self.btn_save.pack(side=tk.RIGHT, padx=10, pady=10)

        # Crear un lienzo para mostrar la imagen capturada
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Actualizar la ventana
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Tomar la captura de la imagen
        ret, frame = self.vid.read()

        # Convertir la imagen a RGB y crear un objeto ImageTk
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))

        # Mostrar la imagen en el lienzo
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Almacenar la imagen en una variable para poder guardarla después
        self.snapshot_image = frame

    def save_snapshot(self):
        # Obtener el nombre del archivo de la imagen a guardar
        filename = tk.filedialog.asksaveasfilename(defaultextension=".png")

        # Si se seleccionó un nombre de archivo, guardar la imagen
        if filename:
            cv2.imwrite(filename, self.snapshot_image)

    def update(self):
        # Obtener un fotograma de la cámara
        ret, frame = self.vid.read()

        if ret:
            # Convertir la imagen a RGB y crear un objeto ImageTk
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))

            # Mostrar la imagen en el lienzo
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Actualizar la ventana después de 15 milisegundos
        self.window.after(15, self.update)

# Iniciar la aplicación
App(tk.Tk())
