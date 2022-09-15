
# Refaça o desafio 035 dos triângulos, acresentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais.
# Isóceles: dois lados iguais
# Escaleno: todos os lados são diferentes.

print('-='*20)
print('Analisador de Triângulo. . .')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
    if r1 and r2 == r3:
        print('Esse triângulo é EQUILÁTERO! Pois seus lados tem valores iguais!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é ISÓCELES! Pois apenas dois de seus lados tem valores iguais!')
    else:
        print('Esse triângulo é ESCALENO! Todos os seus lados tem valores diferentes!')
else:
    print('Estes segmentos não podem formar um triângulo')
