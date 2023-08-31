# Classe Pessoa.
# Crie uma classe chamada Pessoa que tenha atributos como nome, idade e profissão.
# Crie um método que imprima uma saudação com as informações da pessoa.
class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        print(f'Oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}')

ana = Pessoa('Ana', 26, 'modelo')
ana.saudacao()

joao = Pessoa('João', 30, 'veterinário')
joao.saudacao()

maria = Pessoa('Maria', 23, 'dentista')
maria.saudacao()