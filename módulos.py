# Para importar módulos utilizamos comandos como "import", e "from - import - "
# nós chamamos uma coletânea de módulos de biblioteca
# exemplo:

import math

num  = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} é {}.'.format(num, math.ceil(raiz)))
#ou
print('A raíz quadrada de {} é {}.'.format(num, raiz))
