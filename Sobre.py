from tkinter import Tk, Label



class Sobre:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.criarLabel()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Sobre a aplicação')
        self.janela.geometry('300x300+520+100')
        self.janela.resizable(False, False)

    def criarLabel(self):
        self.titulo = Label(self.janela, text='''
                                              Este programa 
                                             foi desenvolvido 
                                            por Francisco Alex
                                                Técnico em Informática     
                                            ''', font=('Arial bold', 15), fg='red')
        self.titulo.place(relx=-0.8, rely=0.2)
                                        

if __name__ == '__main__':
    Sobre()
