# Matriz desordenada
matriz_desordenada = [
    [4, 2, 5],
    [6, 5, 1],
    [6, 3, 8]
]
#matriz ordenanda
matriz_ordenada = (sorted(fila) for fila in matriz_desordenada)
print("\nMatriz Ordenada:")
for fila in matriz_ordenada:
    print(fila)
#fin