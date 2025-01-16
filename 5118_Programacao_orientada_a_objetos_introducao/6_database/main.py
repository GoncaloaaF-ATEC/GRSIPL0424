import sqlite3 as sql
from pessoa import Pessoa

# criar conn/ base dados
conn = sql.connect('database.db')

# criar cursor
cur = conn.cursor()

# exec

cur.execute("""
CREATE TABLE if not exists Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
""")


cur.execute("""
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)  
VALUES 
    (1, 'Silva', 'João', 'Rua das Flores, 123', 'Lisboa'),
    (2, 'Santos', 'Maria', 'Avenida Central, 456', 'Porto'),
    (3, 'Costa', 'Pedro', 'Praça da Alegria, 789', 'Coimbra'),
    (4, 'Ferreira', 'Ana', 'Travessa do Sol, 321', 'Faro'),
    (5, 'Rodrigues', 'Luís', 'Alameda das Árvores, 654', 'Braga');

""")

conn.rollback()

resp = cur.execute("SELECT * FROM Persons")

# print(resp.fetchone())
# print(resp.fetchone())

dados = resp.fetchall()

listaPessoas:list[Pessoa] = []

for d in dados:
    novaPessoa = Pessoa(d)
    listaPessoas.append(novaPessoa)

print(listaPessoas[0])



"""
Lista de comandos

.connect() -> Conecta ao servidor/ cirar a base de dados SQLite3
.cursor() -> Cria o cursor que vai executar as operações
.execute() -> Execura as querys
.commit() -> confirma uma alteração na base de dados
.rollback() -> anula uma alteração na base de dados
.fetchall(), .fetchone(), .fetchany() -> ir buscar os resultados a resposta do execute
"""