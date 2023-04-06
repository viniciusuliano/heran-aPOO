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

        return f'AUMENTO[{novo_salario}]'

class Estagiario(Empregado):

    def __init__(self, codigo, nome, email, salario):
        super().__init__(codigo, nome, email, salario)
    
    def mostraSalarioComDesconto(self, desconto):
        self.desconto = desconto
        aumento = self.salario - desconto
        return f'AUMENTO COM DESCONTOS [{aumento}]'

class Chefe(Empregado):
    
    def __init__(self, codigo, nome, email, salario):
        super().__init__(codigo, nome, email, salario)

    def mostraSalarioComBeneficios(self, beneficios):
        self.beneficios = beneficios
        aumento = self.salario + beneficios 
        return f'AUMENTO COM BENEFICIOS [{aumento}]'


empregado1 = Empregado(111, 'Jeremias', 'jeremias_josias@gemail.com', 2000)
print(empregado1.mostraSalario())
print(empregado1.percentualAumento(25))

estagiario1 = Estagiario(112,'Josue', 'josue_josias@gemail.com', 1100)
print(estagiario1.mostraSalario())
print(estagiario1.mostraSalarioComDesconto(100))


chefe = Chefe(113, 'Isaias', 'isaias_isael@gemail.com', 5000)
print(chefe.mostraSalario())
print(chefe.mostraSalarioComBeneficios(1000))