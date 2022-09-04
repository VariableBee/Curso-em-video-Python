
# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa r$:60,00 por dia e r$:0,15 por km rodado.

km = float(input('Quantos Km rodados?'))
dias = int(input('Quantos dias você alugados?'))
preço = (dias * 60) + (km * 0.15)
print('Ototal a ser pago por {} dias que alugou o veículo somado a {} kilometros que andou nele é R%:.'.format(dias, km, dias))
