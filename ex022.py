#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem ao todo(desconsiderando os espaços)
#Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome: '))
maius = nome.upper()
print('Seu nome em maiúsculo é: {}'.format(maius))
minus = nome.lower()
print('Seu nome em minúsculo é: {}'.format(minus))
total = len(nome.replace(' ', ''))
print('Seu nome tem ao todo {} letras.'.format(total))
num = nome.split()
print('Seu primeiro nome possui {} letras.'.format(len(num[0])))
