
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# calculando porcentagem: 10*5/100 ou 10 * 0.05

print(' '*20)
print('O QUE!? você não está sabendo da nossa PROMOÇÃO de 5% de DESCONTO?')
preço = float(input('QUALQUER produto que levar hoje terá um DESCONTO! Confira, insira o preço de QUALQUER: R$'))
novo = preço - (preço * 5 / 100)
print('Então o novo preço desse produto é R${:.2f}, você economizou R${:.2f}'.format(novo, preço - novo))
