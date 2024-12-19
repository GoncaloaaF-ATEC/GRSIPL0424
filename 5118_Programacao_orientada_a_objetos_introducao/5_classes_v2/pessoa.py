"""
nome
data_nacimento
email
telefone
morada

+351 3424234324
+1      .....
+55 .....

"""

"""

pais
    id
    pais
    code
"""

"""

Telefone
    id
    pais_id
    numero

Pessoa
    id
    ...
    Telefone_id

"""

"""

this <=> self 
"""


class Pessoa:

    def __init__(self, nome: str,
                 data_nacimento: int,
                 email: str,
                 telefone: str,
                 morada: str):

        self.nome = nome
        self.ano_nacimento = data_nacimento
        self.email = email
        self.telefone = telefone
        self.morada = morada

    def get_idade(self):
        return 2024 - self.ano_nacimento



"""

Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material <- done
Métodos: 
    trocaCor - Done
    mostraCor - Done

"""

class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str ):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        print(f"A cor da bola é {self.cor}")


"""
Classe Quadrado: Crie uma classe que modele um quadrado: <- done

Atributos: Tamanho do lado
Métodos: 
    Mudar valor do Lado -> done
    Retornar valor do Lado -> done
    calcular Área;

"""


class Quadrado:

    def __init__(self, lado: float):
        self.lado = lado

    def mudar_lado(self, novo_lado: float):
        if novo_lado > 0:
            self.lado = novo_lado

    def get_lado(self) -> float:
        return self.lado

    def calcular_area(self):
        return pow(self.lado, 2) # <=> self.lado * self.lado



class Morada:

    def __init__(self, rua:str, num:int, apt: str, cp:str):
        self.rua = rua
        self.num = num
        self.apt = apt
        self.cp = cp


class Pessoa3:

    def __init__(self, nome:str, morada:Morada):
        self.nome = nome
        self.morada = morada


class Pessoa4:

    def __init__(self, nome: str, rua:str = None,  num:int= None, apt: str= None, cp:str= None, morada:Morada = None ):
        self.nome = nome
        if morada == None:
            self.morada = Morada(rua, num, apt, cp)
        else:
            self.morada = morada

    def get_rua(self) -> str:
        return self.morada.rua



# Crie uma Agenda de contatos em py (pode e deve ser so  linha de comandos)
# add ct
# listar ct
# remover ct
# pesquisar

# restrições
# nao pode adicioanr contactos com num duplicado
# o telefone tem de ter pelo menos 7 num
