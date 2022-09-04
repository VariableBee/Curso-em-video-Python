
# Crie um programa que leia o nome de uma pessoa e diga se ele tem "silva no nome.

nome = str(input('Digite um nome:')).strip()
print('Nesse nome tem Silva? {}'.format('SILVA'in nome.upper()))
