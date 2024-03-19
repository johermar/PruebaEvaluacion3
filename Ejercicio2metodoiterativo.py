#Iterativo

import random

def determinante_iterativo(matriz):
    """
    Calcula el determinante de una matriz 3x3 de manera iterativa.
    
    Parámetros:
    matriz -- Lista de listas que representa la matriz 3x3.
    
    Retorna:
    El determinante de la matriz.
    """
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

# Crear una matriz 3x3 con valores aleatorios en el rango de 1 a 10
matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

# Imprimir la matriz generada
print("Matriz 3x3 generada aleatoriamente:")
for fila in matriz:
    print(fila)

# Calcular el determinante de la matriz de manera iterativa
determinante = determinante_iterativo(matriz)
print(f"El determinante de la matriz es: {determinante}")