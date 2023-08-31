class Animal():
    def __init__(self, patas, olhos, sons):
        self.patas = patas
        self.olhos = olhos
        self.sons = sons

class Cachorro(Animal):
    def qnt_patas(self , patas):
        print(f'O número de patas é: {self.patas}')

    def qnt_olhos(self,olhos):
        print(f'A quantidade de olhos é: {self.olhos}')

    def som_emitido(self,sons):
        print(f'O som emitido é: {self.sons}')

class Gato(Cachorro):
    pass

cachorro = Cachorro(4, 2, 'auau')
print("Cachorro:")
cachorro.qnt_patas(4)
cachorro.qnt_olhos(2)
cachorro.som_emitido('auau')

print()

gato = Gato(4,2,'miau')
print('Gato:')
gato.qnt_patas(4)
gato.qnt_olhos(2)
gato.som_emitido('miau')

