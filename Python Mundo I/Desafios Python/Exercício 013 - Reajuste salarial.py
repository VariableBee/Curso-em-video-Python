
# Faça um algoritmo que leia e calcule seu reajuste salarial com 15% de aumento.

print('O que? você não está sabendo da nossa promoção de 5% de desconto?')
p = float(input('Qualquer produto que levar hoje terá um desconto! Insira preço:'))
d = p * (15/100)
print('Então o novo preço desse produto é {}, você economizou {}'.format(p + d, d))
