class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostraNome(self):
        return f'{self.nome} - {self.idade}'

class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro
    
    def fazerCompras(self, compras):
        gastar = self.dinheiro - compras
        
        if gastar > 100:
            return 'Está gastando demais!!!'
        else:
            return 'Pode gastar mais'
        

class Pobre(Pessoa):
    def __init__(self, nome, idade, trabalha):
        super().__init__(nome, idade)
        self.trabalha = trabalha

    def vaiTrabalhar(self):
        return 'Está na hora de trabalhar'


class Miseravel(Pessoa):
    def __init__(self, nome, idade, mendigar):
        super().__init__(nome, idade)
        self.mendigar = mendigar

    def mendiga(self):
        return f'Está {self.mendigar}'
    
pessoa = Pessoa('João', 50)
print(pessoa.mostraNome())

rica = Rica('José', 60, 500)
print(rica.fazerCompras(150))

pobre = Pobre('Luiz', 30, 'Trabalho')
print(pobre.vaiTrabalhar())

mendiga1 = Miseravel('Lopes', 25, 'mendigando')
print(mendiga1.mendiga())