from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database  # Importa a classe `Database` para conexão com o banco de dados

# Cria a janela principal da aplicação
jan = Tk()
jan.title("Painel de Usuários")  # Define o título da janela
jan.geometry("300x200")  # Define o tamanho da janela
jan.configure(background="PURPLE")  # Define a cor de fundo da janela
jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
jan.iconbitmap("icons/bala.ico")

# Cria o frame principal da aplicação
UsuarioFrame = Frame(jan, width=300, height=200, bg="PURPLE", relief="raise")
UsuarioFrame.pack()  # Adiciona o frame à janela principal

# Adiciona um rótulo para o campo de entrada de ID do usuário
UsuarioLabel = Label(UsuarioFrame, text="ID Usuário:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
UsuarioLabel.place(x=10, y=20)  # Posiciona o rótulo no frame

# Adiciona um campo de entrada para o ID do usuário
UsuarioEntry = ttk.Entry(UsuarioFrame, width=10)
UsuarioEntry.place(x=120, y=23)  # Posiciona o campo de entrada no frame

# Função para abrir a tela de cadastro de usuário
def CadastrarUsuario():
    CadastroFrame = Toplevel(jan)  # Cria uma nova janela como uma instância de Toplevel
    CadastroFrame.title("Cadastrar Usuário")  # Define o título da nova janela
    CadastroFrame.geometry("400x400")  # Define o tamanho da nova janela
    CadastroFrame.configure(background="PURPLE")  # Configura a cor de fundo da nova janela
    CadastroFrame.resizable(width=False, height=False)  # Impede que a nova janela seja redimensionada

    # Rótulo e campo de entrada para o nome do usuário
    NomeLabel = Label(CadastroFrame, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(CadastroFrame, width=30)
    NomeEntry.place(x=150, y=10)

    # Rótulo e campo de entrada para o endereço do usuário
    EnderecoLabel = Label(CadastroFrame, text="Endereço:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EnderecoLabel.place(x=5, y=40)
    EnderecoEntry = ttk.Entry(CadastroFrame, width=30)
    EnderecoEntry.place(x=150, y=40)

    # Rótulo e campo de entrada para o telefone do usuário
    TelefoneLabel = Label(CadastroFrame, text="Telefone:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelefoneLabel.place(x=5, y=70)
    TelefoneEntry = ttk.Entry(CadastroFrame, width=20)
    TelefoneEntry.place(x=150, y=70)

    # Rótulo e campo de entrada para o e-mail do usuário
    EmailLabel = Label(CadastroFrame, text="E-mail:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EmailLabel.place(x=5, y=100)
    EmailEntry = ttk.Entry(CadastroFrame, width=30)
    EmailEntry.place(x=150, y=100)

    # Rótulo e campo de entrada para o CPF do usuário
    CPFLabel = Label(CadastroFrame, text="CPF:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CPFLabel.place(x=5, y=130)
    CPFEntry = ttk.Entry(CadastroFrame, width=20)
    CPFEntry.place(x=150, y=130)

    # Rótulo e campo de entrada para a data de nascimento do usuário
    DataNascLabel = Label(CadastroFrame, text="Data Nascimento:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    DataNascLabel.place(x=5, y=160)
    DataNascEntry = ttk.Entry(CadastroFrame, width=20)
    DataNascEntry.place(x=150, y=160)

    # Rótulo e campo de entrada para o login do usuário
    LoginLabel = Label(CadastroFrame, text="Login:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    LoginLabel.place(x=5, y=190)
    LoginEntry = ttk.Entry(CadastroFrame, width=20)
    LoginEntry.place(x=150, y=190)

    # Rótulo e campo de entrada para a senha do usuário
    SenhaLabel = Label(CadastroFrame, text="Senha:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    SenhaLabel.place(x=5, y=220)
    SenhaEntry = ttk.Entry(CadastroFrame, width=20, show="*")  # `show="*"` oculta os caracteres digitados
    SenhaEntry.place(x=150, y=220)

    # Botões de tipo de usuário
    # Define botões de rádio para selecionar o tipo de usuário (ADM ou Padrão)
    tipo_usuario = IntVar()  # Variável para armazenar o valor do tipo selecionado
    Radiobutton(CadastroFrame, text="ADM", variable=tipo_usuario, value=1, bg="PURPLE", fg="White").place(x=10, y=250)
    Radiobutton(CadastroFrame, text="Padrão", variable=tipo_usuario, value=2, bg="PURPLE", fg="White").place(x=100, y=250)

    # Função para salvar o cadastro do usuário
    def SalvarUsuario():
        # Obtém os valores dos campos de entrada
        nm_usuario = NomeEntry.get()
        end_usuario = EnderecoEntry.get()
        tl_usuario = TelefoneEntry.get()
        email_usuario = EmailEntry.get()
        cpf_usuario = CPFEntry.get()
        dat_nasc_usuario = DataNascEntry.get()
        login_usuario = LoginEntry.get()
        senha_usuario = SenhaEntry.get()
        id_tip = tipo_usuario.get()  # Obtém o valor selecionado no botão de rádio

        # Validação: verifica se todos os campos foram preenchidos
        if not nm_usuario or not end_usuario or not tl_usuario or not email_usuario or not cpf_usuario or not dat_nasc_usuario or not login_usuario or not senha_usuario or id_tip == 0:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")  # Exibe um aviso
            return

        try:
            # Cria uma instância de conexão com o banco de dados
            db = Database()
            # Query SQL para inserir os dados do usuário
            query = """
            INSERT INTO tb_usuario (nm_usuario, end_usuario, tl_usuario, email_usuario, cpf_usuario, dat_nasc_usuario, login_usuario, senha_usuario, id_tip)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Valores a serem inseridos na tabela
            values = (nm_usuario, end_usuario, tl_usuario, email_usuario, cpf_usuario, dat_nasc_usuario, login_usuario, senha_usuario, id_tip)
            db.cursor.execute(query, values)  # Executa a consulta com os valores fornecidos
            db.conn.commit()  # Confirma as alterações no banco de dados
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")  # Exibe uma mensagem de sucesso
            CadastroFrame.destroy()  # Fecha a janela de cadastro
        except Exception as e:
            # Exibe uma mensagem de erro caso algo dê errado
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    # Botão para salvar o usuário
    SalvarButton = ttk.Button(CadastroFrame, text="Cadastrar", width=10, command=SalvarUsuario)
    SalvarButton.place(x=80, y=350)

    # Botão para voltar à tela anterior
    VoltarButton = ttk.Button(CadastroFrame, text="Voltar", width=10, command=CadastroFrame.destroy)
    VoltarButton.place(x=250, y=350)


# Função para buscar usuário e abrir a tela de alteração ou exclusão
def AlterarOuExcluirUsuario():
    # Obtém o ID do usuário digitado
    id_usuario = UsuarioEntry.get()
    if not id_usuario:  # Valida se o campo está vazio
        messagebox.showwarning("Aviso", "Por favor, insira o ID do usuário.")  # Exibe um aviso
        return

    # Cria uma conexão com o banco de dados e busca o usuário pelo ID
    db = Database()
    db.cursor.execute("SELECT * FROM tb_usuario WHERE id_usuario = %s", (id_usuario,))
    usuario = db.cursor.fetchone()  # Obtém os dados do usuário

    if not usuario:  # Verifica se o usuário foi encontrado
        messagebox.showwarning("Aviso", "Usuário não encontrado.")  # Exibe um aviso
        return

    # Cria uma nova janela para alterar ou excluir o usuário
    AlterarJanela = Toplevel(jan) #criar uma nova janela secundária
    AlterarJanela.title("Alterar/Excluir Usuário")  # Define o título da janela
    AlterarJanela.geometry("400x400")  # Define o tamanho da janela
    AlterarJanela.configure(background="PURPLE")  # Configura a cor de fundo
    AlterarJanela.resizable(width=False, height=False)  # Impede redimensionamento

    # Campos para exibir e editar os dados do usuário
    # Campo Nome
    NomeLabel = Label(AlterarJanela, text="Nome:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(AlterarJanela, width=30)
    NomeEntry.place(x=150, y=10)
    NomeEntry.insert(0, usuario[1])  # Preenche com o valor atual do banco

    # Campo Endereço
    EnderecoLabel = Label(AlterarJanela, text="Endereço:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EnderecoLabel.place(x=5, y=40)
    EnderecoEntry = ttk.Entry(AlterarJanela, width=30)
    EnderecoEntry.place(x=150, y=40)
    EnderecoEntry.insert(0, usuario[2])

    # Campo Telefone
    TelefoneLabel = Label(AlterarJanela, text="Telefone:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    TelefoneLabel.place(x=5, y=70)
    TelefoneEntry = ttk.Entry(AlterarJanela, width=30)
    TelefoneEntry.place(x=150, y=70)
    TelefoneEntry.insert(0, usuario[3])

    # Campo E-mail
    EmailLabel = Label(AlterarJanela, text="E-mail:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    EmailLabel.place(x=5, y=100)
    EmailEntry = ttk.Entry(AlterarJanela, width=30)
    EmailEntry.place(x=150, y=100)
    EmailEntry.insert(0, usuario[4])

    # Campo CPF
    CPFLabel = Label(AlterarJanela, text="CPF:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    CPFLabel.place(x=5, y=130)
    CPFEntry = ttk.Entry(AlterarJanela, width=30)
    CPFEntry.place(x=150, y=130)
    CPFEntry.insert(0, usuario[5])

    # Campo Data de Nascimento
    DataNascLabel = Label(AlterarJanela, text="Data Nascimento:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    DataNascLabel.place(x=5, y=160)
    DataNascEntry = ttk.Entry(AlterarJanela, width=30)
    DataNascEntry.place(x=150, y=160)
    DataNascEntry.insert(0, usuario[6])

    # Campo Login
    LoginLabel = Label(AlterarJanela, text="Login:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    LoginLabel.place(x=5, y=190)
    LoginEntry = ttk.Entry(AlterarJanela, width=30)
    LoginEntry.place(x=150, y=190)
    LoginEntry.insert(0, usuario[7])

    # Campo Senha
    SenhaLabel = Label(AlterarJanela, text="Senha:", font=("Times New Roman", 12), bg="PURPLE", fg="White")
    SenhaLabel.place(x=5, y=220)
    SenhaEntry = ttk.Entry(AlterarJanela, width=30, show="*")  # Oculta os caracteres digitados
    SenhaEntry.place(x=150, y=220)
    SenhaEntry.insert(0, usuario[8])

    # Variável que armazenará o tipo de usuário (1 para ADM e 2 para Padrão), com valor inicial vindo do banco de dados
    tipo_usuario = IntVar(value=usuario[9])  

    # Criação de botões de seleção (radio buttons) para escolher o tipo de usuário
    Radiobutton(AlterarJanela, text="ADM", variable=tipo_usuario, value=1, bg="PURPLE", fg="White").place(x=10, y=250)
    Radiobutton(AlterarJanela, text="Padrão", variable=tipo_usuario, value=2, bg="PURPLE", fg="White").place(x=100, y=250)

    # Função que salva as alterações realizadas no cadastro do usuário
    def SalvarAlteracoes():
        # Obtendo os valores inseridos nos campos de entrada
        nm_usuario = NomeEntry.get()
        end_usuario = EnderecoEntry.get()
        tl_usuario = TelefoneEntry.get()
        email_usuario = EmailEntry.get()
        cpf_usuario = CPFEntry.get()
        dat_nasc_usuario = DataNascEntry.get()
        login_usuario = LoginEntry.get()
        senha_usuario = SenhaEntry.get()
        id_tip = tipo_usuario.get()  # Obtém o tipo de usuário selecionado (1 ou 2)

        # Verifica se todos os campos estão preenchidos
        if not nm_usuario or not end_usuario or not tl_usuario or not email_usuario or not cpf_usuario or not dat_nasc_usuario or not login_usuario or not senha_usuario or id_tip == 0:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")  # Alerta caso algum campo esteja vazio
            return

        # Tenta atualizar os dados do usuário no banco de dados
        try:
            query = """
                UPDATE tb_usuario
                SET nm_usuario = %s, end_usuario = %s, tl_usuario = %s, email_usuario = %s, cpf_usuario = %s, dat_nasc_usuario = %s, login_usuario = %s, senha_usuario = %s, id_tip = %s
                WHERE id_usuario = %s
            """
            # Executa a query de atualização com os valores obtidos
            db.cursor.execute(query, (nm_usuario, end_usuario, tl_usuario, email_usuario, cpf_usuario, dat_nasc_usuario, login_usuario, senha_usuario, id_tip, id_usuario))
            db.conn.commit()  # Salva as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso.")  # Exibe uma mensagem de sucesso
            AlterarJanela.destroy()  # Fecha a janela de alteração
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar usuário: {e}")  # Exibe mensagem de erro em caso de falha

    # Função para excluir o usuário
    def DeletarUsuario():
        # Exibe um diálogo de confirmação antes de excluir
        confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este usuário?")
        if not confirm:
            return  # Cancela a exclusão caso o usuário clique em "Não"

        # Tenta excluir o usuário do banco de dados
        try:
            db.cursor.execute("DELETE FROM tb_usuario WHERE id_usuario = %s", (id_usuario,))  # Executa a query de exclusão
            db.conn.commit()  # Salva as mudanças no banco de dados
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")  # Exibe mensagem de sucesso
            AlterarJanela.destroy()  # Fecha a janela de alteração
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir usuário: {e}")  # Exibe mensagem de erro em caso de falha

    # Botão para salvar as alterações feitas no cadastro
    SalvarButton = ttk.Button(AlterarJanela, text="Salvar Alterações", command=SalvarAlteracoes)
    SalvarButton.place(x=80, y=350)

    # Botão para deletar o usuário
    DeletarButton = ttk.Button(AlterarJanela, text="Deletar", width=10, command=DeletarUsuario)
    DeletarButton.place(x=180, y=350)

    # Botão para voltar (fecha a janela de alteração sem salvar mudanças)
    VoltarButton = ttk.Button(AlterarJanela, text="Voltar", command=AlterarJanela.destroy)
    VoltarButton.place(x=320, y=350)

# Botões principais na janela principal
ttk.Button(UsuarioFrame, text="Buscar", width=8, command=AlterarOuExcluirUsuario).place(x=200, y=22)  # Botão para buscar usuário
ttk.Button(UsuarioFrame, text="Cadastrar", width=10, command=CadastrarUsuario).place(x=120, y=60)  # Botão para abrir a janela de cadastro
ttk.Button(UsuarioFrame, text="Sair", width=8, command=jan.quit).place(x=200, y=150)  # Botão para sair da aplicação

# Inicia o loop principal do Tkinter, mantendo a janela principal aberta
jan.mainloop()
