
# Um professor quer sortear um dos quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

a1 = str(input('Digite um nome:'))
a2 = str(input('Digite um nome:'))
a3 = str(input('Digite um nome:'))
a4 = str(input('Digite um nome:'))

lista = [a1, a2, a3, a4]
print('O aluno escolhido foi {}:'.format(random.choice(lista)))

