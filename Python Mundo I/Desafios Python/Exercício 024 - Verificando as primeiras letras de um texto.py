
# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

cidade = str(input('Digite o nome de uma cidade:')).strip()
print(cidade.upper().split()[0].find('SANTO'))  # Dessa forma mesmo cidades como Santorine retornariam FALSE.



