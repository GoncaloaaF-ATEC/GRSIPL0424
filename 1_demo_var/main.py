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

print(f"---" * 3)
in_nome = input("Qual o seu nome: ")

print(f"ola {in_nome}, bem vindo!")

print(in_nome.islower())


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

# cond





# loops


