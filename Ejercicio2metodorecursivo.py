#Recursivo

import random

def determinante_recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    
    det = 0
    for c in range(len(matriz)):
        submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
        cofactor = matriz[0][c] * determinante_recursivo(submatriz)
        det += cofactor if c % 2 == 0 else -cofactor
    return det

# Crear una matriz 3x3 con valores aleatorios
matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

# Imprimir la matriz
print("Matriz 3x3:")
for fila in matriz:
    print(fila)

# Calcular el determinante de manera recursiva
print("Determinante (Recursivo):", determinante_recursivo(matriz))
