
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto.                  Em até 2x no cartão: preço normal.
# À vista no cartão: 5% de desconto.                         3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format('LOJAS VARIABLEBEE'))
preço = float(input('Preço do produto R$:'))
pagamento = int(input('''
                     
[ 1 ] À vista no dinheiro ou cheque.
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

Escolha sua forma de pagamento: '''))

if pagamento == 1:
    total = preço - preço * (10/100)
    desconto = preço * (10/100)
    print('Você escolheu pagar à vista no dinheiro/cheque. Você terá um desconto de 10% em sua compra!')
    print('DESCONTO R$:{:.2f}'.format(desconto))
elif pagamento == 2:
    total = preço - preço * (5/100)
    desconto = preço * (5/100)
    print('Você escolheu pagar à vista no cartão. Você terá um desconto de 5% em sua compra!')
    print('DESCONTO R$:{:.2f}'.format(desconto))
elif pagamento == 3:
    total = preço
    valorparc = total / 2
    desconto = 0
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(valorparc))
    print('DESCONTO R$:{:.2f}'.format(desconto))
elif pagamento == 4:
    total = preço + preço * (20/ 100)
    juros = preço * (20/100)
    parcelas = int(input('Em quantas vezes gostaria de parcelar sua compra? ' ))
    valorparc = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, valorparc))
    print('JUROS R$:{:.2f}'.format(juros))
    
print('O valor total da compra foi de R${:.2f}!'.format(total))
