
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segunto entre eles.

from time import sleep
print()
print('Os fogos de artifício estão prestres a estourarem! Vamos iniciar a contagem regressiva!!!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Insira barulho de fogos.')