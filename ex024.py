#Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.split()
if 'Santo' in cidade[0]:
    print('O nome da cidade começa com "Santo".')
else:
    print('O nome da cidade não começa com "Santo".')
