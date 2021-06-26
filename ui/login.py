# LIBRERIAS REQUERIDAS
from tkinter import *
from PIL import ImageTk, Image
import os
def iniciar(event):
    nombre = txt_nombre.get()
    usuario = txt_usuario.get()
    email = txt_email.get()
    clave = txt_clave.get()
    clave_confirm = txt_confirm_clave.get()
    print(f"{nombre} {usuario} {clave} {email} {clave_confirm}")


# GENERAMOS LA INTERFAZ 
win_login = Tk() 
win_login.title("Login CODB")
win_login.geometry("500x700")

# CAMPOS REQUERIDOS PARA EL LOGIN
archivo = os.path.dirname(__file__)+"/banner.jpg"
imagen = ImageTk.PhotoImage(Image.open(archivo))
Label(win_login, image=imagen, bd=0).pack(side = "top")

lab_nombre = Label(win_login,text="Escribe tu nombre")
lab_nombre.config(fg="blue",    # Foreground
             bg="green",   # Background
             font=("Verdana",48))
txt_nombre = Entry(win_login, bd=2, width=50)
lab_usuario = Label(win_login,text="Escribe tu usuario")
txt_usuario = Entry(win_login, bd=2, width=50)
lab_email = Label(win_login,text="Escribe tu email")
txt_email = Entry(win_login, bd=2, width=50)
lab_clave = Label(win_login,text="Escribe tu clave")
txt_clave = Entry(win_login, bd=2, width=50, show="*")
lab_confirm_clave= Label(win_login,text="Escribe confirmar clave")
txt_confirm_clave = Entry(win_login, bd=2, width=50, show="*")
# AGREGAMOS EL BOTÓN DE REGISTR
btn_iniciar = Button(None, text='Registrar')
# AGREGA LOS ELEMENTOS A LA VENTANA
lab_nombre.pack()
txt_nombre.pack()
lab_usuario.pack()
txt_usuario.pack()
lab_email.pack()
txt_email.pack()
lab_clave.pack()
txt_clave.pack()
lab_confirm_clave.pack()
txt_confirm_clave.pack()
btn_iniciar.pack()

# EVENTOS
btn_iniciar.bind('<Button-1>', iniciar)

# EJECUTAMOS LA INTERFAZ
win_login.mainloop()