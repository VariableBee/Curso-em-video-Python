
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127.
# O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um número:'))
print('O número {} possui {} como sua parte inteira'.format(num, trunc(num)))

num = float(input('Digite um valor:'))
print('O número {} possui {} como sua parte inteira'.format(num, int(num)))

 
