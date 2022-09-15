
for c in range(0, 6): # Laço de repetições
    print('Oi') # Isso será repetido (0, 6) 6x OiOiOiOiOiOi
print('FIM') # Fora do laço

for c in range(1, 6): # O Range sempre ignora o último número, sendo assim, coloque um a mais ou a menos.
    print(c) # Mostrando na tela o próprio laço de 1 à 5.
print('FIM')

for c in range(5, 0, -1): # Esse "-1" é uma iteração do que acontece no final do laço, 5 - 1, 4 - 1, 3 - 1 . . . para repetir de trás para frente! 5, 4, 3, 2, 1. (O último número era 0, ignorado.)
    print(c)
print ('FIM')

for c in range(0, 11, 2): # Esse "2" é uma iteração para repetir de 2 em 2. 0,2,4,6,8,10.
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1): # N+1 vai garantir a repetição até o valor digitado pelo usuário.
    print(c)
print('FIM')

i = int(input('Início: ')) # Por onde vai começar o laço. Ex: 0
p = int(input('Passo: ')) # De que forma ele vai ser repetido. Ex: 2
f = int(input('Fim: ')) # Onde o laço vai terminar. Ex: 11
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: ')) # Ele vai repetir o input "Digite um valor" 3x.
    s += n # s = s + n (Vamos somar todos os valores repetidos.)
print('A soma de todos os valores foi: {}'.format(s))