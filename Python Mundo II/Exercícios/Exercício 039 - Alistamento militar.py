
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militasr.
# Se é hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Em que ano você nasceu?'))
atual = date.today().year
idade = atual - nascimento
print('Entendido, então você tem {} anos correto?'.format(idade))
if idade < 18:
    print('Você ainda vai se alistar em {} anos'.format(idade - 18))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou {} anos do prazo de alistamento!'.format(idade - 18))
