from tkinter import Tk, Menu, Label, Entry, Button
from tkcalendar import Calendar
import CRUD

class Cadastrar:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.criarLabels()
        self.criarEntries()
        self.callendario()
        self.criarBotões()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Cadastrar tarefas')
        self.janela.geometry('700x400+300+100')
        self.janela.resizable(False, False)

    def criarLabels(self):
        self.nome = Label(self.janela, text='Nome da tarefa', font=('Arial bold', 12))
        self.nome.place(relx=0.05, rely=0.2)

        self.disciplina = Label(self.janela, text='Nome da disciplina', font=('Arial bold', 12))
        self.disciplina.place(relx=0.05, rely=0.3)

        self.professor = Label(self.janela, text='Nome do professor', font=('Arial bold', 12))
        self.professor.place(relx=0.05, rely=0.4)

        self.calendario = Label(self.janela, text='Data de entrega', font=('Arial bold', 12))
        self.calendario.place(relx=0.05, rely=0.5)

        self.titulo = Label(self.janela, text='CADASTRO', font=('Arial bold', 20), fg='#363636')
        self.titulo.place(relx=0.23, rely=0.05)

        self.obs = Label(self.janela, text='''
                                            Observação: Para inserir a data de entrega, 
                                            clique no calendário e depois em 'Salvar Data'
                                            ''', fg='red')
        self.obs.place(relx=0.15, rely=0.7)

    def criarEntries(self):
        self.entryNome = Entry(self.janela)
        self.entryNome.place(relx=0.23, rely=0.2, relheight=0.06, relwidth=0.35)

        self.entryDisciplina = Entry(self.janela)
        self.entryDisciplina.place(relx=0.26, rely=0.3, relheight=0.06, relwidth=0.32)

        self.entryProfessor = Entry(self.janela)
        self.entryProfessor.place(relx=0.26, rely=0.4, relheight=0.06, relwidth=0.32)

        self.entryCalendario = Entry(self.janela)
        self.entryCalendario.place(relx=0.26, rely=0.5, relheight=0.06, relwidth=0.32)
    
    def callendario(self):
        self.calendario = Calendar(self.janela, locale='pt_br')
        self.calendario.place(relx=0.62, rely=0.1)
    
    def criarBotões(self):
        self.Button = Button(self.janela, text='CADASTRAR TAREFA', font=('Arial bold', 10),
                                bg='white',
                                command=lambda:CRUD.Conexão().cadastrar(self.entryNome.get(), 
                                self.entryDisciplina.get(), self.entryProfessor.get(), 
                                self.entryCalendario.get()))
        self.Button.place(relx=0.05, rely=0.59, relheight=0.08, relwidth=0.53)


        self.ButtonData = Button(self.janela, text='SALVAR DATA', font=('Arial bold', 10), 
                                bg='white')
        self.ButtonData.place(relx=0.62, rely=0.59, relheight=0.08, relwidth=0.36)

if __name__ == '__main__':
    Cadastrar()
