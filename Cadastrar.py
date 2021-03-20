from tkinter import Tk
from tkinter import Menu


class Cadastrar:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Gerenciador de Tarefas')
        self.janela.geometry('700x400+300+100')
        self.janela.resizable(False, False)
