#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: '))
frase = frase.upper()
frase = frase.strip()
prime = frase.find('A')
ultim = frase.rfind('A')
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A frase "{}" possui: '.format(frase))
print('A primeira letra A na posição {}.'.format(prime + 1))
print('A última letra A na posição {}.'.format(ultim + 1))
