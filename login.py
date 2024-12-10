from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from DataBase import Database
import subprocess

# Janela de Login
jan = Tk()
jan.title("Doceria - Login")
jan.geometry("400x200")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap("icons/bala.ico")

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
    db.cursor.execute("""SELECT id_tip FROM tb_usuario WHERE login_usuario = %s AND senha_usuario = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()
    
    if VerifyLogin:
        id_tip = VerifyLogin[0]
        
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
menuADM.geometry("400x300")
menuADM.configure(background="purple")
menuADM.resizable(width=False, height=False)
menuADM.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso
menuADM.iconbitmap("icons/bala.ico")

# Funções para abrir as telas de Produto, Fornecedor, Marca e Usuário no menuADM
def abrir_produto():
    menuADM.withdraw()  # Esconde o menu ADM
    subprocess.run(["python", "TelaProduto.py"])  # Executa o script TelaProduto.py
    menuADM.deiconify()  # Mostra a tela de produto

def abrir_usuarios():
    menuADM.withdraw()  # Esconde o menu ADM
    subprocess.run(["python","TelaCadastrarUsuario.py"])
    menuADM.deiconify()  # Mostra a tela de gerenciamento de usuários

def abrir_marca():
    menuADM.withdraw()  # Esconde o menu ADM
    subprocess.run(["python", "TelaMarca.py"])  # Executa o script TelaMarca.py
    menuADM.deiconify()  # Mostra a tela de marca

def abrir_fornecedor():
    menuADM.withdraw()  # Esconde o menu ADM
    subprocess.run(["python", "TelaFornecedor.py"])  # Executa o script TelaFornecedor.py
    menuADM.deiconify()  # Reexibe o menu ADM após fechar a tela de fornecedor

def sair():
    menuADM.withdraw()
    jan.deiconify()  # Volta para a tela de login

# Botões para abrir as telas no menuADM
produto_button = Button(menuADM, text="Produto", font=("Time New Roman", 15), command=abrir_produto)
produto_button.pack(pady=10)

usuario_button = Button(menuADM, text="Usuários", font=("Time New Roman", 15), command=abrir_usuarios)
usuario_button.pack(pady=10)

marca_button = Button(menuADM, text="Marca", font=("Time New Roman", 15), command=abrir_marca)
marca_button.pack(pady=10)

fornecedor_button = Button(menuADM, text="Fornecedor", font=("Time New Roman", 15), command=abrir_fornecedor)
fornecedor_button.pack(pady=10)

Button(menuADM, text="Sair", font=("Times New Roman", 15), command=sair).pack(pady=10)

# Criação da tela menuUsuario
menuUsuario = Toplevel()
menuUsuario.title("Doceria - Menu Usuário")
menuUsuario.geometry("400x200")
menuUsuario.configure(background="purple")
menuUsuario.resizable(width=False, height=False)
menuUsuario.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso
menuUsuario.iconbitmap("icons/bala.ico")

# Funções para abrir as telas de Produto e Minha Conta no menuUsuario
def abrir_produto_usuario():
    menuUsuario.withdraw()  # Esconde o menuUsuario
    subprocess.run(["python","TelaCadastrarUsuario.py"])
    menuUsuario.deiconify()  # Mostra a tela de produto

#def abrir_minha_conta():
  #  menuUsuario.withdraw()  # Esconde o menuUsuario
   # subprocess.run(["python", "TelaMinhaConta.py"])
   # menuUsuario.deiconify()  # Mostra a tela "Minha Conta"

def sair_usuario():
    menuUsuario.withdraw()  # Esconde o menuUsuario
    jan.deiconify()  # Volta para a tela de login

# Botões para abrir as telas no menuUsuario
produto_button_usuario = Button(menuUsuario, text="Produto", font=("Time New Roman", 15), command=abrir_produto_usuario)
produto_button_usuario.pack(pady=10)

#minha_conta_button = Button(menuUsuario, text="Minha Conta", font=("Time New Roman", 15), command=abrir_minha_conta)
#minha_conta_button.pack(pady=10)

Button(menuUsuario, text="Sair", font=("Times New Roman", 15), command=sair_usuario).pack(pady=20)

# Loop principal da interface
jan.mainloop()    

# Loop principal da interface
jan.mainloop()
