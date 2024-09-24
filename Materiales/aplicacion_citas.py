
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

# Función para salir de la aplicación
def salir_aplicacion():
    root.quit()

# Ventana principal
root = tk.Tk()
root.title("Gestión de Citas Médicas")
root.geometry("400x550")
root.configure(bg="#E0F7FA")  # Fondo azul muy claro

# Cargar imagen (debes tener una imagen llamada 'logo.png' en el mismo directorio)
imagen = Image.open("th.png")
imagen = imagen.resize((150, 150), Image.Resampling.LANCZOS)  # Aquí el cambio
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(root, image=imagen_tk, bg="#E0F7FA")  # Fondo azul claro
label_imagen.pack(pady=10)

# Etiquetas y entradas con color de fondo
label_nombre = tk.Label(root, text="Nombre del Paciente:", font=("Arial", 12), bg="#E0F7FA")  # Fondo azul claro
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(pady=5)

label_doctor = tk.Label(root, text="Seleccionar Doctor:", font=("Arial", 12), bg="#E0F7FA")  # Fondo azul claro
label_doctor.pack(pady=5)
combo_doctor = ttk.Combobox(root, values=["Dr. Pérez", "Dr. García", "Dr. Rodríguez"], width=28)
combo_doctor.pack(pady=5)

label_fecha = tk.Label(root, text="Fecha (DD/MM/AAAA):", font=("Arial", 12), bg="#E0F7FA")  # Fondo azul claro
label_fecha.pack(pady=5)
entry_fecha = tk.Entry(root, width=30)
entry_fecha.pack(pady=5)

label_hora = tk.Label(root, text="Hora (HH:MM):", font=("Arial", 12), bg="#E0F7FA")  # Fondo azul claro
label_hora.pack(pady=5)
entry_hora = tk.Entry(root, width=30)
entry_hora.pack(pady=5)

# Botón para redirigir a nueva ventana
btn_redirigir = tk.Button(root, text="Agendar cita", command=abrir_nueva_ventana, bg="#4CAF50", fg="white", width=20)
btn_redirigir.pack(pady=10)

# Botón para salir de la aplicación
btn_salir = tk.Button(root, text="Salir", command=salir_aplicacion, bg="#FF5252", fg="white", width=20)
btn_salir.pack(pady=10)

root.mainloop()