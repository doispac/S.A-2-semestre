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

FornecedorFrame = Frame(jan,width=400,height=200,bg="PURPLE",relief="raise")#CRIA A FRAME TelaFornecedor
FornecedorFrame.pack()#POSICIONA A FRAME TelaFornecedor


#ADICIONAR CAMPOS DE USUÁRIO E SENHA
FornecedorLabel = Label(FornecedorFrame,text="Cod.Fornecedor: ",font=("Times New Roman",18),bg="PURPLE",fg="White")#CRIA UM LABEL PARA O USUÁRIO
FornecedorLabel.place(x=5,y=40)

FornecedorEntry = ttk.Entry(FornecedorFrame,width=10)#CRIA UM CAMPO DE ENTRADA PARA O USUÁRIO
FornecedorEntry.place(x=180,y=50) #POSICIONA O CAMPO DE ENTRADA


#FUNÇÃO DO LOGIN
def Fornecedor():
    id_fornecedor = FornecedorEntry.get() #Obtém o valor do campo de entrada de fornecedor

    #Conecta ao banco de dados
    db = Database() #Cria uma instância da classe Database
    db.cursor.execute("""
    SELECT * FROM tb_fornecedor
    WHERE id_fornecedor = %s,""",(id_fornecedor)) #Executa a consulta SQL para verificar o códio do fornecedor
    VerifyLogin = db.cursor.fetchone() #Obtém o resultado da consulta

    #Veriricar se o usuário foi encontrado
    if VerifyLogin:

     command=DadosFornecedor

    else:
        messagebox.showinfo(title="INFO FORNECEDOR",message="Código inválido") #Exibe mensagem de erro

BuscarButton = ttk.Button(FornecedorFrame,text="Buscar",width=6, command=Fornecedor) #Cria um botão de Buscar
BuscarButton.place(x=250,y=47) #Posiciona o botão de Buscar

CadastrarButton = ttk.Button(FornecedorFrame,text="Cadastrar",width=10, command=Fornecedor) #Cria um botão de Cadastrar
CadastrarButton.place(x=5,y=100) #Posiciona o botão de Buscar

RetornarButton = ttk.Button(FornecedorFrame,text="Retornar",width=8, command=Fornecedor) #Cria um botão de Retornar ao menu principal
RetornarButton.place(x=320,y=160) #Posiciona o botão de Buscar


#FUNÇÃO PARA REGISTRAR NOVO USUÁRIO
def CadastrarFornecedor():
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

def DadosFornecedor():
       
       FornecedorLabel.place(x=5000) #Move o label do fornecedor para fora da tela
       FornecedorEntry.place(x=5000) #Move o campo de entrada do fornecedor para fora da tela
       BuscarButton.place(x=5000) #Move o botão de busca para fora da tela
       CadastrarButton.place(x=5000) #Move o botão cadastro para fora da tela
       RetornarButton.place(x=5000) #Move o o botão de retornar para fora da tela

       Nome_Label = Label(FornecedorFrame,text="Fornecedor:",font=("Times New Roman",18),bg="PURPLE",fg="White") #Cria um label para o nome do fornecedor
       Nome_Label.place(x=5,y=5) #Psiciona o label no frame

       Nome_Entry = ttk.Entry(FornecedorFrame,width=30) #Posiciona o campo de entrada do nome do fornecedor
       Nome_Entry.place(x=120,y=20) #Posiciona o campo de entrada do nome do fornecedor

       CNPJ_Label = Label(FornecedorFrame, text="CNPJ:",font=("Times New Roman",18),bg="PURPLE",fg="White") #Cria um label para o cnpj
       CNPJ_Label.place(x=5,y=40) #Posiciona o label no frame

       CNPJ_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o cnpj
       CNPJ_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       END_Label = Label(FornecedorFrame, text="Endereço:",font=("Times New Roman",18),bg="PURPLE",fg="White") #Cria um label para o endereço
       END_Label.place(x=5,y=40) #Posiciona o label no frame direito

       END_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o endereço
       END_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       TEL_Label = Label(FornecedorFrame, text="Telefone:",font=("Times New Roman",18),bg="PURPLE",fg="White") #Cria um label para o número de telefone
       TEL_Label.place(x=5,y=40) #Posiciona o label no frame

       
       TEL_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o número de telefone
       TEL_Entry.place(x=120,y=55) #Posiciona o campo de entrada

       EMAIL_Label = Label(FornecedorFrame, text="Email:",font=("Times New Roman",18),bg="PURPLE",fg="White") #Cria um label para o email
       EMAIL_Label.place(x=5,y=40) #Posiciona o label no frame

       EMAIL_Entry = ttk.Entry(FornecedorFrame,width=30) #Cria um campo de entrada para o email
       EMAIL_Entry.place(x=120,y=55) #Posiciona o campo de entrada

# INICIAR O LOOP PRINCIPAL
jan.mainloop() # Inicia o loop principal da aplicação