class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.salario = salario

    def mostraSalario(self):
        return f'SALÁRIO [{self.salario}]'
    
    def percentualAumento(self, percentual):
        percentual = percentual/100.0
        aumento = percentual * self.salario
        novo_salario = aumento + self.salario

        return novo_salario

class Estagiario(Empregado):

    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.desconto = desconto
    
    def mostraSalarioComDesconto(self):
        return self.mostraSalarioComDesconto() + f"COM DESCONTO [{self.salario - self.desconto}]"


empregado1 = Empregado(111, 'Jeremias', 'jeremias_josias@gemail.com', 2000)
print(empregado1.mostraSalario())
print(empregado1.percentualAumento(25))

estagiario1 = Estagiario(112,'Josue', 'josue_josias@gemail.com', 1100, 100)
print(estagiario1.mostraSalario())
print(estagiario1.percentualAumento(20))