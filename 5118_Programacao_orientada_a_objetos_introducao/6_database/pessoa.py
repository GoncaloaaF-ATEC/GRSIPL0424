class Pessoa:

    def __init__(self, dados):

        self.PersonID = dados[0]
        self.LastName = dados[1]
        self.FirstName = dados[2]
        self.Address = dados[3]
        self.City = dados[4]


    def __str__(self):
        return f"nome: {self.LastName}\nidade: {self.PersonID}\ntelefone: {self.City}"