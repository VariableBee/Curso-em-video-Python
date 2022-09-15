
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso         25 até 30: Sobrepeso
# Entre 18.5 e 25: Peso ideal            30 até 40: Obesidade
#                                        Acima de 40: Obesidade mórbida.

print('Olá, Bem vind@ a nossa clínica! Hoje calcularemos seu índice de massa corpora, também conhecido como IMC.')
print('Preencha a ficha abaixo com suas informações:')
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print('Certo, calculando IMC. . .')
print('O seu IMC é {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está no peso ideal! Meus parabéns!')
elif imc <= 30:
    print('Parece que você está um pouco acima do peso.')
elif imc <= 40:
    print('Essa não, você está com obesidade!')
else:
    print('Você está com obesidade mórbida! Isso está te fazendo muito mal!!!')