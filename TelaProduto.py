from tkinter import *  # Importa todos os módulos do tkinter
from tkinter import messagebox  # Importa o módulo de caixa de texto do tkinter
from tkinter import ttk
from DataBase import Database  # Importa a classe Database do módulo DataBase

# Janela principal
jan = Tk()  # Cria uma instância da janela principal
jan.title("Painel Produto")  # Define um título para a janela
jan.geometry("300x150")  # Define o tamanho da janela
jan.configure(background="PURPLE")  # Configura a cor de fundo da janela
jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

# Frame para Produto
ProdutoFrame = Frame(jan, width=300, height=150, bg="PURPLE", relief="raise")  # Cria o frame principal
ProdutoFrame.pack()  # Posiciona o frame

# Adicionar campos para inserir produto
ProdutoLabel = Label(ProdutoFrame, text="Cod.Produto:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
# Label para o código do produto
ProdutoLabel.place(x=0, y=20)

ProdutoEntry = ttk.Entry(ProdutoFrame, width=10)  # Campo de entrada para o código do produto
ProdutoEntry.place(x=120, y=23)


# Função para buscar produto no banco de dados

def CadastrarProduto():
    CadastroFrame = Toplevel(jan)  # Cria uma nova janela
    CadastroFrame.title("Cadastrar Produto")
    CadastroFrame.geometry("400x400")  # Define o tamanho da nova janela
    CadastroFrame.configure(background="PURPLE")  # Configura a cor de fundo da janela
    CadastroFrame.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(CadastroFrame, text="Produto:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(CadastroFrame, width=30)
    NomeEntry.place(x=100, y=10)

    QtLabel = Label(CadastroFrame, text="Quantidade:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    QtLabel.place(x=5, y=50)
    QtEntry = ttk.Entry(CadastroFrame, width=10)
    QtEntry.place(x=100, y=50)

    VlLabel = Label(CadastroFrame, text="Valor(R$):", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    VlLabel.place(x=150, y=50)
    VlEntry = ttk.Entry(CadastroFrame, width=10)
    VlEntry.place(x=230, y=50)

    CategoriaLabel = Label(CadastroFrame, text="Categoria:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CategoriaLabel.place(x=5, y=95)
    CategoriaEntry = ttk.Entry(CadastroFrame, width=5)
    CategoriaEntry.place(x=100, y=95)

    MarcaLabel = Label(CadastroFrame, text="Marca:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    MarcaLabel.place(x=150, y=95)
    MarcaEntry = ttk.Entry(CadastroFrame, width=5)
    MarcaEntry.place(x=230, y=95)

    FornecedorLabel = Label(CadastroFrame, text="Fornecedor:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    FornecedorLabel.place(x=5, y=140)
    FornecedorEntry = ttk.Entry(CadastroFrame, width=5)
    FornecedorEntry.place(x=100, y=140)

    DescLabel = Label(CadastroFrame, text="Descrição:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    DescLabel.place(x=5, y=185)
    DescText = Text(CadastroFrame, width=30,  height=7, wrap=WORD)
    DescText.place(x=100, y=185)

    # Botão para salvar o cadastro
    def SalvarCadastro():
        nm_produto = NomeEntry.get()
        qt_produto = QtEntry.get()
        vl_produto = VlEntry.get()
        ds_produto = DescText.get(1.0, END).strip()
        id_categoria = CategoriaEntry.get()
        id_marca = MarcaEntry.get()
        id_fornecedor = FornecedorEntry.get()

        if not nm_produto or not qt_produto or not vl_produto or not id_categoria or not id_marca or not id_fornecedor or not ds_produto:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db = Database()
            query = """
            INSERT INTO tb_produto (nm_produto, qt_produto, vl_produto,ds_produto, id_categoria, id_marca,id_fornecedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (nm_produto, qt_produto, vl_produto, ds_produto, id_categoria, id_marca, id_fornecedor)
            db.cursor.execute(query, values)  # Executa a consulta com os valores
            db.conn.commit()  # Confirma as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso.")
            CadastroFrame.destroy()
            ProdutoFrame.pack()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")

    SalvarButton = ttk.Button(CadastroFrame, text="Cadastrar", width=10, command=SalvarCadastro)
    SalvarButton.place(x=80, y=350)

    VoltarButton = ttk.Button(CadastroFrame, text="Voltar", width=10, command=CadastroFrame.destroy)
    VoltarButton.place(x=320, y=350)
# Função para abrir a tela de alteração de dados do produto
def AlterarProduto():
    id_produto = ProdutoEntry.get()  # Obtém o valor do código do produto
    if not id_produto:
        messagebox.showwarning("Aviso", "Por favor, insira o código do produto para alterar.")
        return

    # Conectar ao banco de dados
    db = Database()
    db.cursor.execute("SELECT * FROM tb_produto WHERE id_produto = %s", (id_produto,))
    produto = db.cursor.fetchone()

    if not produto:
        messagebox.showwarning("Aviso", "Produto não encontrado.")
        return

    # Nova janela para alterar os dados
    AlterarJanela = Toplevel(jan)  # Cria uma nova janela
    AlterarJanela.title("Alterar Produto")
    AlterarJanela.geometry("400x400")  # Define o tamanho da nova janela
    AlterarJanela.configure(background="PURPLE")  # Configura a cor de fundo da janela
    AlterarJanela.resizable(width=False, height=False)  # Impede que a janela seja redimensionada

    NomeLabel = Label(AlterarJanela, text="Produto:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(AlterarJanela, width=30)
    NomeEntry.place(x=100, y=10)
    NomeEntry.insert(0, produto[1])  # Preenche o campo com o nome

    QtLabel = Label(AlterarJanela, text="Quantidade:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    QtLabel.place(x=5, y=50)
    QtEntry = ttk.Entry(AlterarJanela, width=10)
    QtEntry.place(x=100, y=50)
    QtEntry.insert(0, produto[2])

    VlLabel = Label(AlterarJanela, text="Valor(R$):", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    VlLabel.place(x=150, y=50)
    VlEntry = ttk.Entry(AlterarJanela, width=10)
    VlEntry.place(x=230, y=50)
    VlEntry.insert(0, produto[3])

    CategoriaLabel = Label(AlterarJanela, text="Categoria:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CategoriaLabel.place(x=5, y=95)
    CategoriaEntry = ttk.Entry(AlterarJanela, width=5)
    CategoriaEntry.place(x=100, y=95)
    CategoriaEntry.insert(0, produto[5])

    MarcaLabel = Label(AlterarJanela, text="Marca:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    MarcaLabel.place(x=150, y=95)
    MarcaEntry = ttk.Entry(AlterarJanela, width=5)
    MarcaEntry.place(x=230, y=95)
    MarcaEntry.insert(0, produto[6])

    FornecedorLabel = Label(AlterarJanela, text="Fornecedor:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    FornecedorLabel.place(x=5, y=140)
    FornecedorEntry = ttk.Entry(AlterarJanela, width=5)
    FornecedorEntry.place(x=100, y=140)
    FornecedorEntry.insert(0, produto[7])

    DescLabel = Label(AlterarJanela, text="Descrição:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    DescLabel.place(x=5, y=185)
    DescText = Text(AlterarJanela, width=30,  height=7, wrap=WORD)
    DescText.place(x=100, y=185)
    DescText.insert(END, produto[4])   

    # Função para salvar as alterações no banco de dados
    def SalvarAlteracoes():
        nm_produto = NomeEntry.get()
        qt_produto = QtEntry.get()
        vl_produto = VlEntry.get()
        ds_produto = DescText.get("1.0", END).strip()  # Ajustado
        id_categoria = CategoriaEntry.get()
        id_marca = MarcaEntry.get()
        id_fornecedor = FornecedorEntry.get()

        if not nm_produto or not qt_produto or not vl_produto or not id_categoria or not id_marca or not id_fornecedor or not ds_produto:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            db.cursor.execute("""
                UPDATE tb_produto
                SET nm_produto = %s, qt_produto = %s, vl_produto = %s, id_categoria = %s, id_marca = %s, id_fornecedor = %s, ds_produto = %s
                WHERE id_produto = %s
            """, (nm_produto, qt_produto, vl_produto, id_categoria, id_marca, id_fornecedor, ds_produto, id_produto))
            db.conn.commit()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
            AlterarJanela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")

    def DeletarProduto():
        id_produto = ProdutoEntry.get()  # Obtém o valor do código do produto
        if not id_produto:
            messagebox.showwarning("Aviso", "Por favor, insira o código do produto para deletar.")
            return

        # Conectar ao banco de dados
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM tb_produto WHERE id_produto = %s", (id_produto,))
            produto = db.cursor.fetchone()

            if not produto:
                messagebox.showwarning("Aviso", "Produto não encontrado.")
                return

            # Confirmação para deletar
            confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o produto: {produto[1]}?")
            if confirm:
                db.cursor.execute("DELETE FROM tb_produto WHERE id_produto = %s", (id_produto,))
                db.conn.commit()  # Confirma a exclusão no banco de dados
                messagebox.showinfo("Sucesso", "Produto deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar produto: {e}")

    #Bortão que salva as alterações nos dados do produto
    SalvarButton = ttk.Button(AlterarJanela, text="Salvar Alterações", command=SalvarAlteracoes)
    SalvarButton.place(x=80, y=350)
    # Botão de deletar produto
    DeletarButton = ttk.Button(AlterarJanela, text="Deletar", width=10, command=DeletarProduto)
    DeletarButton.place(x=180, y=350)
    #Botão para retornar a tela de pesquisar produto
    VoltarButton = ttk.Button(AlterarJanela, text="Voltar", command=AlterarJanela.destroy)
    VoltarButton.place(x=320, y=350)




# Botões principais
BuscarButton = ttk.Button(ProdutoFrame, text="Buscar", width=6, command=AlterarProduto)  # Botão de buscar produto
BuscarButton.place(x=200, y=22)

CadastrarButton = ttk.Button(ProdutoFrame, text="Cadastrar", width=10, command=CadastrarProduto)  # Botão de cadastrar produto
CadastrarButton.place(x=120, y=60)

RetornarButton = ttk.Button(ProdutoFrame, text="Sair", width=8, command=jan.quit)  
# Botão para fechar a aplicação
RetornarButton.place(x=125, y=110)

# Loop principal
jan.mainloop()