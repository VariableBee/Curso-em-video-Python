
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado.
# Média entre 5.0 e 6.9: Recuperação.
# Média 7.0 ou superior: Aprovado.

n1 = float(input('Sua N1 foi:'))
n2 = float(input('Sua N2 foi:'))
média = n1 + n2 / 2

if média <= 5.0:
    print('Infelizmente você foi reprovado! Sua média foi de {}'.format(média))
elif média >= 5 or média <= 6.9 :
    print('Você está de recuperação! Sua média foi de {}'.format(média))
else:
    print('Meus parabéns, você foi APROVADO! Sua média foi de {}'.format(média))