#faça um programa que leia o comprimento do cateto oposto e do 
#cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
N1 = int(input('Dê a medida do cateto oposto: '))
N2 = int(input('Dê a medida do cateto adjacente: '))
hipo = math.hypot(N1, N2)
print('O comprimento da hipotenusa é {}'.format(hipo))
