#Crie um programa que leia o nome de uma pessoa e diga se ela possui "SILVA" no nome.
nome = str(input('Digite seu nome completo: '))
nome = nome.upper()
if 'SILVA' in nome:
    print('Você possui o sobrenome silva!')
else:
    print('Você não possui o sobrenome silva.')
