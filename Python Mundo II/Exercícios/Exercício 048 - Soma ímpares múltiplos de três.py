
# Faça um programa que calcule a soma entre todos os números ímpares que são de múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Aqui estão a soma dos números ímpar múltiplos de 3: ')

soma = 0 #acumulador faz a soma
cont = 0 #contador adiciona de 1 em 1...
for c in range(1, 501, 2):
    if c%3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}. Espero ter ajudado'.format(cont, soma))
