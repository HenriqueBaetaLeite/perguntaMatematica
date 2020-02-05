from random import choice
from time import sleep
print('\033[33mOlá, irei fazer uma pergunta aleatória de alguma operação matemática.\nDigite 2 números e irei sortear o operador.\033[m')
print('-' * 20)
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
print('Sorteando o operador...')
sleep(1)
operadores = ['+', '-', 'x']
sorteio = choice(operadores)
print(sorteio)
resultfinal = 0
if sorteio == '+':
    resultfinal = n1 + n2
elif sorteio == '-':
    resultfinal = n1 - n2
elif sorteio == 'x':
    resultfinal = n1 * n2
resultado = float(input('Digite o resultado entre {} {} {} = '.format(n1, sorteio, n2)))
if resultado == resultfinal:
    print('\033[36mParabéns!\033[m Você acertou o resultado!')
else:
    print('\033[31mVocê errou\033[m, estude mais...')
