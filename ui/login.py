# LIBRERIAS REQUERIDAS
from tkinter import *

def iniciar(event):
    if txt_password.get() =="clave" and txt_usuario.get() == "edwin":
        print("Login Correcto") 
    else:
        print("Login Incorrecto")


# GENERAMOS LA INTERFAZ 
win_login = Tk() 
win_login.title("Login CODB")
win_login.geometry("300x100")

# CAMPOS REQUERIDOS PARA EL LOGIN
txt_usuario = Entry(win_login, bd=2, width=20)
txt_password = Entry(win_login, bd=2, width=20, show="*")
btn_iniciar = Button(None, text='Iniciar')
txt_usuario.pack()
txt_password.pack()
btn_iniciar.pack()

# EVENTOS
btn_iniciar.bind('<Button-1>', iniciar)

# EJECUTAMOS LA INTERFAZ
win_login.mainloop()