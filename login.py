from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from DataBase import Database

# Janela de Login
jan = Tk()
jan.title("Doceria - Login")
jan.geometry("400x200")
jan.configure(background="white")
jan.resizable(width=False, height=False)

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

# Função de Login
def Login():
    usuario = UsuarioEntry.get()
    senha = SenhaEntry.get()
    
    db = Database()
    db.cursor.execute("""
    SELECT id_tip FROM tb_usuario
    WHERE login_usuario = %s AND senha_usuario = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()
    
    if VerifyLogin:
        id_tip = VerifyLogin[0]
        messagebox.showinfo(title="INFO LOGIN", message="Login efetuado com sucesso")
        
        jan.withdraw()  # Oculta a tela de login
        
        if id_tip == 1:
            menuADM.deiconify()  # Mostra a tela menuADM para administrador
        elif id_tip == 2:
            menuUsuario.deiconify()  # Mostra a tela menuUsuario para usuário comum
        else:
            messagebox.showwarning(title="INFO LOGIN", message="Tipo de usuário inválido!")
    else:
        messagebox.showinfo(title="INFO LOGIN", message="Usuário ou Senha Inválida!")

# Botão de Login
LoginButton = ttk.Button(loginFrame, text="LOGIN", width=15, command=Login)
LoginButton.place(x=150, y=150)

# Criação da tela menuADM
menuADM = Toplevel()
menuADM.title("Doceria - Menu ADM")
menuADM.geometry("500x400")
menuADM.configure(background="white")
menuADM.resizable(width=False, height=False)
menuADM.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso

Label(menuADM, text="Bem-vindo ao Menu ADM!", font=("Times New Roman", 24), bg="white", fg="purple").pack(pady=50)
Button(menuADM, text="Sair", font=("Times New Roman", 15), command=lambda: [menuADM.withdraw(), jan.deiconify()]).pack(pady=20)

# Criação da tela menuUsuario
menuUsuario = Toplevel()
menuUsuario.title("Doceria - Menu Usuário")
menuUsuario.geometry("500x400")
menuUsuario.configure(background="white")
menuUsuario.resizable(width=False, height=False)
menuUsuario.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso

Label(menuUsuario, text="Bem-vindo ao Menu Usuário!", font=("Times New Roman", 24), bg="white", fg="blue").pack(pady=50)
Button(menuUsuario, text="Sair", font=("Times New Roman", 15), command=lambda: [menuUsuario.withdraw(), jan.deiconify()]).pack(pady=20)

# Loop principal da interface
jan.mainloop()
