#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
#por dia e R$0,15 por Km rodado.

DA = float(input('Quantos dias o carro foi alugado? '))
CD = DA * 60
KR = float(input('Quantos quilômetros foram rodados nesse tempo? '))
CK = KR * 0.15
CT = CK + CD
print('O total a ser pago pelo tempo alugado é de : R${:.2f}'.format(CT))
