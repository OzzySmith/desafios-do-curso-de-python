#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
num = float(input('Digite um número flutuante: '))
trunc = math.trunc(num)
print('A parte inteira de {} é igual a {}'.format(num, trunc))
