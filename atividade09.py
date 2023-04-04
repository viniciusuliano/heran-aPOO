class Funcionario:
    def __init__(self, nome, endereço, telefone, email):
        self.nome =nome
        self.endereço =endereço
        self.telefone =telefone
        self.email =email
    
    def exibirDados(self):  
        return f'{self.nome} - {self.endereço} - {self.telefone} -{self.email}'
    

class Assistente(Funcionario):
    def __init__(self, nome, endereço, telefone, email, matricula):
        super().__init__(nome, endereço, telefone, email)
        self.matricula = matricula

    def exibirMatricula(self):
        return f'MATRICULA - [{self.matricula}]'

class Tecnico(Assistente):
    def __init__(self, nome, endereço, telefone, email, matricula, bonus):
        super().__init__(nome, endereço, telefone, email, matricula)
        self.bonus = bonus


    def bonusSalarial(self):
        return f'MATRICULA - [{self.matricula}] BONUS - [{self.bonus}]'

class Administrativo(Assistente):
    def __init__(self, nome, endereço, telefone, email, matricula, turno):
        super().__init__(nome, endereço, telefone, email, matricula)
        self.turno = turno

    def adicionalTurno(self, dia):
        if self.turno == dia:
            return  f'MATRICULA - {self.matricula} [SEM ADICIONAL]'
        else:
            f'MATRICULA - {self.matricula} [ADICIONAL JÁ CONTABILIZADO]'
        
    

funcionario = Funcionario('Jean', 'Rua Paulo Ponick', 34343434, 'jeanzinho@gemail.com')
print(funcionario.exibirDados())

assistente = Assistente('João', 'Rua Bento Torquato da Rocha', 23232323, 'joaozinho@gemail.com', 111111)
print(assistente.exibirMatricula())

tecnico = Tecnico('Mateus', 'Rua Pio XII', 32323232, 'mateuzinho@gemail.com', 121212, '$150')
print(tecnico.bonusSalarial())


adm = Administrativo('Tiago', 'Rua Bolinhas Bolinhas', 33333333, 'tiaguinho@gemail.com', 131313, 'Noite')
print(adm.adicionalTurno('Noite'))
