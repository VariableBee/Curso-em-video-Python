
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número'))
b = int(input('Digite outro número'))
c = int(input('Digite um terceiro número'))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado entre {}, {} e {} foi {}'.format(a, b, c, menor))
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado entre {}, {} e {} foi {}'.format(a, b, c, maior))
