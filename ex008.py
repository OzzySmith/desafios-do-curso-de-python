#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
D = int(input('Digite uma distância em metros: '))
KM = D / 1000
HM = D / 100
DAM = D / 10
M = D / 1
DM = D * 10
CM = D * 100
MM = D * 1000

print('A medida de {} metros corresponde a:'.format(D))
print('{}km'.format(KM))
print('{}hm'.format(HM))
print('{}dam'.format(DAM))
print('{}m'.format(M))
print('{}dm'.format(DM))
print('{}cm'.format(CM))
print('{}mm'.format(MM))
