# Matriz desordenada
matriz_desordenada = [
    [9, 2, 5],
    [4, 7, 1],
    [6, 3, 8]
]

# Imprimir matriz desordenada
print("Matriz Desordenada:")
for fila in matriz_desordenada:
    print(fila)

# Ordenar la matriz utilizando el método sorted()
matriz_ordenada = [sorted(fila) for fila in matriz_desordenada]

# Imprimir matriz ordenada
print("\nMatriz Ordenada:")
for fila in matriz_ordenada:
    print(fila)