
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


frase = str(input('Escreva uma frase: ')).replace(" ","").upper() #.strip()
# palavras = frase.split()
# junto = ''.join(palavras)
# ao_contrario = junto[::-1]
ao_contrario = frase[::-1]
# print('O inverso de {} é {}'.format(junto, ao_contrario))
if frase == ao_contrario:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
