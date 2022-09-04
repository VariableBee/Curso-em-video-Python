
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nome = str(input('Nome do aluno:'))
mat = str(input('Matéria:'))
num3 = float(input('Nota da P1:'))
num4 = float(input('Nota da p2:'))
 
print('A média de {} em {} foi {}'.format(nome, mat, (num3 + num4) / 2))
