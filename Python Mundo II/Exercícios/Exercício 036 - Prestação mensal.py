
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Qual é o valor da casa? R$:'))
anos = int(input('Em quantos anos gostaria de financiar a casa? '))
salário = float(input('Qual é seu salário? R$:'))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print('Certo, estou calculando . . . O salário mínimo que você precisa para aceitarmos a compra é de R${:.2f}!'.format(mínimo))

if prestação <= mínimo:
    print('Meus parabéns, o valor da prestação mensal será de R$:{:.2f} para a compra de uma casa com o valor de R${:.2f} em {} anos!'.format(prestação, casa, anos))
else:
    print('Sinto muito, o empréstimo foi negado!')