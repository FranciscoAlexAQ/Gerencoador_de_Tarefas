from tkinter import Tk, Menu, Label, Entry, Button
import CRUD

class Atualizar:
    def __init__(self):
        self.janela = Tk()
        self.configurarJanela()
        self.criarLabels()
        self.criarEntries()
        self.criarBotões()
        self.janela.mainloop()
    
    def configurarJanela(self):
        self.janela.title('Atualizar tarefas')
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

        self.titulo = Label(self.janela, text='ATUALIZAÇÃO', font=('Arial bold', 20), fg='red')
        self.titulo.place(relx=0.23, rely=0.05)

    def inserir(self, cod, nome, disci, prof, calend):
        #self.code = cod
        self.entryNome.insert(0, nome)
        self.entryDisciplina.insert(0, disci)
        self.entryProfessor.insert(0, prof)
        self.entryCalendario.insert(0, calend)

    def criarEntries(self):
        self.entryNome = Entry(self.janela)
        self.entryNome.place(relx=0.23, rely=0.2, relheight=0.06, relwidth=0.35)

        self.entryDisciplina = Entry(self.janela)
        self.entryDisciplina.place(relx=0.26, rely=0.3, relheight=0.06, relwidth=0.32)

        self.entryProfessor = Entry(self.janela)
        self.entryProfessor.place(relx=0.26, rely=0.4, relheight=0.06, relwidth=0.32)

        self.entryCalendario = Entry(self.janela)
        self.entryCalendario.place(relx=0.26, rely=0.5, relheight=0.06, relwidth=0.32)

    def criarBotões(self):
        self.Button = Button(self.janela, text='Atualizar Tarefa', 
                                command=lambda:CRUD.Conexão().cadastrar(self.entryNome.get(), 
                                self.entryDisciplina.get(), self.entryProfessor.get(), 
                                self.entryCalendario.get()))
        self.Button.place(relx=0.15, rely=0.59, relheight=0.08, relwidth=0.36)


if __name__ == '__main__':
    Atualizar()
