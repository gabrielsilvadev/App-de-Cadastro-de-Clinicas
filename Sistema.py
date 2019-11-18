from tkinter import *
import tkinter as tk
    
class Sistema:
   
   def __init__(self,master=None):          
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
Sistema(root)
root['background']='DodgerBlue'
root.geometry('600x500+0+0')
root.mainloop()
