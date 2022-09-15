
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual= date.today().year
maiores = 0  # Variável de controle
menores = 0 # Variável de controle

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º  pessoa: '.format(c)))
    if (anoatual - ano) >=18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas atingiram a maior idade, enquanto {} pessoas ainda são menores de idade.'.format(maiores, menores))