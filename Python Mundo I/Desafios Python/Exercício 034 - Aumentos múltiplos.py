
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguale, o aumento é de 15%

print('Olá tudo bem! Você está prestes a receber um aumento!')
salário = float(input('Para isso, por favor nos diga, qual é o seu salário? R$:'))
aumento = salário
if salário >= 1250:
    aumento = salário * 0.10
else:
    aumento = salário * 0.15

print('Meus parabéns! você teve um aumento de {:.2f}, seu novo salário é de R${:.2f}'.format(aumento, salário + aumento))
