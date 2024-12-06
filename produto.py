from tkinter import *
import menuADM
import tkinter as ttk

jan = Tk()
jan.title("Doceria - Produto")
jan.geometry("400x200")
jan.configure(background="white")
jan.resizable(width=False,height=False)

jan.iconbitmap(default="icons/bala.ico")

produtoFrame = Frame(jan,width=600,height=300,bg="PURPLE",relief="raise")
produtoFrame.pack()

def Cadastro():
    print("oi")
    
   

cadastrobutton = ttk.Button(produtoFrame,text="Cadastrar",width=15, command=Cadastro)
cadastrobutton.place(x=5,y=150) 

retornarbutton = ttk.Button(produtoFrame,text="Retornar",width=15, command=menuADM)
retornarbutton.place(x=100,y=150) 

jan.mainloop()