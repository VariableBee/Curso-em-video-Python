

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digito separados.
# Exemplo de como calcular unidade, decimal, centena e milhar

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(' '*20)
print('Analisando o número {}, ele possuí:'.format(num))
print('{} Unidades'.format(u))
print('{} Dezenas'.format(d))
print('{} Centenas'.format(c))
print('{} Milhares'.format(m))


