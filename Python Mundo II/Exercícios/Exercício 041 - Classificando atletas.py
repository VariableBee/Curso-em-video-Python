
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master

from datetime import date
ano = int(input('Em que ano você nasceu?'))
idade = date.today().year - ano

print('Sua idade é de {} anos correto?'.format(idade))

if idade <= 9:
    print('A sua categoria é: Mirim')
elif idade <= 14:
    print('A sua categoria é: Infantil')
elif idade <=19:
    print('A sua categoria é: Junior')
elif idade <= 20:
    print('A sua categoria é: Sênior')
else:
    print('A sua categoria é: Master')
    
    