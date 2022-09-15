
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('Olá Scottie, hoje nós vamos criar uma PA.')
t1 = int(input('Por favor, me diga o primeiro termo para nossa PA ter início: '))
r = int(input('Digite uma razão para fazermos nossa PA: '))
n = 10 # ENÉSIMO TERMO QUE QUERO ENCONTRAR
tn = t1 + (n-1) * r # FÓRMULA PARA ENCONTRAR UM TERMO DE UMA PA
print('Aqui estão os 10 primeiros termos dessa PA:')
for c in range(t1, tn+1, r):
    print(c)
print('O décimo termo da PA de {} com a razão {} é {}'.format(t1, r, tn))
    
