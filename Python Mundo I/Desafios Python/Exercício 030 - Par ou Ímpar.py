
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

num = int(input('Digite um número qualquer: '))
result = num % 2  # O Resto da divisão de qualquer número PAR por 2 é 0 e IMPAR é 1
if result == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR'.format(num))


