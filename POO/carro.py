# Classe Carro
# Crie uma classe chamada Carro com atributos como marca, modelo e ano.
# Crie um método para acelerar o carro.

class Carro():
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def caracteristicas(self):
        print(f'Esse carro é da marca {self.marca}, modelo {self.modelo}, do ano {self.ano} e está andando a uma velocidade de {self.velocidade} Km/h')

    def acelerar(self, km_acelerados):
        self.velocidade += km_acelerados

carro = Carro('Jeep', 'Renegade', 2015, 70)
carro.acelerar(30)
carro.caracteristicas()
