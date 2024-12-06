from tkinter import *
import tkinter as tk

class Menu_Usuario:
    def __init__(self,master=None):
        self.fonte=("Arial", "12")
        self.container1 = Frame(master)
        self.container1["padx"]=10
        self.container1['pady']=5
        self.container1.pack()

        self.btnMinhaConta = Button(self.container1,text="Minha Conta",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnMinhaConta.pack(side=LEFT)
        
        self.container2 = Frame(master)
        self.container2["padx"]=10
        self.container2['pady']=5
        self.container2.pack()

        self.btnProduto = Button(self.container2,text="Produto",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnProduto.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3["padx"]=70
        self.container3['pady']=15
        self.container3.pack(side=RIGHT)

        self.btnSair = Button(self.container3,text="Sair",foreground="white",background="gray",font=self.fonte,width=5)
        self.btnSair.pack()

if __name__ == "__main__":
    root = tk.Tk()
    login = Menu_Usuario(root)
    root.title("Menu Usuário")
    root.mainloop()
