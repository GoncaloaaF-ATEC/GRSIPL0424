"""

void olaMundo(){
    sout("Ola mundo");
}

"""

def ola_mundo():
    print("Ola mundo")

ola_mundo()
ola_mundo()
ola_mundo()

print("---" * 3)
def ola_mundo():
    print("Ola mundo")

def ola_mundo2(nome):
    print(f"Ola mundo, {nome}")

ola_mundo2("Gonçalo")
ola_mundo2("Rui")
ola_mundo2("Ana")

print("---" * 3)

ola_mundo2(2000)

print("---" * 3)

def ola_mundo3(nome: str):
    print(f"Ola mundo 3, {nome.capitalize()}")


ola_mundo3("nome")
# ola_mundo3(2000)

print("---" * 3)

def ola_mundo4(nome: str, ano:int):
    n = nome.capitalize()
    print(f"Ola mundo 3, {n} em {ano}")



ola_mundo4("o meu nome", 2022)
print("---" * 3)

def ola_mundo5(nome: str, ano:int):
    n = nome.capitalize()
    return f"Ola mundo 5, {n} em {ano}"

resp = ola_mundo5("o meu nome return", 2022)
print(resp)
print(resp.upper())

print("---" * 3)

def soma(val1:int, val2:int) -> int:
    soma = val1 + val2
    return soma

print(soma(10, 20))


def soma2(val1:int, val2:int = 30) -> int:
    soma = val1 + val2
    return soma

print(soma2(10))


print("---" * 3)

def soma3(val1:int, val2:int = 30, val3:int = 10) -> int:
    soma = val1 + val2 + val3
    return soma

print(soma3(10))
print("---" * 3)


print(soma3(10, val3=100))