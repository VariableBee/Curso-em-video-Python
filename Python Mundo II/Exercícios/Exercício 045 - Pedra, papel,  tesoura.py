
from time import sleep
from random import randint

print('-=-' * 20)
print('VAMOS JOGAR JO! KEN! PO! Tente me vencer!...')
print('-=-' * 20)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jokenpo = ['pedra', 'papel', 'tesoura']
jogador = int(input('Qual é sua jogada? '))
computador = randint(0, 2)

print()
sleep(1)
print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')
sleep (2)
print()
print('-='*20)
print('Computador jogou {}'.format(jokenpo[computador])) 
print('O jogador jogou {}'.format(jokenpo[jogador]))
print('-='*20)
print()

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('EU VENCI HAHAHAHA')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print('EU VENCI HAHAHAHA')
    else:
        print('JOGADOR VENCEU!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 1:
        print('EU VENCI HAHAHAA')
    else:
        print('JOGADOR VENCEU!')
        
    
    