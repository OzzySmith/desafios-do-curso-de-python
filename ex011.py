#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
L = float(input('Qual a largura dessa parede? '))
A = float(input('Qual a altura dessa parede? '))
P = L * A
T = 2
print('Essa parede possui {} metros quadrados de área.'.format(P))
print('Para pintar essa parede é necessário {} litros de tinta.'.format (P / T))
