from tkinter import * #IMPORTA TODOS OS MODULOS DO TKINTER
from tkinter import messagebox #IMPORTA O MÓDULO DE CAIXA DE TEXTO DO TKINTER
from tkinter import ttk
from turtle import register_shape  #IMPORTA O MÓDULO DE WIDGETS TEMÁTICOS DO TKINTER
from DataBase import Database #IMPORTA A CLASSE DataBase DO MÓDULO DataBase

jan = Tk() #CRIA UMA INSTÂNCIA DA JANELA PRINCIAL
jan.title("Painel Forcenedor") #DEFINE UM TÍTULO DA JANELA
jan.geometry("400x200") #DEFINE O TAMANHO DA JANELA
jan.configure(background="white") #CONFIGURA A COR DE FUNDO DA JANELA
jan.resizable(width=False,height=False)#IMPEDE QUE A JANELA SEJA REDIMENCIONADA

FornecedorFrame = Frame(jan,width=400,height=200,bg="MIDNIGHTBLUE",relief="raise")#CRIA A FRAME TelaFornecedor
FornecedorFrame.pack()#POSICIONA A FRAME TelaFornecedor


#ADICIONAR CAMPOS DE USUÁRIO E SENHA
FornecedorLabel = Label(FornecedorFrame,text="Cod Fornecedor: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#CRIA UM LABEL PARA O USUÁRIO
FornecedorLabel.place(x=5,y=40)

FornecedorEntry = ttk.Entry(FornecedorFrame,width=10)#CRIA UM CAMPO DE ENTRADA PARA O USUÁRIO
FornecedorEntry.place(x=215,y=50) #POSICIONA O CAMPO DE ENTRADA


#FUNÇÃO DO LOGIN
def Fornecedor():
    id_fornecedor = FornecedorEntry.get() #Obtém o valor do campo de entrada de usuário

    #Conecta ao banco de dados
    db = Database() #Cria uma instância da classe Database
    db.cursor.execute("""
    SELECT * FROM tb_fornecedor
    WHERE id_fornecedor = %s,""",(id_fornecedor,)) #Executa a consulta SQL para verificar o códio do fornecedor
    VerifyLogin = db.cursor.fetchone() #Obtém o resultado da consulta

    #Veriricar se o usuário foi encontrado
    if VerifyLogin:
       
       Nome_Label = Label(FornecedorFrame,text="Fornecedor:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o nome
       Nome_Label.place(x=5,y=5) #Psiciona o label no frame direito

       Nome_Entry = ttk.Entry(FornecedorFrame,width=30) #Posiciona o campo de entrada
       Nome_Entry.place(x=120,y=20) #Posiciona o campo de entrada

       CNPJ_Label = Label(FornecedorFrame, text="CNPJ:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
       CNPJ_Label.place(x=5,y=40) #Posiciona o label no frame direito

       CNPJ_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
       CNPJ_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       END_Label = Label(FornecedorFrame, text="Endereço:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
       END_Label.place(x=5,y=40) #Posiciona o label no frame direito

       END_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
       END_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       TEL_Label = Label(FornecedorFrame, text="Telefone:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
       TEL_Label.place(x=5,y=40) #Posiciona o label no frame direito

       
       TEL_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
       TEL_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       EMAIL_Label = Label(FornecedorFrame, text="Email:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
       EMAIL_Label.place(x=5,y=40) #Posiciona o label no frame direito

       EMAIL_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
       EMAIL_Entry.place(x=120,y=55) #Posiciona o campo de entrada

    else:
        messagebox.showinfo(title="INFO FORNECEDOR",message="Códico inválido") #Exibe mensagem de erro

BuscarButton = ttk.Button(FornecedorFrame,text="Buscar",width=10, command=Fornecedor) #Cria um botão de Buscar
BuscarButton.place(x=300,y=47) #Posiciona o botão de Buscar

CadastrarButton = ttk.Button(FornecedorFrame,text="Cadastrar",width=10, command=Fornecedor) #Cria um botão de Cadastrar
CadastrarButton.place(x=225,y=100) #Posiciona o botão de Buscar

RetornarButton = ttk.Button(FornecedorFrame,text="Retornar",width=10, command=Fornecedor) #Cria um botão de Retornar ao menu principal
RetornarButton.place(x=300,y=100) #Posiciona o botão de Buscar


#FUNÇÃO PARA REGISTRAR NOVO USUÁRIO
def Registrar():
    #REMOVENDO BOTÕES DE LOGIN
    #LoginButton.place(x=5000) #Move o botão de registro para fora da tela
    #RegisterButton.place(x=5000) #Move o botão de registro para fora da tela

    #INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label(FornecedorFrame,text="Nome:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o nome
    NomeLabel.place(x=5,y=5) #Psiciona o label no frame direito

    NomeEntry = ttk.Entry(FornecedorFrame,width=30) #Posiciona o campo de entrada
    NomeEntry.place(x=120,y=20) #Posiciona o campo de entrada

    EmailLabel = Label(FornecedorFrame, text="Email:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
    EmailLabel.place(x=5,y=40) #Posiciona o label no frame direito

    EmailEntry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
    EmailEntry.place(x=120,y=55) #Posiciona o campo de entrada

    #FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS


# INICIAR O LOOP PRINCIPAL
jan.mainloop() # Inicia o loop principal da aplicação