from tkinter import Tk
from tkinter import Menu


class Sobre:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Sobre a aplicação')
        self.janela.geometry('700x400+300+100')
        self.janela.resizable(False, False)
