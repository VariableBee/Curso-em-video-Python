
# Um professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input('Nome:'))
n2 = str(input('Nome:'))
n3 = str(input('Nome:'))
n4 = str(input('Nome:')) 

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação será:')
print(lista)
