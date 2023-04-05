class Veiculo():
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    
class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, qtd_portas):
    super().__init__(marca, modelo, ano)
    self.qtdportas = qtd_portas

  def mostraqtdPortas(self):
    return f'QUANTIDADE PORTAS: {self.qtdportas}'

class Moto(Veiculo):
  def __init__(self, marca, modelo, ano, cilindradas):
    super().__init__(marca, modelo, ano)
    self.cilindrada = cilindradas
    
  def mostraCilindradas(self):
    return f'CILINDRADAS: {self.cilindrada}'
  

veiculo = Carro('Volkswagen', 'Sedan', 2022, 4)
print(f'MARCA: {veiculo.marca} MODELO: {veiculo.modelo} ANO: {veiculo.ano} PORTAS: {veiculo.qtdportas}')

veiculo2 = Moto('Honda', 'CG', '2023', 1500)
print(f'MARCA: {veiculo2.marca} MODELO: {veiculo2.modelo} ANO: {veiculo2.ano} CILINDRADAS: {veiculo2.cilindrada}')