from tkinter import *
import tkinter as tk
    
class Janela:
   def __init__(self, master=None):
        
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.text1=Label(self.widget1, text='Arriegua agendamento')
        self.text1['font']=("Arial","20","bold")
        self.text1.pack(side=TOP)

        self.conteiner12=Frame(master,background='DodgerBlue')
        self.conteiner12['pady']=10
        self.conteiner12.pack()

        
        

        self.conteiner13=Frame(master,background='DodgerBlue')
        self.conteiner13['pady']=10
        self.conteiner13.pack()

        
        self.text1=Label(self.conteiner13, background='white',text='CDT cariri')
        self.text1['font']=("Arial","15")
        self.text1.pack(side=TOP)

        self.text1=Label(self.conteiner13, background='white',text='E um centro de diagnostico e terapia do cariri fundado')
        self.text1['font']=("Arial","10")
        self.text1.pack()
        
        self.text1=Label(self.conteiner13, background='white',text='  em 1990 tem sua cede na Rua andre cardoso Centro crato  que o ferece os seguintes servicos: ')
        self.text1['font']=("Arial","10")
        self.text1.pack()

        self.text1=Button(self.conteiner13, text='Dermatologia')
        self.text1['font']=("Arial","10")
        self.text1["width"]=50
        self.text1.pack()

        self.text1=Button(self.conteiner13, text='Ultrasonografia')
        self.text1['font']=("Arial","10")
        self.text1["width"]=50
       
        self.text1.pack()


        

        
        
   
root = Tk()
Janela(root)
root['background']='DodgerBlue'
root.geometry('600x500+0+0')
root.mainloop()
