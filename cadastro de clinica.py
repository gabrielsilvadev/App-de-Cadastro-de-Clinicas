from tkinter import *
import tkinter as tk
    
class Janela:
   def __init__(self, master=None):


        self.widget1 = Frame(master)
        self.widget1.pack()
        self.text1=Label(self.widget1, text='Arriegua agendamento')
        self.text1['font']=("Arial","20","bold")
        self.text1.pack(side=TOP)
        
        self.conteiner1=Frame(master)
        self.conteiner1['pady']=10
        self.conteiner1.pack()

        self.titulo=Label(self.conteiner1,text="Cadastrar Clinica")
        self.titulo['font']=("Calibri",'10')
        self.titulo.pack(side=TOP)

        
        #self.widget2=Frame(master)
        #self.widget2.pack()
        #self.imagem=PhotoImagem(self.widget2,file='')
        #self.imagem.pack()
       
        self.conteiner=Frame(master)
        self.conteiner['pady']=10
        self.conteiner.pack()

        self.nomelabel=Label(self.conteiner,text="Nome")
        self.nomelabel.pack(side=TOP)

        self.nome=Entry(self.conteiner)
        self.nome["width"] = 30
        self.nome.pack()
        
        self.conteiner13=Frame(master)
        self.conteiner13['pady']=10
        self.conteiner13.pack()

        self.telefone=Label(self.conteiner13,text="Telefone")
        self.telefone.pack(side=TOP)

        self.telefoneEntry=Entry(self.conteiner13)
        self.telefoneEntry["width"] = 30
        self.telefoneEntry.pack()
        

        
        

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

        self.conteiner21=Frame(master)
        self.conteiner21['pady']=10
        self.conteiner21.pack()

        self.emaillabel=Label(self.conteiner21,text="Quantos servicoes")
        self.emaillabel.pack(side=TOP)

        self.email=Entry(self.conteiner21)
        self.email["width"] = 30
        self.email.pack()

        self.conteiner19=Frame(master)
        self.conteiner19['pady']=10
        self.conteiner19.pack()
        
        
        self.cadastrar=Button(self.conteiner19,width=10)
        self.cadastrar['text']='Cadastrar'
        self.cadastrar.pack()


        
        self.conteiner50=Frame(master)
        self.conteiner50['pady']=10
        self.conteiner50.place()

        self.medicolabel=Label(self.conteiner50,text="Medico(a)")
        self.medicolabel.pack(side=TOP)
        
        self.medico=Entry(self.conteiner50)
        self.medico["width"] = 30
        self.medico.pack()
       
        

        self.conteiner51=Frame(master)
        self.conteiner51['pady']=10
        self.conteiner51.place()

        self.crmlabel=Label(self.conteiner51,text="Crm")
        self.crmlabel.pack(side=TOP)

        self.crm=Entry(self.conteiner51)
        self.crm["width"] = 30
        self.crm.pack()

        self.conteiner52=Frame(master)
        self.conteiner52['pady']=10
        self.conteiner52.place()

        self.descricaolabel=Label(self.conteiner52,text="Descricao")
        self.descricaolabel.pack()

        self.descricao=Entry(self.conteiner52)
        self.descricao["width"] = 30
        self.descricao.pack()

        self.conteiner53=Frame(master)
        self.conteiner53['pady']=10
        self.conteiner53.place()

        self.email1label=Label(self.conteiner53,text="Quantos servicoes")
        self.email1label.pack()

        self.email1=Entry(self.conteiner53)
        self.email1["width"] = 30
        self.email1.pack()


        
        
   
root = Tk()
Janela(root)
root.geometry('600x600+10+10')
root.mainloop()
