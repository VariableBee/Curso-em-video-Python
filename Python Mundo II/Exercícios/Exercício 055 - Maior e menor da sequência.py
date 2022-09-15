
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
from math import inf

menor = inf #Infitino inicialmente
maior = 0 
for c in range(1, 6):
    peso = float(input('Qual é o peso da {}º pessoa? '.format(c)))
    if peso > maior:
        maior = peso # Isso somente no primeiro Loop
    if peso < menor: # Nota¹
        menor = peso # Isso somento no primeiro Loop
   
   # Nota¹: Aqui não vai ELIF pois o ElIF só aconteceria se o peso não fosse maior, ele sempre vai ser, assim como sempre será menor que inf
   # AGORA IMAGINE O LOOP DO ZERO COM NOVOS VALORES NAS VARIÁVEIS DE CONTROLE.
   
print('O maior peso entre todos os voluntários foi {}'.format(maior))
print('E o menor peso dentre os voluntários foi {}'.format(menor))