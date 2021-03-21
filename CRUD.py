import sqlite3


class Conexão:
    
    def criarBanco(self):
        try:
            conn = sqlite3.connect('banco.db')
            return conn
        except Exception as e:
            print(e)
    
    def criarTabela(self):
        try:
            conn = self.criarBanco()
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE tarefas (codigo int primary key not null,
                                                   tarefa varchar(30) not null,
                                                   disciplina varchar(30) not null, 
                                                   professor varchar(30) not null, 
                                                   data varchar(30) not null)''')
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def cadastrar(self):
        try:
            conn = self.criarBanco()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO tarefas (codigo, tarefa, disciplina, professor, data)
                                                    VALUES (2, "tarefa B", "Disciplina C", "Paulo", "20/03/2021")''')
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

