# cmt

"""

cmt linha 1
cmt linha 2
...
cmt linha n

"""

'''

cmt linha 1
cmt linha 2
...
cmt linha n

'''


# var

nome = "Gonçalo"
idade = 38

# nome = 29 # deve ser evitado -> Não Usar <-

# print e  concat

print(nome)
print(idade)

print(nome,"tem", idade, "anos")

print(nome + " tem "+  str(idade) +  " anos")

print(f"{nome.upper()} tem {idade} anos")

num = 10.123

print(f"{num}")
print(f"{num.__round__(0)}")
print(f"{num.__floor__()}")
print(f"{num.__ceil__()}")

# op var


op1 = 10 + 5
op2 = 10 - 5
op3 = 10 / 5


op4 = 10 / 3
print(f"{op4}")

op5 = 10 // 3
print(f"{op5}")

op6 = 10 % 3 #  10 mod 3
print(f"{op6}")

# input
'''


print(f"---" * 3)
in_nome = input("Qual o seu nome: ")

print(f"ola {in_nome}, bem vindo!")

print(in_nome.islower())
'''

# tipos de dados

i = 12
f = 212.1212
s = "dadsdasd"
bt = True
bf = False

# Type hint

nome: str = "Gonçalo"
num: int = 10
numD: float = 102.2
b: bool = True


# input v2
'''
num1 = input("num 1: ")
num2 = input("num 2: ")

# tratar dados

num1 = int(num1)
num2 = int(num2)

soma = num1 + num2
print(soma)
'''
# cond
print("---"*5)
idade = 10

if idade > 18:
    print("Adulto")
else:
    print("Menor")


idade = 16
if idade >= 18:
    print("Adulto")

elif idade > 15:
    print("Teen")

else:
    print("Menor")



if True:
    pass
    # cria um bloco vazio

print("----" * 5)

idade = 12
match idade:
    case 10:
        print("menor")
    case 15:
        print("teen")
    case _:
        print("maior")



# || - or
# && - and


#range

range(10) # 0 ... 9 <-> range(n) -> 0... n-1

range(10, 100) # 10 ... 99 <-> range(m, n) -> m... n-1

range(10, 100, 5)# 10 ... 99, de 5 em 5 <-> range(m, n, s) -> m... n-1 com step de s

range(0, 100, 5) # 0 ... 99, de 5 em 5 <-> range(m, n, s) -> m... n-1 com step de s

# loops - For

for i in range(10, 100, 5):
    print(i)


for i in "Gonçalo":
    print(i)

for i in enumerate("Gonçalo"):
    print(i)


#  tuplo

nome = (10, "Gonaçlo")

print(nome)
print(nome[0])
print(nome[1])

print("----" * 5)

id, nome = (10, "Gonaçlo")
print(id)
print(nome)

tp1 = (10, "Gonaçlo")
nomes = (
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda",
    "Fábio", "Gabriela", "Henrique", "Isabel", "João",
    "Karla", "Luís", "Marta", "Nuno", "Olga"
)

print("----" * 5)

for nome in nomes: # for (nome: nomes){}
    print(nome)

tp3 = nomes + tp1

print(tp3)

print("----" * 5)
# loops - while

i = 10
while i > 0:
    print(i)
    if i == 4:
        break

    i = i - 1

# loops - For

print("----" * 5)
for i in range(10, 100, 3):
    if i % 2 == 0:
        continue

    print(i)


    if i == 61:
        break


# len
print("----" * 5)

nomes = (
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda",
    "Fábio", "Gabriela", "Henrique", "Isabel", "João",
    "Karla", "Luís", "Marta", "Nuno", "Olga"
)

print(len(nomes))
print(len("Gonçalo Feliciano"))

print("----" * 2)


print(nomes.__len__())
print("Gonçalo Feliciano".__len__())