from tkinter import *
import tkinter as tk
    
class Janela:
   def __init__(self, master=None):
        
        self.conteiner1=Frame(master)
        self.conteiner1['pady']=10
        self.conteiner1.pack()

        self.titulo=Label(self.conteiner1,text="Cadastrar Clinica")
        self.titulo['font']=("Calibri",'30')
        self.titulo.pack(side=TOP)

       
        
        self.conteiner13=Frame(master)
        self.conteiner13['pady']=10
        self.conteiner13.pack()

        self.telefone=Label(self.conteiner13,text="Telefone")
        self.telefone.pack(side=TOP)

        self.telefoneEntry=Entry(self.conteiner13)
        self.telefoneEntry["width"] = 30
        self.telefoneEntry.pack()
        

        self.conteiner=Frame(master)
        self.conteiner['pady']=10
        self.conteiner.pack()

        self.nomelabel=Label(self.conteiner,text="Nome")
        self.nomelabel.pack(side=TOP)

        self.nome=Entry(self.conteiner)
        self.nome["width"] = 30
        self.nome.pack()
        

        self.conteiner12=Frame(master)
        self.conteiner12['pady']=10
        self.conteiner12.pack()

        self.enderecolabel=Label(self.conteiner12,text="Endereço")
        self.enderecolabel.pack(side=TOP)
        
        self.endereco=Entry(self.conteiner12)
        self.endereco["width"] = 30
        self.endereco.pack()
       
        

        self.conteiner11=Frame(master)
        self.conteiner11['pady']=10
        self.conteiner11.pack()

        self.cnpjlabel=Label(self.conteiner11,text="CNPJ ")
        self.cnpjlabel.pack(side=TOP)

        self.cnpj=Entry(self.conteiner11)
        self.cnpj["width"] = 30
        self.cnpj.pack()

        self.conteiner18=Frame(master)
        self.conteiner18['pady']=10
        self.conteiner18.pack()

        self.emaillabel=Label(self.conteiner18,text="Email ")
        self.emaillabel.pack(side=TOP)

        self.email=Entry(self.conteiner18)
        self.email["width"] = 30
        self.email.pack()

        self.conteiner19=Frame(master)
        self.conteiner19['pady']=10
        self.conteiner19.pack()
        
        
        self.cadastrar=Button(self.conteiner19,width=10)
        self.cadastrar['text']='Cadastrar'
        self.cadastrar.pack()


        
        
   
root = Tk()
Janela(root)
root.geometry('600x1000+0+0')
root.mainloop()
