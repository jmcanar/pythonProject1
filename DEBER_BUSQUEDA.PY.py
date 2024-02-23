import numpy as np
arreglo_3x3 =np.array([

        [4,7,2],
        [1,9,6],
        [8,3,5]
])
print(arreglo_3x3)
valor_buscado = int(input('ingrese el valor. '))
fila_encontrada = -1
columna_encontrada = -1

for fila in range(len(arreglo_3x3)):
    for columna in range(len(arreglo_3x3[fila])):
        if arreglo_3x3[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -1:
        break
if fila_encontrada != -1:
    print(f"se encontro {valor_buscado} en fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"{valor_buscado} no se encontro la matriz.")
