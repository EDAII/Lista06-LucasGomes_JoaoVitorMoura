import random
import os

while True: #Validação limite superior
    try:
        sl = int(input('Digite o limite superior do vetor: '))
        if (sl < 1):
            raise ValueError(sl)
    except ValueError as e:
        print("Valor inválido:",e)
    else:
        break

while True: #Validação do tamanho do vetor
    try:
        size = int(
            input(
                'Digite o tamanho do vetor que seja menor do que o limite superior: '
            ))
        if (size > sl):
            raise ValueError(size)
    except ValueError as e:
        print("Valor inválido:",e)
    else:
        break

#Comando para gerar um vetor não ordenado de tamanho size de 0 ate num randomicamente
vector = random.sample(range(sl),size)
# vector = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
# size = 12
print(f'Array: {vector}\n')

#Verifica inversões em A e B

inversionsA = 0
inversionsB = 0
inversionsR = 0
inversionsListA = []
inversionsListB = []
inversionsListR = []

# Group A
print(f'Group A: {vector[:size//2]}')
for i in range(0,size//2):
    for j in range(i+1, size//2):
        if(vector[i]>vector[j]):
            inversionsListA.append((vector[i],vector[j]))
            inversionsA+=1

# Sort group A
for j in range(size//2-1):
    for k in range(j + 1, 0, -1):
        if (vector[k] < vector[k - 1]):
            vector[k], vector[k - 1] = vector[k - 1], vector[k]

print(f'Amount of inversions in A: {inversionsA}')
print(f'Inversions in A: {inversionsListA}\n')

# Group B
print(f'Group B: {vector[size//2:]}')
for i in range(size//2,size):
    for j in range(i + 1, size):
        if (vector[i] > vector[j]):
            inversionsListB.append((vector[i], vector[j]))
            inversionsB += 1

# Sort group B
for j in range(size // 2, size-1):
    for k in range(j + 1, size // 2, -1):
        if (vector[k] < vector[k - 1]):
            vector[k], vector[k - 1] = vector[k - 1], vector[k]

print(f'Amount of inversions in B: {inversionsB}')
print(f'Inversions in B: {inversionsListB}\n')

# Print sorted A and B
print(f'{vector[:size//2]} - {vector[size//2:]}')

# Count inversions AB
i=j=k=0
left = vector[:size//2]
right = vector[size//2:]

while(i < len(left) and j < len(right)):
    for x in range(size//2):
        if (left[x] > right[j] and left[i] > right[j]):
            inversionsListR.append((left[x], right[j]))
            inversionsR += 1
    if(left[i] < right[j]):
        vector[k] = left[i]
        i += 1
    else:
        vector[k] = right[j]
        j += 1
    k += 1
print(f'Amount of inversions in A-B: {inversionsR}')
print(f'Inversions in A-B: {inversionsListR}\n')
print(f'Sorted array: {vector}')
print(f'\nTotal of inversions: {inversionsA+inversionsB+inversionsR}')
