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

       

class sistema:
    def __init__(self,cadastro1):
        self.conteiner=Frame(master)
        self.conteiner.pack()
        self.lista=list[]
        self.lista = self.conteiner

class Janela:  
    def __init__(self, master=None):
        
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.text1=Label(self.widget1, text='arriegua agenda')
        self.text1.pack()

        self.widget2=Frame(master)
        self.widget2.pack()
        self.text2=Label(self.widget2, text='quem sou eu?')
        self.text2.pack()

        self.widget3=Frame(master)
        self.widget3.pack()
        self.empresa = Button(self.widget3,width=15)
        self.empresa['text']='Empresa'
        self.widget3['pady']=10
        self.empresa.pack()
        
        self.widget4=Frame(master)
        self.widget4.pack()
        self.cliente=Button(self.widget4,width=15)
        self.cliente['text']='Cliente'
        self.widget4['pady']=10
        self.cliente.pack()

        self.widget5=Frame(master)
        self.widget5.pack()
        self.visita=Button(self.widget5,width=15)
        self.widget5['pady']=10
        self.visita['text']='visita'
        self.widget5['bg']='#F2F2F2'
        self.visita.pack()
        
        
        #self.visita['comand']=self.sistem()
   
root = Tk()
Janela(root)
arquivo=Image.open("C:/Downloads/im.jpg")
background_image=PhotoImage(arquivo)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry('500x500+0+0')
root.mainloop()
