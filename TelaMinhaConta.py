from tkinter import Tk, Label, Button
from tkinter import messagebox
from DataBase import Database
import sys

# Verifica se há um parâmetro passado (login do usuário)
if len(sys.argv) < 2:
    messagebox.showerror("Erro", "Login do usuário não fornecido.")
    sys.exit()

login_usuario = sys.argv[1]

# Função para buscar informações do usuário no banco de dados
def obter_dados_usuario(login):
    db = Database()
    db.cursor.execute("""
        SELECT nm_usuario, end_usuario, tl_usuario, email_usuario, cpf_usuario, dat_nasc_usuario
        FROM tb_usuario
        WHERE login_usuario = %s
    """, (login,))
    return db.cursor.fetchone()

# Busca os dados do usuário
dados_usuario = obter_dados_usuario(login_usuario)

if not dados_usuario:
    messagebox.showerror("Erro", "Usuário não encontrado.")
    sys.exit()

# Extrai os dados do resultado da consulta
nm_usuario, end_usuario, tl_usuario, email_usuario, cpf_usuario, dat_nasc_usuario = dados_usuario

# Criação da Janela
janela_minha_conta = Tk()
janela_minha_conta.title("Doceria - Minha Conta")
janela_minha_conta.geometry("500x400")
janela_minha_conta.configure(background="purple")
janela_minha_conta.resizable(width=False, height=False)
janela_minha_conta.iconbitmap("icons/bala.ico")

# Widgets para exibir os dados do usuário
Label(janela_minha_conta, text="Minha Conta", font=("Arial", 24), bg="purple", fg="white").pack(pady=20)
Label(janela_minha_conta, text=f"Nome: {nm_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)
Label(janela_minha_conta, text=f"Endereço: {end_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)
Label(janela_minha_conta, text=f"Telefone: {tl_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)
Label(janela_minha_conta, text=f"Email: {email_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)
Label(janela_minha_conta, text=f"CPF: {cpf_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)
Label(janela_minha_conta, text=f"Data de Nascimento: {dat_nasc_usuario}", font=("Arial", 16), bg="purple", fg="white").pack(pady=5)

# Botão para fechar a janela
Button(janela_minha_conta, text="Fechar", font=("Arial", 15), command=janela_minha_conta.destroy).pack(pady=20)

# Loop Principal da Interface
janela_minha_conta.mainloop()
