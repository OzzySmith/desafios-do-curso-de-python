#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
N = int(input('Digite um número: '))
ANT = N - 1
SCS = N + 1
print('O antecessor e o sucessor de {} são, respectivamente: {} e {}.'.format(N, ANT, SCS))

#exemplo simplificado

print('O antecessor e o sucessor de {} são, respectivamente: {} e {}.'.format(N, (N-1), (N+1)))
