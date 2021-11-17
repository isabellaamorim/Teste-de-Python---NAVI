from math import *

vetorx = [0] * 10
for i in range(0, 10): 
    if i % 2 == 0: 
        vetorx[i] = 3 ** i + 7 * factorial(i)
    else: 
        vetorx[i] = 2 ** i + 4 * log(i)

media = sum(vetorx)/10
max_position = vetorx.index(max(vetorx))

print('A média dos elementos desse vetor é: {:.2f}'. format(media))
print('A posição do maior elemento desse vetor é: {}'. format(max_position))