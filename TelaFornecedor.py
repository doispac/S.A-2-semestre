from tkinter import *  # Importa todos os módulos do tkinter
from tkinter import messagebox  # Importa o módulo de caixa de texto do tkinter
from tkinter import ttk
from DataBase import Database  # Importa a classe Database do módulo DataBase

# Janela principal
jan = Tk()  # Cria uma instância da janela principal
jan.title("Painel Fornecedor")  # Define um título para a janela
jan.geometry("300x150")  # Define o tamanho da janela
jan.configure(background="PURPLE")  # Configura a cor de fundo da janela
jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

# Frame para Fornecedor
FornecedorFrame = Frame(jan, width=300, height=150, bg="PURPLE", relief="raise")  # Cria o frame principal
FornecedorFrame.pack()  # Posiciona o frame

# Adicionar campos para inserir fornecedor
FornecedorLabel = Label(
    FornecedorFrame, text="Cod. Fornecedor:", font=("Times New Roman", 12), bg="PURPLE", fg="White"
)  # Label para o código do fornecedor
FornecedorLabel.place(x=0, y=20)

FornecedorEntry = ttk.Entry(FornecedorFrame, width=10)  # Campo de entrada para o código do fornecedor
FornecedorEntry.place(x=120, y=23)


# Função para buscar fornecedor no banco de dados

