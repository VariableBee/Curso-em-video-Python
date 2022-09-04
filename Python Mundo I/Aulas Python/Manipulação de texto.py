
# MANIPULAÇÃO DE TEXTO

frase = 'Curso em vídeo python'

# FATIAMENTO
print(frase[9])
print(frase[13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# ANÁLISE
len(frase)
frase.count('o', 0, 13)
frase.find('deo')
'curso' in frase  # Frase precisa ser uma lista para essa análise funcionar.

# TRANSFORMAÇÃO
# Algumas funções de Manipulação de texto.
frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase.strip()  # Coloque Lstrio ou Rstrip para remover espaços a esquerda ou direita.

# DIVISÃO
frase.split()
# JUNÇÃO
'-'.join(frase)
