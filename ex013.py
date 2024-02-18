#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
S = float(input('Digite o salário atual de um funcionário: '))
A = S + (S * 15 / 100)
print('O salário desse funcionário, anteriormente de R${:.2f}, será de R${:.2f} após o aumento de 15%.'.format(S, A))
