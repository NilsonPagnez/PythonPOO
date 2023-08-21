class Pessoa: 
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome =sobrenome

p1 = Pessoa("Nilson", "Pagnez")

print(p1.nome)