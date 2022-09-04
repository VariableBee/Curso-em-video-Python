
# MÓDULOS/BIBLIOTECA

# Bibliotecas disponíveis: https://docs.python.org/3.10/library/index.html

import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual {}'.format(num, floor(raiz)))