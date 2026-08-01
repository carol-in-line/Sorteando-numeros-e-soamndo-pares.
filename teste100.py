from random import randint
from time import sleep

lis = []
def sorteia():
    print ('sorteando os 5 valores :', end = '')
    for c in range (0,5):
        n = randint(1,50)
        lis.append(n)
        print(f'{n }, ', end = '', flush = True)
        sleep(0.3)
    print()


def par(lis):
    soma = 0 
    for c in lis:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {lis} temos {soma}')

sorteia()
par(lis)
