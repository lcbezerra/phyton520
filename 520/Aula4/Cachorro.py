#"/usr/bin/python3"

class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
        pass

    def viver(self):
        print('Estou vivo!!')

class Cachorro(Animal):
    ''' Abstração de um cachorro


    Cria um cachorro, baseado nos conceitos definidos em sala.'''
    _DNA = 'Cachorro'                   # Definindo uma constante protegida

    def __init__(self, nome, idade, cor, raca='Vira-lata', porte='Médio'):
        # Atributos obrigatórios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.porte = porte

    
        # Atributos padrão para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.focinho = True # Valores únicos como true e false 
        self.lingua = True #
        self.olhos = 2
        self.rabo = True
        print(f'Cachorro {nome}, Construído com sucesso!')



    # O que faz - Métodos
    def latir(self):
        if self.lingua:
            print(f'{self.nome} Au Au Au')
    
    def comer(self):
        print(f'{self.nome} Comendo...')

    def cheirar(self):
        if self.lingua:
            print(f'{self.nome} Cheirando...')

    def cagar(self):
        print(f'{self.nome} Cagando...')

    def dormir(self):
        print(f'{self.nome} Dormindo...')

    def __del__(self):                                #método destrutor                  
        print(f'Descanse em paz {self.nome}')

    def __str__(self):
        return 'Constrói um cachorro'


# print(Cachorro)
    

# rex= Cachorro()
# rex.viver()
# rex.latir()






# print()
