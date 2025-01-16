import uuid

'''

herança 
encapsulamento 
visibilidade 
override -> reescrever metodos
polimorfismo

'''
class Pessoa:

    def __init__(self, nome, idade):
        self._id = uuid.uuid4() # portect
        self.__nome = nome ## pvt
        self.idade = idade

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f'Pessoa: Nome: {self.__nome}, idade: {self.idade}'



class Aluno(Pessoa):

    def __init__(self, nome: str, idade: int, turma:str):
        super().__init__(nome, idade)
        self.turma = turma


    def __str__(self):
        return f'Aluno id - {self._id} :\nnome: {self.getNome()}, turma: {self.turma}, idade: {self.idade}'
