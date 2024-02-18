#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida seu primeiro e último nome separadamente.
#Exemplo: Ana maria de souza
#primeiro: Ana
#último: souza
nome = str(input('Digite seu nome completo: '))
nome = nome.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[-1]))
