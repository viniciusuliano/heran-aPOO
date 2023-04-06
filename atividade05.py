class Forma:
    def __init__(self, area1):
        self.tamanho = area1

    def area(self):
        return self.tamanho


class Retangulo(Forma):
    def __init__(self, area1, altura, largura):
        super().__init__(area1)
        self.altura = altura
        self.largura = largura

    def calculoArea(self):
        area = self.altura * self.largura
        return area


class Circulo(Forma):

    def __init__(self, area1, raio):
        super().__init__(area1)
        self.raio = raio

    def calculoArea(self):
        area = 3.14 * (self.raio ** 2)
        return area


retangulo = Retangulo(30, 10, 20)
circulo = Circulo(10, 10)

print(retangulo.calculoArea())
print(circulo.calculoArea())
