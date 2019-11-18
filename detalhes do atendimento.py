from tkinter import *
import tkinter as tk
    
class Janela:
   def __init__(self, master=None):
        
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.text1=Label(self.widget1, text='Arriegua agendamento')
        self.text1['font']=("Arial","20","bold")
        self.text1.pack(side=TOP)

        self.conteiner12=Frame(master,background='black')
        self.conteiner12['pady']=10
        self.conteiner12.pack()

        
        

        self.conteiner13=Frame(master,background='DodgerBlue')
        self.conteiner13['pady']=10
        self.conteiner13.pack()

        
        self.text1=Label(self.conteiner13, background='white',text='CDT cariri')
        self.text1['font']=("Arial","15",'bold' )
        self.text1.pack(side=TOP)

        self.text1=Label(self.conteiner13, background='white',text='Dermatologia')
        self.text1['font']=("Arial","10")
        self.text1.pack(side=TOP)
        
        self.text1=Label(self.conteiner13, background='white',text='Dr.RENATA FERRER, especialista em procedimentos dermatologicos pela UFC Fortaleza. ')
        self.text1['font']=("Arial","10")
        self.text1.pack()
        
        self.text1=Label(self.conteiner13, background='white',text='10 anos de esperiencia na area. portando o CRM:12343 ')
        self.text1['font']=("Arial","10")
        self.text1.pack()
        
        self.text1=Label(self.conteiner13, background='white',text='Horarios de  Atendimento')
        self.text1['font']=("Arial","10",'bold')
        self.text1.pack(side=TOP)

        self.text1=Checkbutton(self.conteiner13,background='DodgerBlue', text='7:00-8:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()

        self.text1=Checkbutton(self.conteiner13,background='DodgerBlue' ,text='8:00-9:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()
        self.text1=Checkbutton(self.conteiner13, background='DodgerBlue',text='9:00-10:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()

        self.text1=Checkbutton(self.conteiner13,background='DodgerBlue', text='10:00-11:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()

        self.text1=Checkbutton(self.conteiner13, background='DodgerBlue',text='13:00-14:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()

        self.text1=Checkbutton(self.conteiner13, background='DodgerBlue',text='14:00-15:00')
        self.text1['font']=("Arial","8")
        self.text1["width"]=150
        self.text1.pack()

        self.conteiner23=Frame(master,background='DodgerBlue')
        self.conteiner23['pady']=10
        self.conteiner23.pack()
        
        self.text1=Button(self.conteiner23, text='Confirmar')
        self.text1['font']=("Arial","8")
        self.text1["width"]=50
        self.text1.pack()


        

        
        
   
root = Tk()
Janela(root)
root['background']='DodgerBlue'
root.geometry('600x500+0+0')
root.mainloop()
