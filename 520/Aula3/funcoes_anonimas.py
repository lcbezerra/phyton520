#!/usr/bin/python3

# def mostrar_hello_world():
#     print('hello world')

# mostrar_hello_world()

# #Criando uma estrutura de funções
# def menu():
#     print('Escolha a opção: ')
#     print('1 - Registrar produto')
#     print('2 - Consultar saldo do caixa')
#     print('3 - Abrir caixa registradora')
#     print('4 - Fechamento do mês')
#     return input('digite a opção desejada: ')

# def registrar_produto():
#     print('Produto registrado')

# def consultar_saldo():
#     print('Saldo é R$ x')

# def abrir_caixa():
#     print('Abrindo')

# def fechamento():
#     print('Fechando')

# #Estrutura principal
# while True:
#     print ('Caixa Registradora')
#     opcao = menu()
#     if opcao == '1':
#         registrar_produto() #Função 1      # 'pass' faz ignorar uma linha, passa sem executar função
#     elif opcao == '2':
#         consultar_saldo() #Função 2
#     elif opcao == '3':
#         abrir_caixa() #Função 3
#     elif opcao == '4':
#         fechamento() #Função 4
#     else:
#         break #Função 5
#     input()                          #evita que volta, da um pause (fica aguardando enter para voltar o loop)



### FUNÇÕES ANÔNIMAS
var = lambda x : x*2
print(var(2))


numeros = list(range(1,100))

def dobro(x):
    return x * 2# numeros = [list(range(1,100))]
# print (numeros)


print(list(map(dobro,numeros)))

# numeros = [x for x in range(1,100)]
# print (numeros)


################# pode mudar o dobro por lambda


print(list(map(lambda x : x + 3,numeros)))





