#Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e a raíz quadrada.
N = int(input('Digite um número: '))
D = N * 2
T = N * 3
RQ = N ** (1/2)

print('O dobro de {} é {}. \nseu triplo é {}.\ne sua raiz quadrada é {}.'.format(N, D, T, RQ))