def CadastrarFornecedor():
    CadastroFrame = Toplevel(jan)  # Cria uma nova janela
    CadastroFrame.title("Cadastrar Fornecedor")
    CadastroFrame.geometry("400x400")  # Define o tamanho da nova janela
    CadastroFrame.configure(background="PURPLE")  # Configura a cor de fundo da janela
    CadastroFrame.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(CadastroFrame, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(CadastroFrame, width=30)
    NomeEntry.place(x=120, y=10)

    CnpjLabel = Label(CadastroFrame, text="CNPJ:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CnpjLabel.place(x=5, y=50)

    CnpjEntry = ttk.Entry(CadastroFrame, width=30)
    CnpjEntry.place(x=120, y=50)

    EndrLabel = Label(CadastroFrame, text="Endereço:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EndrLabel.place(x=5, y=95)

    EndrEntry = ttk.Entry(CadastroFrame, width=30)
    EndrEntry.place(x=120, y=95)

    TelLabel = Label(CadastroFrame, text="Telefone:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelLabel.place(x=5, y=140)

    TelEntry = ttk.Entry(CadastroFrame, width=30)
    TelEntry.place(x=120, y=140)

    EmailLabel = Label(CadastroFrame, text="Email:", font=("Times New Roman", 15), bg="PURPLE", fg="White")
    EmailLabel.place(x=5, y=185)

    EmailEntry = ttk.Entry(CadastroFrame, width=30)
    EmailEntry.place(x=120, y=185)

    # Botão para salvar o cadastro
    def SalvarCadastro():
        nm_fornecedor = NomeEntry.get()
        cnpj_fornecedor = CnpjEntry.get()
        end_fornecedor = EndrEntry.get()
        tl_fornecedor = TelEntry.get()
        email_fornecedor = EmailEntry.get()

        if not nm_fornecedor or not cnpj_fornecedor or not end_fornecedor or not tl_fornecedor or not email_fornecedor:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db = Database()
            query = """
            INSERT INTO tb_fornecedor (nm_fornecedor, cnpj_fornecedor, end_fornecedor, tl_fornecedor, email_fornecedor)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (nm_fornecedor, cnpj_fornecedor, end_fornecedor, tl_fornecedor, email_fornecedor)
            db.cursor.execute(query, values)  # Executa a consulta com os valores
            db.conn.commit()  # Confirma as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso.")
            CadastroFrame.destroy()
            FornecedorFrame.pack()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar fornecedor: {e}")

    SalvarButton = ttk.Button(CadastroFrame, text="Cadastrar", width=10, command=SalvarCadastro)
    SalvarButton.place(x=150, y=240)

    VoltarButton = ttk.Button(CadastroFrame, text="Voltar", width=10, command=CadastroFrame.destroy)
    VoltarButton.place(x=150, y=275)
# Função para abrir a tela de alteração de dados do fornecedor
def AlterarFornecedor():
    id_fornecedor = FornecedorEntry.get()  # Obtém o valor do código do fornecedor
    if not id_fornecedor:
        messagebox.showwarning("Aviso", "Por favor, insira o código do fornecedor para alterar.")
        return

    # Conectar ao banco de dados
    db = Database()
    db.cursor.execute("SELECT * FROM tb_fornecedor WHERE id_fornecedor = %s", (id_fornecedor,))
    fornecedor = db.cursor.fetchone()

    if not fornecedor:
        messagebox.showwarning("Aviso", "Fornecedor não encontrado.")
        return

    # Nova janela para alterar os dados
    AlterarJanela = Toplevel(jan)  # Cria uma nova janela
    AlterarJanela.title("Alterar Fornecedor")
    AlterarJanela.geometry("400x400")  # Define o tamanho da nova janela
    AlterarJanela.configure(background="PURPLE")  # Configura a cor de fundo da janela
    AlterarJanela.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(AlterarJanela, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=20, y=20)
    NomeEntry = ttk.Entry(AlterarJanela, width=30)
    NomeEntry.place(x=100, y=20)
    NomeEntry.insert(0, fornecedor[1])  # Preenche o campo com o nome do fornecedor

    CnpjLabel = Label(AlterarJanela, text="CNPJ:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CnpjLabel.place(x=20, y=60)
    CnpjEntry = ttk.Entry(AlterarJanela, width=30)
    CnpjEntry.place(x=100, y=60)
    CnpjEntry.insert(0, fornecedor[2])  # Preenche o campo com o CNPJ

    EndrLabel = Label(AlterarJanela, text="Endereço:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EndrLabel.place(x=20, y=100)
    EndrEntry = ttk.Entry(AlterarJanela, width=30)
    EndrEntry.place(x=100, y=100)
    EndrEntry.insert(0, fornecedor[3])  # Preenche o campo com o endereço

    TelLabel = Label(AlterarJanela, text="Telefone:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelLabel.place(x=20, y=140)
    TelEntry = ttk.Entry(AlterarJanela, width=30)
    TelEntry.place(x=100, y=140)
    TelEntry.insert(0, fornecedor[4])  # Preenche o campo com o telefone

    EmailLabel = Label(AlterarJanela, text="Email:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EmailLabel.place(x=20, y=180)
    EmailEntry = ttk.Entry(AlterarJanela, width=30)
    EmailEntry.place(x=100, y=180)
    EmailEntry.insert(0, fornecedor[5])  # Preenche o campo com o email
    

    # Função para salvar as alterações no banco de dados
    def SalvarAlteracoes():
        nm_fornecedor = NomeEntry.get()
        cnpj_fornecedor = CnpjEntry.get()
        end_fornecedor = EndrEntry.get()
        tl_fornecedor = TelEntry.get()
        email_fornecedor = EmailEntry.get()

        if not nm_fornecedor or not cnpj_fornecedor or not end_fornecedor or not tl_fornecedor or not email_fornecedor:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db.cursor.execute("""
                UPDATE tb_fornecedor
                SET nm_fornecedor = %s, cnpj_fornecedor = %s, end_fornecedor = %s, tl_fornecedor = %s, email_fornecedor = %s
                WHERE id_fornecedor = %s
            """, (nm_fornecedor, cnpj_fornecedor, end_fornecedor, tl_fornecedor, email_fornecedor, id_fornecedor))
            db.conn.commit()  # Confirma as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso.")
            AlterarJanela.destroy()  # Fecha a janela de alteração
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar fornecedor: {e}")

    def DeletarFornecedor():
        id_fornecedor = FornecedorEntry.get()  # Obtém o valor do código do fornecedor
        if not id_fornecedor:
            messagebox.showwarning("Aviso", "Por favor, insira o código do fornecedor para deletar.")
            return

        # Conectar ao banco de dados
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM tb_fornecedor WHERE id_fornecedor = %s", (id_fornecedor,))
            fornecedor = db.cursor.fetchone()

            if not fornecedor:
                messagebox.showwarning("Aviso", "Fornecedor não encontrado.")
                return

            # Confirmação para deletar
            confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o fornecedor: {fornecedor[1]}?")
            if confirm:
                db.cursor.execute("DELETE FROM tb_fornecedor WHERE id_fornecedor = %s", (id_fornecedor,))
                db.conn.commit()  # Confirma a exclusão no banco de dados
                messagebox.showinfo("Sucesso", "Fornecedor deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar fornecedor: {e}")

    #Bortão que salva as alterações nos dados do fornecedor
    SalvarButton = ttk.Button(AlterarJanela, text="Salvar Alterações", command=SalvarAlteracoes)
    SalvarButton.place(x=80, y=220)
    # Botão de deletar fornecedor
    DeletarButton = ttk.Button(AlterarJanela, text="Deletar", width=10, command=DeletarFornecedor)
    DeletarButton.place(x=180, y=220)
    #Botão para retornar a tela de pesquisar fornecedor
    VoltarButton = ttk.Button(AlterarJanela, text="Voltar", command=AlterarJanela.destroy)
    VoltarButton.place(x=320, y=350)




# Botões principais
BuscarButton = ttk.Button(FornecedorFrame, text="Buscar", width=6, command=AlterarFornecedor)  # Botão de buscar fornecedor
BuscarButton.place(x=200, y=22)

CadastrarButton = ttk.Button(FornecedorFrame, text="Cadastrar", width=10, command=CadastrarFornecedor)  # Botão de cadastrar fornecedor
CadastrarButton.place(x=120, y=60)

RetornarButton = ttk.Button(
    FornecedorFrame, text="Sair", width=8, command=jan.quit
)  # Botão para fechar a aplicação
RetornarButton.place(x=125, y=110)

# Loop principal
jan.mainloop()