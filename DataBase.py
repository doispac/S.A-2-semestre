import mysql.connector #Importar o módulo mysql.connector para conectar ao banco de dados MySQL

class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="loja_doce_db"
        )
        self.cursor= self.conn.cursor() #Criar um cursor para executar comandos SQL
        #Criar a tabela 'tb_usuario' se ela não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tb_usuario(
            id_usuario int(10) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            nm_usuario varchar(40),
            end_usuario varchar(40),
            tl_usuario varchar(10),
            email_usuario varchar(40),
            cpf_usuario varchar(14),
            dat_nasc_usuario date, 
            login_usuario varchar(40), 
            senha_usuario varchar(40),
            id_tip int(10) zerofill NOT NULL           
        );''')
        self.conn.commit() #Confirma a criação da tabela

        print("conectado ao banco de Dados") #Imprime uma mensagem de confirmação

    #Método para registrar um novo usuário no banco de dados
    def RegistrarNoBanco(self,nm_usuario,end_usuario,tl_usuario,email_usuario,cpf_usuario,dat_nasc_usuario,login_usuario,senha_usuario,id_tip):
        self.cursor.execute("INSERT INTO tb_usuario (nm_usuario,end_usuario,tl_usuario,email_usuario,cpf_usuario,dat_nasc_usuario,login_usuario,senha_usuario,id_tip) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nm_usuario,end_usuario,tl_usuario,email_usuario,cpf_usuario,dat_nasc_usuario,login_usuario,senha_usuario,id_tip)) #Insere os dados do usuário na tabela
        self.conn.commit() #Confirma a inserção de dados

    #Método para alterar os dados de um usuário existente no banco de dados
    def alterarUsuario(self, id_usuario, nm_usuario, end_usuario, tl_usuario, email_usuario,cpf_usuario,dat_nasc_usuario,login_usuario,senha_usuario,id_tip):
            self.cursor.execute("UPDATE tb_usuario SET nm_usuario=%s, end_usuario=%s, tl_usuario=%s, email_usuario=%s, cpf_usuario=%s, dat_nasc_usuario=%s, login_usuario=%s, senha_usuario=%s WHERE id_usuario=%s",(nm_usuario,end_usuario,tl_usuario,email_usuario,cpf_usuario,dat_nasc_usuario,login_usuario,senha_usuario,id_tip,id_usuario)) # Atualiza os dados do usuário com o id fornecido
            self.conn.commit() #Confirma a atualização dos dados 

    #Método para excluir um usuário do banco de dados
    def excluirUsuario(self,id_usuario):
            self.cursor.execute("DELETE FROM tb_usuario WHERE id_usuario=%s",(id_usuario,))
            self.conn.commit()

    #Método para buscar os dados de um usuário no banco de dados
    def buscarUsuario(self,id_usuario):
            self.cursor.execute("SELECT * FROM tb_usuario WHERE id_usuario=%s",(id_usuario,))
            return self.cursor.fetchone()
    
    #Método para buscar os dados de um fornecedor no banco de dados
    def buscarFornecedor(self,id_fornecedor):
          self.cursor.execute("SELECT * FROM tb_fornecedor WHERE id_fornecedor=%s",(id_fornecedor))
          return self.cursor.fetchone()

    def __del__(self):
            self.conn.close()