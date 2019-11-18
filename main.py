from tkinter import *
import tkinter as tk

class cadastro1:
    def __init__(self,nome='',endereco='',cnpj=''):
        self.conteiner10 = Frame(master)
        self.nome=Entry(self.conteiner10)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao

        self.conteiner12 = Frame(master)
        self.endereco=Entry(self.conteiner12)
        self.endereco["width"] = 30
        self.endereco["font"] = self.fontePadrao

        self.conteiner11 = Frame(master)
        self.cnpj=Entry(self.conteiner11)
        self.cnpj["width"] = 30
        self.cnpj["font"] = self.fontePadrao

class Sistema:
    def __init__(self):
        self.conteiner=Frame(master)
        self.conteiner.pack()

class Janela:
    def __init__(self, master=None):
        
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.text1=Label(self.widget1, text='Arriegua agendamento')
        self.text1['font']=("Arial","20","bold")
        self.text1.pack(side=TOP)

        self.conteiner4=Frame(master,background='DodgerBlue')
        self.conteiner4['pady']=30
        self.conteiner4.pack()

        self.segundoConteiner=Frame(master,background='DodgerBlue')
        self.segundoConteiner['pady']=20
        self.segundoConteiner.pack()
        
        self.email = Label(self.segundoConteiner, background='white',text="Email: ")
        self.email.pack(side=LEFT)
        
        self.text2=Label(self.conteiner4, background='white',text='Cliente')
        self.text2['font']=("Arial","15","bold")
        self.text2.pack(side=TOP)

        self.senhaLabel = Label(self.segundoConteiner, background='white',text="Login")
        self.senhaLabel['font']=("Arial","8","bold")
        self.senhaLabel.pack()
        
        self.emaill = Entry(self.segundoConteiner,background='white',text="Email")
        self.emaill["width"] = 30,
        self.emaill.pack()

        self.terceiroConteiner=Frame(master,background='DodgerBlue')
        self.terceiroConteiner['pady']=20
        self.terceiroConteiner.pack()
        
        self.senhaLabel = Label(self.terceiroConteiner, text="Senha: ",background='white')
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroConteiner,background='white')
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.quartoConteiner=Frame(master,background='DodgerBlue')
        self.quartoConteiner['pady']=20
        self.quartoConteiner.pack()
  
        self.autenticar = Button(self.quartoConteiner)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack(side=LEFT)


        self.widget3 = Frame(master,background='white')
        self.widget3.pack()
        self.text1=Label(self.widget3, background='white',text='Empresa')
        self.text1['font']=("Arial","15","bold")
        self.text1.pack()

        self.segundoConteiner1=Frame(master,background='DodgerBlue')
        self.segundoConteiner1['pady']=20
        self.segundoConteiner1.pack()

        self.senhaLabel = Label(self.segundoConteiner1, background='white',text="Login")
        self.senhaLabel['font']=("Arial","8","bold")
        self.senhaLabel.pack(side=TOP)

        self.email2 = Label(self.segundoConteiner1, text="Email")
        self.email2.pack(side=LEFT)
        
        self.emaill22 = Entry(self.segundoConteiner1,background='white',text="Email: ")
        self.emaill22["width"] = 30,
        self.emaill22.pack(side=LEFT)

        self.terceiroConteiner1=Frame(master,background='DodgerBlue')
        self.terceiroConteiner1['pady']=20
        self.terceiroConteiner1.pack()
        
        self.senhaLabel = Label(self.terceiroConteiner1, background='white',text="Senha: ")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroConteiner1)
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.quartoConteiner2=Frame(master,background='DodgerBlue')
        self.quartoConteiner2['pady']=20
        self.quartoConteiner2.pack()
  
        self.autenticar = Button(self.quartoConteiner2)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack()
        
        self.conteiner=Frame(master,background='black')
        self.conteiner['pady']=-100
        self.conteiner.pack()
        
        self.visita=Button(self.conteiner,width=10,command=sistema)
        self.visita['text']='visita'
        self.visita.pack()
def sistema():
    root = Tk()
    Janela(root)
    root.geometry('600x500+0+0')
    root['background']='DodgerBlue'
    root.mainloop()
            
    self.widget1 = Frame(master,background='DodgerBlue')
    self.widget1['background']='black'
    self.widget1.pack()
    self.text1=Label(self.widget1, text='Arriegua agendamento')
    self.text1['font']=("Arial","20","bold")
    self.text1.pack(side=TOP)

    self.conteiner12=Frame(master,background='DodgerBlue')
    self.conteiner12['pady']=10
    self.conteiner12.pack()
            
    self.endereco=Entry(self.conteiner12)
    self.endereco["width"] = 30
    self.endereco.pack()

    self.conteiner19=Frame(master,background='DodgerBlue')
    self.conteiner19['pady']=8
    self.conteiner19.place(x=400,y=40)
            
    self.pesquisar=Button(self.conteiner19,width=8)
    self.pesquisar['text']='Pesquisar'
    self.pesquisar.pack()

    self.conteiner13=Frame(master,background='white')
    self.conteiner13['pady']=10
    self.conteiner13.pack()
            
    self.text1=Label(self.conteiner13,background='white', text='CDT cariri')
    self.text1['font']=("Arial","15")
    self.text1.pack(side=TOP)

    self.text1=Label(self.conteiner13,background='white', text='CNPJ:43073984593454759')
    self.text1['font']=("Arial","10")
    self.text1.pack()

    self.text1=Label(self.conteiner13, background='white',text='NUMERO:(88)96760818')
    self.text1['font']=("Arial","10")
    self.text1.pack(side=LEFT)

    self.conteiner16=Frame(master,background='white')
    self.conteiner16['pady']=10
    self.conteiner16.place(x=220,y=190)

    self.text1=Label(self.conteiner16,background='white', text='VIcente lemos')
    self.text1['font']=("Arial","15")
    self.text1.pack(side=TOP)

    self.text1=Label(self.conteiner16, background='white',text='CNPJ:43073984593454759')
    self.text1['font']=("Arial","10")
    self.text1.pack()
            
    self.text1=Label(self.conteiner16,background='white', text='NUMERO:(88)96760818')
    self.text1['font']=("Arial","10")
    self.text1.pack(side=LEFT)

    self.conteiner15=Frame(master,background='white')
    self.conteiner15['pady']=15
    self.conteiner15.place(x=220,y=320)
            
    self.text1=Label(self.conteiner15, text='Afago',background='white')
    self.text1['font']=("Arial","15")
    self.text1.pack(side=TOP)

    self.text1=Label(self.conteiner15, text='CNPJ:43073984593454759',background='white')
    self.text1['font']=("Arial","10")
    self.text1.pack()

    self.text1=Label(self.conteiner15, text='NUMERO:(88)96760818',background='white')
    self.text1['font']=("Arial","10")
    self.text1.pack(side=LEFT)
        
   
root = Tk()
Janela(root)
root.geometry('600x500+0+0')
root['background']='DodgerBlue'
root.mainloop()
