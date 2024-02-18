#Escreva um programa que leia uma temperatuca em Celsius , e a converta para Fahrenheit

C = float(input('Digite uma temperatura em Celsius: '))
F = (9 * C / 5) + 32

print('A temperatura de {}°c é equivalente a {}°f.'.format(C, F))
