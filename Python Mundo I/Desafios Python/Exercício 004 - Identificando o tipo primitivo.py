
# Crie um algoritmo que leia e mostre os tipos primitivos de um valor, se ele possui números, letras, espaços, etc.

a = input('Digite algo:') 
print('O tipo primitivo desse valor é' , type(a)) # Type identifica o tipo primitivo de um valor.
print('Tem espaços?', a.isspace())  # Existe uma variedade de "Is" para identificar as características de um valor.
print('É um número', a.isnumeric())
print('É alfabetico', a.isalpha())


