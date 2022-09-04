
# CONDIÇÕES

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:   # Caso tempo seja menor ou igual a 3.
    print('Carro novo')
else:            # Caso contrário...
    print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'carro velho')  # Podemos simplificar uma condição em Python com uma linha só!
print('--FIM--')

# NOME LINDO VS NOME MEH
nome = str(input('Qual é seu nome? '))
if nome == 'Christian':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia,{}'.format(nome))

# MÉDIA DE UM ALUNO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
