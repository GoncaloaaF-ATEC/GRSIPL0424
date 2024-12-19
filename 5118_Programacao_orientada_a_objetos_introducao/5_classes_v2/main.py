from pessoa import Pessoa, Pessoa3, Morada


p = Pessoa("Joao", 2001, "j@sapo.pt", "123213231", "Lisboa")


print(p.nome)

p.nome = "Carlos"

print(p.nome)


print(p.get_idade())



p3 = Pessoa3("Gonçalo",
             Morada(
                 "rua 1",
                    31,
                    123,
                    "2134-123"))