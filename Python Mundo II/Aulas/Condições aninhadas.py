
# Condição simples
nome = str(input('Qual é seu nome?'))
if nome == 'Christian':
    print('Que nome bonito!')

# Condição composta:
nome = str(input('Qual é seu nome?'))
if nome == 'Christian':
    print('Que nome bonito!')
else:
    print('Tenha um bom dia, {}!'.format(nome))

# Estrutura aninhada simplificada
nome = str(input('Qual é seu nome?'))
if nome == 'Christian':
    print('Que nome bonito!')
elif nome == 'Mísia' or nome == 'Amora' or nome == 'Bailey':
    print('Seu nome é muito fofo!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia{}!'.format(nome))
    
# Pode criar quantos 'elifs' quiser dentro de um if.
# Condição composta:

