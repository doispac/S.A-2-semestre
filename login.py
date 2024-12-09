from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from DataBase import Database
import menuADM

# Janela de Login
jan = Tk()
jan.title("Doceria - Login")
jan.geometry("400x200")
jan.configure(background="white")
jan.resizable(width=False, height=False)

jan.iconbitmap(default="icons/bala.ico")

# Frame de Login
loginFrame = Frame(jan, width=400, height=200, bg="PURPLE", relief="raise")
loginFrame.pack()

UsuarioLabel = Label(loginFrame, text="Usuário: ", font=("Times New Roman", 20), bg="PURPLE", fg="white")
UsuarioLabel.place(x=5, y=65)

UsuarioEntry = ttk.Entry(loginFrame, width=30)
UsuarioEntry.place(x=120, y=75)

SenhaLabel = Label(loginFrame, text="Senha: ", font=("Times New Roman", 20), bg="PURPLE", fg="white")
SenhaLabel.place(x=5, y=105)

SenhaEntry = ttk.Entry(loginFrame, width=30, show="•")
SenhaEntry.place(x=120, y=115)

# Supondo que menuADM é uma janela existente
def Login():
    usuario = UsuarioEntry.get()
    senha = SenhaEntry.get()
    
    db = Database()
    db.cursor.execute("""
    SELECT * FROM tb_usuario
    WHERE login_usuario = %s AND senha_usuario = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()
    
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Login efetuado com sucesso")
        jan.withdraw()  # Oculta a tela de login
        menuADM.deiconify()  # Mostra a tela menuADM existente
    else:
        messagebox.showinfo(title="INFO LOGIN", message="Usuário ou Senha Inválida!")

# Botão de Login
LoginButton = ttk.Button(loginFrame, text="LOGIN", width=15, command=Login)
LoginButton.place(x=150, y=150)

# Aqui você cria ou referencia a tela menuADM existente
menuADM = Toplevel()
menuADM.title("Doceria - Menu ADM")
menuADM.geometry("500x400")
menuADM.configure(background="white")
menuADM.resizable(width=False, height=False)
menuADM.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso

Label(menuADM, text="Bem-vindo ao Menu ADM!", font=("Times New Roman", 24), bg="white", fg="purple").pack(pady=50)
Button(menuADM, text="Sair", font=("Times New Roman", 15), command=lambda: [menuADM.withdraw(), jan.deiconify()]).pack(pady=20)

jan.mainloop()


