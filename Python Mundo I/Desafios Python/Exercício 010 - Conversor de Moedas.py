
# Crie um programa que leia quanto dinheiro uma pessao tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$:1,00 = R$:3,27

nome = str(input('Obrigado por entrar em contato com a Gingercâmbio, por favor digite seu nome:'))
print('Olá {} , poderia nos dizer qual é o saldo em sua carteira?'.format(nome))
real = float(input('Saldo:'))
dolar = real / 3.27
print('Okay! Olhando aqui em nosso sistema com R${:.2f} você poderia comprar até US${:.2f} Dólares!'.format(real, dolar))
print('Estamos felizes que escolheu a Gingercâmbio para realizar o seu sonho de viajar para o exterior! Aproveite')
