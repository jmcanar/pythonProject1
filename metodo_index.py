# Definir la matriz
matriz = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# Letra a buscar
letra_a_buscar = 'e'

# Buscar la letra en la matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
        if matriz[fila][columna] == letra_a_buscar:
            print(f"La letra '{letra_a_buscar}' se encuentra en la posición [{fila}][{columna}] de la matriz.")
            break
    else:
        continue
    break  # Detener el bucle exterior si la letra se encuentra
