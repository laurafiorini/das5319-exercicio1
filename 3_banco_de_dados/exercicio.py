import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM Alunos')
    data = c.fetchall()
    for row in data:
        print(row)

def add_values():
    c.execute(
        """
        INSERT INTO Alunos 
        VALUES
            ('Joao', 10114385, 28, 2022, 'Formado'),
            ('Pedro', 13100001, 25, 2020, 'Trancamento'),
            ('Maísa', 11280821, 26, 2023, 'Cursando'),
            ('Patrick', 14204123, 24, 2022, 'Desistiu')
        """
    )

print('>> Lendo a base de dados...')
read_from_db()

print('\n>> Adicionando novos valores...')
add_values()

print('\n>> Lendo a base de dados com novos valores...')
read_from_db()

print('\n>> Aplicando filtros...')

print('\n>> Quem trancou o curso?')
c.execute("SELECT Nome FROM Alunos WHERE Situacao == 'Trancamento'")
data = c.fetchall()
for row in data:
    print(row[0])

print('\n>> Quem entrou após 2012?')
c.execute("SELECT Nome FROM Alunos WHERE Ingresso > 2012")
data = c.fetchall()
for row in data:
    print(row[0])

print('\n>> Qual a idade de Patrick?')
c.execute("SELECT Idade FROM Alunos WHERE Nome == 'Patrick'")
data = c.fetchall()
for row in data:
    print(row[0])

print("\n>> Alterar o nome de Pedro para Carlos (UPDATE)")
c.execute("UPDATE Alunos SET Nome = 'Carlos' WHERE Nome == 'Pedro'")
read_from_db()