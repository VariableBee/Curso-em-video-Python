

# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM Km.
# CALCULE O PREÇO DA PASSAGEM COBRANDO R$: 0,50 por Km para viagens de até 200KM E R|$0,45 PARA VIAGENS LONGAS.

distância = int(input('Qual é a distância dessa viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50

else:
    preço = distância * 0.45

print('E o preço de sua passagem será de R${:.2f}. Boa viagem!'.format(preço))
