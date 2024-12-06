from tkinter import *
import tkinter as tk

class Menu_ADM:
    def __init__(self,master=None):
        self.fonte=("Arial", "12")
        self.container1 = Frame(master)
        self.container1["padx"]=10
        self.container1['pady']=5
        self.container1.pack()

        self.btnProduto = Button(self.container1,text="Produto",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnProduto.pack(side=LEFT)
        
        self.container2 = Frame(master)
        self.container2["padx"]=10
        self.container2['pady']=5
        self.container2.pack()

        self.btnUsuarios = Button(self.container2,text="Usuários",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnUsuarios.pack(side=LEFT)
        
        self.container3 = Frame(master)
        self.container3["padx"]=10
        self.container3['pady']=5
        self.container3.pack()

        self.btnFornecedor = Button(self.container3,text="Fornecedor",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnFornecedor.pack(side=LEFT)

        self.container4 = Frame(master)
        self.container4["padx"]=10
        self.container4['pady']=5
        self.container4.pack()

        self.btnMarca = Button(self.container4,text="Marca",foreground="white",background="gray",font=self.fonte,width=40)
        self.btnMarca.pack(side=LEFT)

        self.container5 = Frame(master)
        self.container5["padx"]=70
        self.container5['pady']=15
        self.container5.pack(side=RIGHT)

        self.btnSair = Button(self.container5,text="Sair",foreground="white",background="gray",font=self.fonte,width=5)
        self.btnSair.pack()


       

if __name__ == "__main__":
    root = tk.Tk()
    login = Menu_ADM(root)
    root.title("Menu ADM")
    root.mainloop()
