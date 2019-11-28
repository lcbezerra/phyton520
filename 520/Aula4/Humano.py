#!/usr/bin/python3

class Humano:
    # atributos
    # pernas=2
    # bracos=2
    # cabeca=1
    _PI = 3.1415

    # metodos magicos
    def __init__(self, nome):      #método construtor
        # atributos do objeto
        self.pernas = 2
        self.braco = 2
        self.nome = nome
        self.saldo = 0


    # metodo
    def acidente(self):
        self.pernas -= 1           #palavra 'self' se refencia ao proprio objeto
    def saldo_bancario(self):
        if self.pernas < 2 and self.nome == 'Carlos':
            self.saldo -= 10000,
            print('Você está de férias permanentes')
            if random.randint(1,10 == 9):
                self.saldo *= -1
        else:
            print ('Você não é o Carlos, beleza')
            self.saldo += 10000
            print(f'Você agora tem {self.saldo}')

carlos = Humano('Carlos')         #criando um objeto
# carlos._PI = 4

# print(carlos._PI)

# print(carlos.pernas) # Acessando um atributo
# carlos.pernas = 1    # Mudando um atributo

print(carlos.pernas) # printa com Carlos com 1 perna

# print(Humano._PI)

carlos.acidente()
print(carlos.pernas)
carlos.saldo_bancario()
print(carlos.saldo)