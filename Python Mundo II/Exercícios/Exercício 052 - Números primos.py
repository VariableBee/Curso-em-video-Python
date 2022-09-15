
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
primo = True
for c in range(1, num):# 1, 2, 3, 4 ... num
    if num % c: # Se ele for divisível por qualquer valor entre 1 e ele próprio, NÃO É PRIMO
        primo = False

if primo == True:
    print(num + 'É PRIMO!')
else:
    print(num + 'NÃO É PRIMO!')

     