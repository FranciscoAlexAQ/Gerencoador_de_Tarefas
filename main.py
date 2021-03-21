from tkinter import Tk, Menu, Label, Button, Entry
from tkinter.ttk import Treeview
import Cadastrar, Atualizar, Sobre
from CRUD import Conexão


# Classe principal
class GerenciadorTarefas:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.criarMenu()
        self.criarLabel()
        self.criarBotões()
        self.criarEntries()
        self.criarTabelaTarefas()
        self.janela.mainloop()
    
    # configurando janela
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

        # ----------- Menu de atuaçização -----------------------------------------
        self.sobre = Menu(self.menu)
        self.menu.add_command(label='Sobre', command=Sobre.Sobre)
        # -------------------------------------------------------------------------

        # ========== Fim do menu principal ========================================
        self.janela.config(menu=self.menu)
    
    # Criando a label
    def criarLabel(self):
        self.labelPrincipal = Label(self.janela, text='LISTA DE TAREFAS PENDENTES', fg='red', 
                                                font=('Arial, bold', 14))
        self.labelPrincipal.place(relx=0.3, rely=0.05)

    # Criando botões
    def criarBotões(self):
        self.btnExcluir = Button(self.janela, text='excluir', font=('Arial bold', 12))
        self.btnExcluir.place(relx=0.04, rely=0.16, relwidth=0.15, relheight=0.08)

        self.btnPesquisar = Button(self.janela, text='pesquisar', font=('Arial bold', 12))
        self.btnPesquisar.place(relx=0.27, rely=0.16, relwidth=0.15, relheight=0.08)
    
    # Criando entries
    def criarEntries(self):
        self.entryPesquisa = Entry(self.janela)
        self.entryPesquisa.place(relx=0.43, rely=0.16, relheight=0.08, relwidth=0.3)

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

        self.tabela.place(relx=0.005, rely=0.3, relwidth=0.99, relheight=0.69)

        #self.tabela.delete(*self.tabela.get_children())
        for i in Conexão().consultar():
            self.tabela.insert('', 0, values=i)



GerenciadorTarefas()
