
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

cont = 0
soma = 0
for c in range(1, 7): 
    num = int(input('Digite um número qualquer: '))
    if num % 2 == 0:
        cont += 1
        soma += num 
print('Você informou {} números pares e a soma entre eles é: {}'.format(cont, soma))
    
    

