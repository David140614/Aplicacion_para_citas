import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Función para cambiar de ventana
def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("400x300")
    label_nueva = tk.Label(nueva_ventana, text="Bienvenido a la nueva ventana", font=("Arial", 14), fg="blue")
    label_nueva.pack(pady=50)

# Ventana principal
root = tk.Tk()
root.title("Gestión de Citas Médicas")
root.geometry("400x400")
root.configure(bg="#F0F0F0")

# Cargar imagen (debes tener una imagen llamada 'logo.png' en el mismo directorio)
imagen = Image.open("logo.png")
imagen = imagen.resize((100, 100), Image.ANTIALIAS)
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(root, image=imagen_tk, bg="#F0F0F0")
label_imagen.pack(pady=10)

# Etiquetas y entradas con color de fondo
label_nombre = tk.Label(root, text="Nombre del Paciente:", font=("Arial", 12), bg="#F0F0F0")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(pady=5)

label_doctor = tk.Label(root, text="Seleccionar Doctor:", font=("Arial", 12), bg="#F0F0F0")
label_doctor.pack(pady=5)
combo_doctor = ttk.Combobox(root, values=["Dr. Pérez", "Dr. García", "Dr. Rodríguez"], width=28)
combo_doctor.pack(pady=5)

label_fecha = tk.Label(root, text="Fecha (DD/MM/AAAA):", font=("Arial", 12), bg="#F0F0F0")
label_fecha.pack(pady=5)
entry_fecha = tk.Entry(root, width=30)
entry_fecha.pack(pady=5)

label_hora = tk.Label(root, text="Hora (HH:MM):", font=("Arial", 12), bg="#F0F0F0")
label_hora.pack(pady=5)
entry_hora = tk.Entry(root, width=30)
entry_hora.pack(pady=5)

# Botón para redirigir a nueva ventana
btn_redirigir = tk.Button(root, text="Ir a otra ventana", command=abrir_nueva_ventana, bg="#4CAF50", fg="white", width=20)
btn_redirigir.pack(pady=20)

root.mainloop()