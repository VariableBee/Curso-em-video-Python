
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar r$:7,00 por cada km acima do limite.

vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('SUA MULTA SERÁ DE R$:{} POR ANDAR A {}Km/h !'.format((vel - 80) * 7, vel))
else:
    print('Tenha um bom dia! Continue dirigindo em segurança!')
    