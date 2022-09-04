
# FUNDAMENTOS DA LINGUAGEM

# PADRÃO ANSI 033[Style/Text/Back m
# \033[0:33:44m
# Códigos para estilo:
# STYLE            TEXT        BACK
# 0 = none          30          40
# 1 = Bold          31          41
# 4 = Underline     32          42
# 7 = Negative      33          43
#                   34          44
#                   35          45
#                   36          46
#                   37          47

print('\033[4;36;40mOlá, Mundo!')
a = 3
b = 5
print('\033[m Os valores são \033[1;31m{}\033[m e \033[1;31m{}\033[m!!! '.format(a, b))

nome = 'Christian'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'],nome, cores['limpa']))


