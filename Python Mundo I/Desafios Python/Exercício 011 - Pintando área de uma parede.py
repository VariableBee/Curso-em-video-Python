
# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Considere que cada litro de tinta pinta uma área de 2m².

largura = float(input('Qual é a largura da parede?'))
altura = float(input('Qual é a altura da parede?'))
área = largura * altura 
print('Considerando que cada litro de tinta pinta uma área de 2m²')
print('seria necessário {} litros de tinta para pintar uma parede com uma área de {} metros.'.format(área/2, área))
