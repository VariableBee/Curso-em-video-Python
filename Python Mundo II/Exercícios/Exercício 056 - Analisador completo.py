
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 
# A média de idade do grupo.
# O nome do homem mais velho.
# Quantas mulheres tem menos de 21 anos?

from datetime import date
mulheres = 0
maisvelho = 0
somaidade = 0
for c in range(1, 5):#Repetir 4x
    print(' ----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome? ')).upper()
    ano = int(input('Idade '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    
    idade = date.today().year - ano
    somaidade += idade
    if sexo == 'F':
        mulheres += 1
    if idade > maisvelho and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    
média = somaidade / 4
print('A média da idade do grupo é {}'.format(média))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('Existem {} mulheres no grupo'.format(mulheres))

