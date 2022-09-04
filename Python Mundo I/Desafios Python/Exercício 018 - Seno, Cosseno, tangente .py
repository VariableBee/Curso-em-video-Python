
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = float(input('Ângulo:'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {} graus tem o seno de {:.2f}'.format(a, s))
print('O ângulo de {} graus tem o cosseno de {:.2f}'.format(a, c))
print('O ângulo de {} graus tem a tangente de {:.2f}'.format(a, t))
