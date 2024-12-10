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
menuADM.geometry("500x400")
menuADM.configure(background="purple")
menuADM.resizable(width=False, height=False)
menuADM.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso


# Criação da tela menuUsuario
menuUsuario = Toplevel()
menuUsuario.title("Doceria - Menu Usuário")
menuUsuario.geometry("500x400")
menuUsuario.configure(background="purple")
menuUsuario.resizable(width=False, height=False)
menuUsuario.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso

# Funções para abrir as telas de Produto, Fornecedor, Marca e Usuário no menuADM
def abrir_produto():
    menuADM.withdraw()  # Esconde o menu ADM
    menuProduto.deiconify()  # Mostra a tela de produto

def abrir_usuarios():
    menuADM.withdraw()  # Esconde o menu ADM
    menuUsuarios.deiconify()  # Mostra a tela de gerenciamento de usuários

def abrir_marca():
    menuADM.withdraw()  # Esconde o menu ADM
    menuMarca.deiconify()  # Mostra a tela de marca

def abrir_fornecedor():
    menuADM.withdraw()  # Esconde o menu ADM
    menuFornecedor.deiconify()  # Mostra a tela de fornecedor

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

Button(menuADM, text="Sair", font=("Times New Roman", 15), command=sair).pack(pady=20)

# Função para voltar ao menu ADM a partir da tela de Produto
def voltar_produto():
    menuProduto.withdraw()
    menuADM.deiconify()

# Criação da tela Produto
menuProduto = Toplevel()
menuProduto.title("Doceria - Produto")
menuProduto.geometry("500x400")
menuProduto.configure(background="purple")
menuProduto.resizable(width=False, height=False)
menuProduto.withdraw()  # Mantém a tela oculta até o botão "Produto" ser clicado

label_produto = Label(menuProduto, text="Tela de Produto", font=("Arial", 20), bg="purple", fg="white")
label_produto.pack(pady=50)

# Botão para voltar ao menu ADM
botao_voltar_produto = Button(menuProduto, text="Voltar", font=("Arial", 15), command=voltar_produto)
botao_voltar_produto.pack(pady=20)

# Função para voltar ao menu ADM a partir da tela de Fornecedor
def voltar_fornecedor():
    menuFornecedor.withdraw()
    menuADM.deiconify()

# Criação da tela Fornecedor
menuFornecedor = Toplevel()
menuFornecedor.title("Doceria - Fornecedor")
menuFornecedor.geometry("500x400")
menuFornecedor.configure(background="purple")
menuFornecedor.resizable(width=False, height=False)
menuFornecedor.withdraw()  # Mantém a tela oculta até o botão "Fornecedor" ser clicado

label_fornecedor = Label(menuFornecedor, text="Tela de Fornecedor", font=("Arial", 20), bg="purple", fg="white")
label_fornecedor.pack(pady=50)

# Botão para voltar ao menu ADM
botao_voltar_fornecedor = Button(menuFornecedor, text="Voltar", font=("Arial", 15), command=voltar_fornecedor)
botao_voltar_fornecedor.pack(pady=20)

# Função para voltar ao menu ADM a partir da tela de Marca
def voltar_marca():
    menuMarca.withdraw()
    menuADM.deiconify()

# Criação da tela Marca
menuMarca = Toplevel()
menuMarca.title("Doceria - Marca")
menuMarca.geometry("500x400")
menuMarca.configure(background="purple")
menuMarca.resizable(width=False, height=False)
menuMarca.withdraw()  # Mantém a tela oculta até o botão "Marca" ser clicado

label_marca = Label(menuMarca, text="Tela de Marca", font=("Arial", 20), bg="purple", fg="white")
label_marca.pack(pady=50)

# Botão para voltar ao menu ADM
botao_voltar_marca = Button(menuMarca, text="Voltar", font=("Arial", 15), command=voltar_marca)
botao_voltar_marca.pack(pady=20)

# Função para voltar ao menu ADM a partir da tela de Gerenciamento de Usuários
def voltar_usuarios():
    menuUsuarios.withdraw()
    menuADM.deiconify()

