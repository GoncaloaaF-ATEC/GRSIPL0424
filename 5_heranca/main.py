from modelo import Pessoa, Aluno
import uuid

p = Pessoa(nome="Gonçalo", idade=20)

print(p.getNome())
# print(p.__nome)

p.setNome("Novo Nome")
print(p.getNome())


print(p)


al = Aluno(nome="Carlos", idade=40, turma="GRSIPL")

print(al)