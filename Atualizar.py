from tkinter import Tk
from tkinter import Menu


class Atualizar:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Atualizar Informações')
        self.janela.geometry('700x400+300+100')
        self.janela.resizable(False, False)
