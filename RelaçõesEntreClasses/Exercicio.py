class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

    def ligar(self):
        return f'{self.nome} está ligando'


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


corsa = Carro('Corsa')
v8 = Motor('V8')
volkswagen = Fabricante('Volkswagen')

corsa.motor = v8
corsa.fabricante = volkswagen

print(corsa.motor.ligar())
