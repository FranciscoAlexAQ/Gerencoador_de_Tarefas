import sqlite3


class Conexão:
    
    def criarBanco(self):
        try:
            self.conn = sqlite3.connect('banco.db')
            return self.conn
        except Exception as e:
            print(e)
    
    def criarTabela(self):
        try:
            conn = self.criarBanco()
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE tarefas (codigo integer primary key autoincrement,
                                                   tarefa varchar(30) not null,
                                                   disciplina varchar(30) not null, 
                                                   professor varchar(30) not null, 
                                                   data varchar(30) not null)''')
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def deletarTabela(self):
        try:
            conn = self.criarBanco()
            cursor = conn.cursor()
            cursor.execute('DROP TABLE tarefas')
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def cadastrar(self, tarefa, disciplina, professor, data):
        try:
            self.conn = self.criarBanco()
            self.cursor = self.conn.cursor()
            self.cursor.execute(f'''INSERT INTO tarefas (tarefa, disciplina, professor, data)
                                                    VALUES ("{tarefa}", "{disciplina}", "{professor}", "{data}")''')
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)

    def consultar(self):
        try:
            self.conn = self.criarBanco()
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM tarefas ORDER BY data')
            self.conn.commit() 
            self.dados = self.cursor.fetchall()
            self.conn.close()
            return self.dados
        except Exception as e:
            print(e)


if __name__ == '__main__':
    #Conexão().deletarTabela()
    Conexão().criarTabela()
    


