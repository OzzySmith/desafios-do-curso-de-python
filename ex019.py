#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = str(input('Escreva o nome do primeiro aluno: '))
a2 = str(input('Escreva o nome do segundo aluno: '))
a3 = str(input('Escreva o nome do terceiro aluno: '))
a4 = str(input('Escreva o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]
sorteio = random.choice(alunos)
print('Dos seguintes alunos mencionados: {}, {}, {} e {}, o sorteado foi {}, parabéns!'.format(a1, a2, a3, a4, sorteio))
