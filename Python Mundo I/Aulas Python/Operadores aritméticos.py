
# OPERADORES ARITMÉTICOS:

# + Adição 
# - Subtração 
# * Multiplicação 
# / Divisão.
# O operador para igualdade é "=="

# OPERADORES DE POTÊNCIA:

# ** Potência
# // Divisão inteira 
# % Resto da divisão

# ORDEM DE PROCEDÊNCIA:
# 1: ()
# 2: **
# 3: * | / | // | %
# 4: + | -

# EXEMPLOS:
n = 5 + 3 * 2
n1 = 3 * 5 + 4 ** 2
n2 = 3 * (5 + 4) ** 2

print(n2)

x = int(input('Digite um valor'))
y = int(input('Digite outro valor'))

s = x + y
m = x * y
d = x / y
e = x ** y
di = x // y

print('A soma é:{}, o produto é {}, a divisão é {}'.format(s, m, d), end='')  # END='' Quebra a linha.
print('A Divisão inteira é {}, e a potência é {}'.format(di, e))

# OPERAÇÕES ARITMÉTICAS COM STR:
print('Oi' + 'Olá')
print('Oi' * '5')
print('=' * 20)

# OPERAÇÕES COM .FORMAT:
# {:20}
# {:<20}
# {:.2f}
# {:=^20}


 
