#Crie um programa que leia quanto dinheiro você tem na carteira e mostre quantos dólares ela pode comprar.
R = float(input('Quantos reais você possui atualmente? '))
D = float(input('Digite a cotação atual do dólar: '))
C = R / D
print('Com {:.2f} reais é possível comprar {:.2f} dólares.'.format(R, C))