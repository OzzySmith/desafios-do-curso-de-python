#Faça um programa que leia um ângulo qualquer
#e mostre na tela o valor do seu seno, coseno e a tangente desse ângulo.
import math
ang = int(input('Digite o ângulo que você deseja trabalhar: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
if ang == 90 or ang == 270:
    print('Para o ângulo de {}°, nós temos: \n seno: {:.2f} \n cosseno: {:.2f} \n e a tangente é inexistente.'.format(ang, sen, cos))
else:
    print('Para o ângulo de {}°, nós temos: \n seno: {:.2f} \n cosseno: {:.2f} \n e a tangente: {:.2f}'.format(ang, sen, cos, tan))
