from tkinter import *  # Importa todos os módulos do tkinter
from tkinter import messagebox  # Importa o módulo de caixa de texto do tkinter
from tkinter import ttk
from DataBase import Database  # Importa a classe Database do módulo DataBase

# Janela principal
jan = Tk()  # Cria uma instância da janela principal
jan.title("Painel Marca")  # Define um título para a janela
jan.geometry("300x150")  # Define o tamanho da janela
jan.configure(background="PURPLE")  # Configura a cor de fundo da janela
jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
jan.iconbitmap("icons/bala.ico")

# Frame para Fornecedor
MarcaFrame = Frame(jan, width=300, height=150, bg="PURPLE", relief="raise")  # Cria o frame principal
MarcaFrame.pack()  # Posiciona o frame

# Adicionar campos para inserir fornecedor
MarcaLabel = Label(
    MarcaFrame, text="Cod. Marca:", font=("Times New Roman", 12), bg="PURPLE", fg="White"
)  # Label para o código do fornecedor
MarcaLabel.place(x=0, y=20)

MarcaEntry = ttk.Entry(MarcaFrame, width=10)  # Campo de entrada para o código do fornecedor
MarcaEntry.place(x=120, y=23)


# Função para buscar fornecedor no banco de dados

def CadastrarMarca():
    CadastroFrame = Toplevel(jan)  # Cria uma nova janela
    CadastroFrame.title("Cadastrar Marca")
    CadastroFrame.geometry("400x400")  # Define o tamanho da nova janela
    CadastroFrame.configure(background="PURPLE")  # Configura a cor de fundo da janela
    CadastroFrame.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(CadastroFrame, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(CadastroFrame, width=30)
    NomeEntry.place(x=120, y=10)

    TelefoneLabel = Label(CadastroFrame, text="Contato:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelefoneLabel.place(x=5, y=50)

    TelefoneEntry = ttk.Entry(CadastroFrame, width=30)
    TelefoneEntry.place(x=120, y=50)


    # Botão para salvar o cadastro
    def SalvarCadastro():
        nm_marca = NomeEntry.get()
        telefone_marca = TelefoneEntry.get()

        if not nm_marca or not telefone_marca:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db = Database()
            query = """
            INSERT INTO tb_marca (nm_marca,tl_marca)
            VALUES (%s, %s)
            """
            values = (nm_marca, telefone_marca)
            db.cursor.execute(query, values)  # Executa a consulta com os valores
            db.conn.commit()  # Confirma as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Marca cadastrado com sucesso.")
            CadastroFrame.destroy()
            MarcaFrame.pack()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar marca: {e}")

    SalvarButton = ttk.Button(CadastroFrame, text="Cadastrar", width=10, command=SalvarCadastro)
    SalvarButton.place(x=150, y=240)

    VoltarButton = ttk.Button(CadastroFrame, text="Voltar", width=10, command=CadastroFrame.destroy)
    VoltarButton.place(x=150, y=275)
# Função para abrir a tela de alteração de dados do fornecedor
def AlterarMarca():
    id_marca = MarcaEntry.get()  # Obtém o valor do código do fornecedor
    if not id_marca:
        messagebox.showwarning("Aviso", "Por favor, insira o código do marca para alterar.")
        return

    # Conectar ao banco de dados
    db = Database()
    db.cursor.execute("SELECT * FROM tb_marca WHERE id_marca = %s", (id_marca,))
    marca = db.cursor.fetchone()

    if not marca:
        messagebox.showwarning("Aviso", "Marca não encontrado.")
        return

    # Nova janela para alterar os dados
    AlterarJanela = Toplevel(jan)  # Cria uma nova janela
    AlterarJanela.title("Alterar Marca")
    AlterarJanela.geometry("400x400")  # Define o tamanho da nova janela
    AlterarJanela.configure(background="PURPLE")  # Configura a cor de fundo da janela
    AlterarJanela.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(AlterarJanela, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=20, y=20)
    NomeEntry = ttk.Entry(AlterarJanela, width=30)
    NomeEntry.place(x=100, y=20)
    NomeEntry.insert(0, marca[1])  # Preenche o campo com o nome do fornecedor

    TelefoneLabel = Label(AlterarJanela, text="Telefone:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelefoneLabel.place(x=20, y=60)
    TelefoneEntry = ttk.Entry(AlterarJanela, width=30)
    TelefoneEntry.place(x=100, y=60)
    TelefoneEntry.insert(0, marca[2])  # Preenche o campo com o CNPJ


    # Função para salvar as alterações no banco de dados
    def SalvarAlteracoes():
        nm_marca = NomeEntry.get()
        telefone_marca = TelefoneEntry.get()

        if not nm_marca or not telefone_marca:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db.cursor.execute("""
                UPDATE tb_marca
                SET nm_marca = %s, tl_marca = %s
                WHERE id_marca = %s
            """, (nm_marca,telefone_marca))
            db.conn.commit()  # Confirma as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Marca atualizada com sucesso.")
            AlterarJanela.destroy()  # Fecha a janela de alteração
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar marca: {e}")

    def DeletarMarca():
        id_marca = MarcaEntry.get()  # Obtém o valor do código do fornecedor
        if not id_marca:
            messagebox.showwarning("Aviso", "Por favor, insira o código da marca para deletar.")
            return

        # Conectar ao banco de dados
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM tb_marca WHERE id_marca = %s", (id_marca,))
            marca = db.cursor.fetchone()

            if not marca:
                messagebox.showwarning("Aviso", "Marca não encontrado.")
                return

            # Confirmação para deletar
            confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o fornecedor: {marca[1]}?")
            if confirm:
                db.cursor.execute("DELETE FROM tb_marca WHERE id_marca = %s", (id_marca,))
                db.conn.commit()  # Confirma a exclusão no banco de dados
                messagebox.showinfo("Sucesso", "Marca deletada com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar marca: {e}")

    #Bortão que salva as alterações nos dados do fornecedor
    SalvarButton = ttk.Button(AlterarJanela, text="Salvar Alterações", command=SalvarAlteracoes)
    SalvarButton.place(x=80, y=220)
    # Botão de deletar fornecedor
    DeletarButton = ttk.Button(AlterarJanela, text="Deletar", width=10, command=DeletarMarca)
    DeletarButton.place(x=180, y=220)
    #Botão para retornar a tela de pesquisar fornecedor
    VoltarButton = ttk.Button(AlterarJanela, text="Voltar", command=AlterarJanela.destroy)
    VoltarButton.place(x=320, y=350)




# Botões principais
BuscarButton = ttk.Button(MarcaFrame, text="Buscar", width=6, command=AlterarMarca)  # Botão de buscar fornecedor
BuscarButton.place(x=200, y=22)

CadastrarButton = ttk.Button(MarcaFrame, text="Cadastrar", width=10, command=CadastrarMarca)  # Botão de cadastrar fornecedor
CadastrarButton.place(x=120, y=60)

RetornarButton = ttk.Button(
    MarcaFrame, text="Sair", width=8, command=jan.quit
)  # Botão para fechar a aplicação
RetornarButton.place(x=125, y=110)

# Loop principal
jan.mainloop()