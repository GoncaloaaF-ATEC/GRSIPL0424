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



arr: list[Pessoa] = []

arr.append(p)
arr.append(al)
print("-----")
# print(arr[1].turma) <- funiona mas nao fazer
print("-----")
for elm in arr:
    print(isinstance(elm, Aluno))


print("-----")
print(issubclass(Pessoa, Aluno))
print(issubclass(Aluno, Pessoa))