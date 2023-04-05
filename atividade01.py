class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def mostraPessoa(self):
    return f'NOME: {self.nome} IDADE: {self.idade}'
  
class Aluno(Pessoa):
  def __init__(self, nome, idade, nota):
    super().__init__(nome, idade)
  
    self.nota = nota  
  
  def mostraNota(self):
    return f'NOTA: {self.nota}'
  
pessoa = Aluno('Vinicius', 20, 8.5)
print(pessoa.mostraPessoa())
print(pessoa.mostraNota())