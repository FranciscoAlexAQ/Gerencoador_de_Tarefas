from tkinter import Tk, Menu, Label
from tkinter.ttk import Treeview
import Cadastrar


# Classe principal
class GerenciadorTarefas:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.criarMenu()
        self.criarLabel()
        self.criarTabelaTarefas()
        self.janela.mainloop()
    
    # configurando janel
    def configurarJanela(self):
        self.janela.title('Gerenciador de Tarefas')
        self.janela.geometry('700x400+300+100')
        self.janela.resizable(False, False)

    # Criando menus 
    def criarMenu(self):
        # ========== Menu principal ==============================================
        self.menu = Menu(self.janela)

        # ----------- Menu de cadastro --------------------------------------------
        self.cadastrar = Menu(self.menu)
        self.menu.add_command(label='cadastrar', command=Cadastrar.Cadastrar)
        # -------------------------------------------------------------------------

        # ========== Fim do menu principal ========================================
        self.janela.config(menu=self.menu)
    
    # Criando a label
    def criarLabel(self):
        self.labelPrincipal = Label(self.janela, text='LISTA DE TAREFAS PENDENTES', fg='red', 
                                                font=('Arial, bold', 14))
        self.labelPrincipal.place(relx=0.3, rely=0.05)

    # Criando a tabela de tarefas 
    def criarTabelaTarefas(self):
        # Tabela de tarefas 
        self.tabela = Treeview(self.janela, column=('col1', 'col2', 'col3', 'col4', 'col5'))

        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='código')
        self.tabela.heading('#2', text='tarefa')
        self.tabela.heading('#3', text='disciplina')
        self.tabela.heading('#4', text='professor')
        self.tabela.heading('#5', text='data da entrega')

        self.tabela.column('#0', width=-60)
        self.tabela.column('#1', width=30)
        self.tabela.column('#2', width=70)
        self.tabela.column('#3', width=70)
        self.tabela.column('#4', width=100)
        self.tabela.column('#5', width=100)

        self.tabela.place(relx=0.005, rely=0.2, relwidth=0.99)


GerenciadorTarefas()