# Criação da tela de Gerenciamento de Usuários
menuUsuarios = Toplevel()
menuUsuarios.title("Doceria - Gerenciamento de Usuários")
menuUsuarios.geometry("500x400")
menuUsuarios.configure(background="purple")
menuUsuarios.resizable(width=False, height=False)
menuUsuarios.withdraw()  # Mantém a tela oculta até o botão "Gerenciar Usuários" ser clicado

label_usuarios = Label(menuUsuarios, text="Tela de Gerenciamento de Usuários", font=("Arial", 20), bg="purple", fg="white")
label_usuarios.pack(pady=50)

# Botão para voltar ao menu ADM
botao_voltar_usuarios = Button(menuUsuarios, text="Voltar", font=("Arial", 15), command=voltar_marca)
botao_voltar_usuarios.pack(pady=20)

    
# Criação da tela menuUsuario
menuUsuario = Toplevel()
menuUsuario.title("Doceria - Menu Usuário")
menuUsuario.geometry("500x400")
menuUsuario.configure(background="purple")
menuUsuario.resizable(width=False, height=False)
menuUsuario.withdraw()  # Mantém a tela oculta até o login ser realizado com sucesso

# Funções para abrir as telas de Produto e Minha Conta no menuUsuario
def abrir_produto_usuario():
    menuUsuario.withdraw()  # Esconde o menuUsuario
    menuProduto.deiconify()  # Mostra a tela de produto

def abrir_minha_conta():
    menuUsuario.withdraw()  # Esconde o menuUsuario
    menuMinhaConta.deiconify()  # Mostra a tela "Minha Conta"

def sair_usuario():
    menuUsuario.withdraw()  # Esconde o menuUsuario
    jan.deiconify()  # Volta para a tela de login

# Botões para abrir as telas no menuUsuario
produto_button_usuario = Button(menuUsuario, text="Produto", font=("Time New Roman", 15), command=abrir_produto_usuario)
produto_button_usuario.pack(pady=10)

minha_conta_button = Button(menuUsuario, text="Minha Conta", font=("Time New Roman", 15), command=abrir_minha_conta)
minha_conta_button.pack(pady=10)

Button(menuUsuario, text="Sair", font=("Times New Roman", 15), command=sair_usuario).pack(pady=20)

# Função para voltar ao menuUsuario a partir da tela Produto
def voltar_produto_usuario():
    menuProduto.withdraw()
    menuUsuario.deiconify()

# Criação da tela Produto
menuProduto_usuario = Toplevel()
menuProduto_usuario.title("Doceria - Produto")
menuProduto_usuario.geometry("500x400")
menuProduto_usuario.configure(background="purple")
menuProduto_usuario.resizable(width=False, height=False)
menuProduto_usuario.withdraw()  # Mantém a tela oculta até o botão "Produto" ser clicado

label_produto = Label(menuProduto_usuario, text="Tela de Produto", font=("Arial", 20), bg="purple", fg="white")
label_produto.pack(pady=50)

# Botão para voltar ao menuUsuario
botao_voltar_produto = Button(menuProduto_usuario, text="Voltar", font=("Arial", 15), command=voltar_produto_usuario)
botao_voltar_produto.pack(pady=20)

# Função para voltar ao menuUsuario a partir da tela "Minha Conta"
def voltar_minha_conta():
    menuMinhaConta.withdraw()
    menuUsuario.deiconify()

# Criação da tela "Minha Conta"
menuMinhaConta = Toplevel()
menuMinhaConta.title("Doceria - Minha Conta")
menuMinhaConta.geometry("500x400")
menuMinhaConta.configure(background="purple")
menuMinhaConta.resizable(width=False, height=False)
menuMinhaConta.withdraw()  # Mantém a tela oculta até o botão "Minha Conta" ser clicado

label_minha_conta = Label(menuMinhaConta, text="Tela de Minha Conta", font=("Arial", 20), bg="purple", fg="white")
label_minha_conta.pack(pady=50)

# Botão para voltar ao menuUsuario
botao_voltar_minha_conta = Button(menuMinhaConta, text="Voltar", font=("Arial", 15), command=voltar_minha_conta)
botao_voltar_minha_conta.pack(pady=20)

# Loop principal da interface
jan.mainloop()    

# Loop principal da interface
jan.mainloop()
