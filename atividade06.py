class Conta():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def creditar(self, valor):
        self.saldo += valor
        return self.saldo

    def debitar(self, valor):
        self.saldo -= valor
        return self.saldo


class ContaPP(Conta):
    def __init__(self, numero, saldo, cliente, saldoMinimo):
        super().__init__(numero, saldo, cliente)
        self.saldoM = saldoMinimo

    def atualizarSaldo(self):
        if self.saldoM < 300:
            return f'Saldo Insuficiente'
        else:
            return f'Saldo Suficiente'

    def mostraSaldoMinimo(self):
        return f'Seu Saldo Minimo é {self.saldoM}'


class Cinvest(Conta):
    def __init__(self, numero, saldo, cliente, dt_invest, periodo):
        super().__init__(numero, saldo, cliente)
        self.invest = dt_invest
        self.periodo = periodo


# conta = Conta(1, 1500, 1)
conta2 = ContaPP(1, 2000, 2, 2000)
# print(conta.creditar(300))
# print(conta.debitar(200))
print(conta2.debitar(1700))
# print(conta2.atualizarSaldo())
print(conta2.mostraSaldoMinimo())
