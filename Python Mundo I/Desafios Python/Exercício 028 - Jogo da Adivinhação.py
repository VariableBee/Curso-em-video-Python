
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5.
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}. TENTE DE NOVO!'.format(computador, jogador))

