class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)

        self.salario = salario
    
    def aumento(self):
        aumento = self.salario * 0.25
        novo_salario = self.salario + aumento
        return novo_salario
    
funcionario = Funcionario('Vinicius', 20, 1500)
print(funcionario.aumento())
