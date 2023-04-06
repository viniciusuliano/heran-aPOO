class Animal():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer(self):
        return f'{self.nome} está comendo'


class Gato(Animal):
    def __init__(self, nome, peso, miar):
        super().__init__(nome, peso)

        self.miar = miar

    def miar(self):
        return self.miar


class Cachorro(Animal):
    def __init__(self, nome, peso, latir):
        super().__init__(nome, peso)

        self.latir = latir

    def latir(self):
        return self.latir


gato = Gato('Jeremias', 4, 'MIAU')
cachorro = Cachorro('Marvin', 7, 'AUAU')

print(gato.miar)
print(gato.comer())
print(cachorro.comer())
print(cachorro.latir)
