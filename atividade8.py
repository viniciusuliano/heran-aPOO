class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimiValor(self):
        return f'R${self.valor}'


class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorAdicional(self):
        valor_vip = self.valor + self.adicional
        return f'R${valor_vip}'


class Normal(Ingresso):
    def __init__(self, valor, valor_normal):
        super().__init__(valor)
        self.valor2 = valor_normal

    def imprimiIngressoNormal(self):
        return f'R${self.valor2}'


class CamaroteInferior(Vip):
    def __init__(self, valor, adicional, localização):
        super().__init__(valor, adicional)
        self.localização = localização

    def mostraLocal(self):
        return f'LOCAL - ALA [{self.localização}]'


class CamaroteSuperior(Vip):
    def __init__(self, valor, adicional):
        super().__init__(valor, adicional)

    def mostraValor(self):
        return f'VALOR - [R${self.valor}] + ADICIONAL [R${self.adicional}]'


ingresso = Ingresso(50)
print(f'INGRESSO - {ingresso.imprimiValor()}')

vip = Vip(50, 30)
print(f'INGRESSO VIP - {vip.imprimiValor()}')
print(f'ADICIONAL - {vip.valorAdicional()}')

normal = Normal(50, 30)
print(f'INGRESSO NORMAL - {normal.imprimiIngressoNormal()}')

inferior = CamaroteInferior(70, 0, 'B')
print(inferior.mostraLocal())

superior = CamaroteSuperior(150, 50)
print(superior.mostraValor())
