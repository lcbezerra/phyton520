#!/usr/bin/python3


import random                        # pega módulo inteiro (módulo que trata operações de aleatoriedade)
import os                            # possibilita usar funcionalidades do s.o.
import sys                           # acessa variáveis de sistema e alguns parâmetros específicos
import datetime                      # cuida de data e hora
import json                          # codificar e/ou decodificar um arquivo no formato JSON
import csv                           # trabalha com planilhas


############## MÓDULO OS
print(os.listdir('/home/developer'))  # lista os diretórios
# print(os.rename('nomeerrado.txt','nomecerto.txt'))

os.system('ls')                      # automatiza funções do sistema
os.system('sudo systemctl start apache2')

############## MÓDULO RANDOM
print('módulo random: ', random.randint(1,90))    #retorna numero inteiro de um rand a até b

############## MÓDULO SYS 
print(sys.platform)                      # mostra o s.o.
print(sys.builtin_module_names)          #mostra os modulos do sistema
print(sys.argv)                          

#sys.exit                                 #sair do sistema


############## MÓDULO DATETIME
print(datetime.datetime.now())
print(datetime.timedelta(7))

print(datetime.time(14,0,0))
print(datetime.date(2019,5,4))

# EXEMPLO PRÁTICO    ### controle de acesso por hora ---- a partir de 1 hora não permite o acesso
acesso = datetime.datetime(2019,1,22,00,00,00)         
atual = datetime.datetime(2019,1,22,1,1,00)       

print(atual - acesso)

print(acesso)
print(atual)

if (atual - acesso).total_seconds() > 3600:
    print('seu token expirou')
else:
    print('acesso liberado')

####################### MÓDULO JSON

print(json.dumps({
    "nome":"Daniel",
    "sobrenome":"Silva"},indent=4))

print(json.loads('{"nome":"Daniel","sobrenome":"Silva"}'))



