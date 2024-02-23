import numpy as np
#Variables unidimensionales con valores enteros:
enteros = [1, 2, 3, 4, 5, 6]
print(enteros)

#Variables unidimensionales con valores flotantes:
flotantes = [1.0, 2.5, 3.7, 4.2, 5.9, 6.3]
print(flotantes)

#Variables unidimensionales con valores de texto:
texto = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
print(texto)

#Variables unidimensionales con valores de enteros, flotantes y texto
mixtos = [1, 2.5, "tres", 4, 5.7, "seis"]
print(mixtos)

print(">>>>Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores enteros (6 variables en total)<<<<")
enteros_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
enteros_5x5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
enteros_3x6 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
print(enteros_2x3)
print(enteros_5x5)
print(enteros_3x6)

print(">>>>Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores flotantes (6 variables en total)<<<<")
float_2x3 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
float_5x5 = np.array([[1.1, 2.2, 3.3, 4.4, 5.5], [6.6, 7.7, 8.8, 9.9, 10.10], [11.11, 12.12, 13.13, 14.14, 15.15], [16.16, 17.17, 18.18, 19.19, 20.20], [21.21, 22.22, 23.23, 24.24, 25.25]])
float_3x6 = np.array([[1.1, 2.2, 3.3, 4.4, 5.5, 6.6], [7.7, 8.8, 9.9, 10.10, 11.11, 12.12], [13.13, 14.14, 15.15, 16.16, 17.17, 18.18]])
print(float_2x3)
print(float_5x5)
print(float_3x6)

print(">>>>Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de texto (6 variables en total)<<<<")
texto_2x3 = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
texto_5x5 = np.array([['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']])
texto_3x6 = np.array([['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r']])
print(texto_2x3)
print(texto_5x5)
print(texto_3x6)

print(">>>>Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de enteros, flotantes y texto (6 variables en total)<<<<")
mixtos_2x3 = np.array([[1, 2.2, 'a'],[3, 4.4, 'b']])
mixtos_5x5 = np.array([[1, 2.2, 'a', 'b', 'c'],[3, 4.4, 'd', 'e', 'f'],[5, 6.6, 'g', 'h', 'i'],[7, 8.8, 'j', 'k', 'l'],[9, 10.1, 'm', 'n', 'o']])
mixtos_3x6 = np.array([[1, 2.2, 'a', 'b', 'c', 'd'],[3, 4.4, 'e', 'f', 'g', 'h'],[5, 6.6, 'i', 'j', 'k', 'l']])
print(mixtos_2x3)
print(mixtos_5x5)
print(mixtos_3x6)

print('>>>>Declare 2 variables tridimensionales 2x3x2, 5x5x5, 3x6x2 y asigne valores enteros<<<<')
# Variable tridimensional 2x3x2 con valores enteros
enteros_2x3x2 = np.array([[[1, 2],
                           [3, 4],
                           [5, 6]],

                          [[7, 8],
                           [9, 10],
                           [11, 12]]])
print(enteros_2x3x2)
# Variable tridimensional 5x5x5 con valores enteros
enteros_5x5x5 = np.array([[[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20],
                           [21, 22, 23, 24, 25]],

                          [[26, 27, 28, 29, 30],
                           [31, 32, 33, 34, 35],
                           [36, 37, 38, 39, 40],
                           [41, 42, 43, 44, 45],
                           [46, 47, 48, 49, 50]],

                          [[51, 52, 53, 54, 55],
                           [56, 57, 58, 59, 60],
                           [61, 62, 63, 64, 65],
                           [66, 67, 68, 69, 70],
                           [71, 72, 73, 74, 75]],

                          [[76, 77, 78, 79, 80],
                           [81, 82, 83, 84, 85],
                           [86, 87, 88, 89, 90],
                           [91, 92, 93, 94, 95],
                           [96, 97, 98, 99, 100]],

                          [[101, 102, 103, 104, 105],
                           [106, 107, 108, 109, 110],
                           [111, 112, 113, 114, 115],
                           [116, 117, 118, 119, 120],
                           [121, 122, 123, 124, 125]]])
print(enteros_5x5x5)
# Variable tridimensional 3x6x2 con valores enteros
enteros_3x6x2 = np.array([[[1, 2],
                           [3, 4],
                           [5, 6],
                           [7, 8],
                           [9, 10],
                           [11, 12]],

                          [[13, 14],
                           [15, 16],
                           [17, 18],
                           [19, 20],
                           [21, 22],
                           [23, 24]],

                          [[25, 26],
                           [27, 28],
                           [29, 30],
                           [31, 32],
                           [33, 34],
                           [35, 36]]])
print(enteros_3x6x2)

print("Declare 2 variables tridimensionales 2x3x1, 5x5x2, 3x6x5 y asigne valores flotantes (6 variables en total)")
# Variable tridimensional 2x3x1 con valores flotantes
flotantes_2x3x1 = np.array([[[1.1],
                             [2.2],
                             [3.3]],

                            [[4.4],
                             [5.5],
                             [6.6]]])
print(flotantes_2x3x1)
# Variable tridimensional 5x5x2 con valores flotantes
flotantes_5x5x2 = np.array([[[1.1, 2.2],
                             [3.3, 4.4],
                             [5.5, 6.6],
                             [7.7, 8.8],
                             [9.9, 10.1]],

                            [[11.11, 12.12],
                             [13.13, 14.14],
                             [15.15, 16.16],
                             [17.17, 18.18],
                             [19.19, 20.20]],

                            [[21.21, 22.22],
                             [23.23, 24.24],
                             [25.25, 26.26],
                             [27.27, 28.28],
                             [29.29, 30.30]],

                            [[31.31, 32.32],
                             [33.33, 34.34],
                             [35.35, 36.36],
                             [37.37, 38.38],
                             [39.39, 40.40]],

                            [[41.41, 42.42],
                             [43.43, 44.44],
                             [45.45, 46.46],
                             [47.47, 48.48],
                             [49.49, 50.50]]])
print(flotantes_5x5x2)
# Variable tridimensional 3x6x5 con valores flotantes
flotantes_3x6x5 = np.array([[[1.1, 2.2, 3.3, 4.4, 5.5],
                             [6.6, 7.7, 8.8, 9.9, 10.1],
                             [11.11, 12.12, 13.13, 14.14, 15.15],
                             [16.16, 17.17, 18.18, 19.19, 20.20],
                             [21.21, 22.22, 23.23, 24.24, 25.25],
                             [26.26, 27.27, 28.28, 29.29, 30.30]],

                            [[31.31, 32.32, 33.33, 34.34, 35.35],
                             [36.36, 37.37, 38.38, 39.39, 40.40],
                             [41.41, 42.42, 43.43, 44.44, 45.45],
                             [46.46, 47.47, 48.48, 49.49, 50.50],
                             [51.51, 52.52, 53.53, 54.54, 55.55],
                             [56.56, 57.57, 58.58, 59.59, 60.60]],

                            [[61.61, 62.62, 63.63, 64.64, 65.65],
                             [66.66, 67.67, 68.68, 69.69, 70.70],
                             [71.71, 72.72, 73.73, 74.74, 75.75],
                             [76.76, 77.77, 78.78, 79.79, 80.80],
                             [81.81, 82.82, 83.83, 84.84, 85.85],
                             [86.86, 87.87, 88.88, 89.89, 90.90]]])
print(flotantes_3x6x5)

print('>>>Declare 2 variables tridimensionales 2x3x3, 5x5x4, 3x6x1 y asignar valores de texto (6 variables en total)<<<')
# Variable tridimensional 2x3x3 con valores de texto
texto_2x3x3 = np.array([[['a', 'b', 'c'],
                         ['d', 'e', 'f'],
                         ['g', 'h', 'i']],

                        [['j', 'k', 'l'],
                         ['m', 'n', 'o'],
                         ['p', 'q', 'r']]])
# Variable tridimensional 5x5x4 con valores de texto
texto_5x5x4 = np.array([[['a', 'b', 'c', 'd'],
                         ['e', 'f', 'g', 'h'],
                         ['i', 'j', 'k', 'l'],
                         ['m', 'n', 'o', 'p'],
                         ['q', 'r', 's', 't']],

                        [['u', 'v', 'w', 'x'],
                         ['y', 'z', 'A', 'B'],
                         ['C', 'D', 'E', 'F'],
                         ['G', 'H', 'I', 'J'],
                         ['K', 'L', 'M', 'N']],

                        [['O', 'P', 'Q', 'R'],
                         ['S', 'T', 'U', 'V'],
                         ['W', 'X', 'Y', 'Z'],
                         ['1', '2', '3', '4'],
                         ['5', '6', '7', '8']],

                        [['9', '0', '!', '?'],
                         ['@', '#', '$', '%'],
                         ['^', '&', '*', '('],
                         [')', '-', '_', '='],
                         ['+', '<', '>', '.']],

                        [['/', ';', ':', '"'],
                         ["'", '[', ']', '{'],
                         ['}', '|', 'mm', '`'],
                         ['~', ' ', 'ñ', 'á'],
                         ['é', 'í', 'ó', 'ú']]])
# Variable tridimensional 3x6x1 con valores de texto
texto_3x6x1 = np.array([[['Hola'],
                         ['compañeros'],
                         ['yo'],
                         ['soy'],
                         ['Marcelo'],
                         ['Canar']],

                        [['cómo'],
                         ['asignar'],
                         ['valores'],
                         ['de'],
                         ['texto'],
                         ['en']],

                        [['Python'],
                         ['usando'],
                         ['variables'],
                         ['tridimensionales'],
                         ['de'],
                         ['NumPy']]])
print(texto_2x3x3)
print(texto_5x5x4)
print(texto_3x6x1)

print('Declare 2 variables tridimensionales 2x3x2, 5x5x1, 3x6x2 y asignar valores de enteros, flotantes y texto (6 variables en total)')
# Variable tridimensional 2x3x2 con valores de enteros, flotantes y texto
mixto_2x3x2 = np.array([[[1, 2.5, 'a'],
                         [3, 4.7, 'b'],
                         [5, 6.3, 'c']],

                        [[7, 8.2, 'd'],
                         [9, 10.6, 'e'],
                         [11, 12.9, 'f']]])

# Variable tridimensional 5x5x1 con valores de enteros, flotantes y texto
mixto_5x5x1 = np.array([[[1, 2.5, 'g'],
                         [3, 4.7, 'h'],
                         [5, 6.3, 'i'],
                         [7, 8.2, 'j'],
                         [9, 10.6, 'k']],

                        [[11, 12.9, 'l'],
                         [13, 14.3, 'm'],
                         [15, 16.7, 'n'],
                         [17, 18.1, 'o'],
                         [19, 20.4, 'p']],

                        [[21, 22.8, 'q'],
                         [23, 24.2, 'r'],
                         [25, 26.6, 's'],
                         [27, 28.9, 't'],
                         [29, 30.3, 'u']],

                        [[31, 32.7, 'v'],
                         [33, 34.1, 'w'],
                         [35, 36.5, 'x'],
                         [37, 38.8, 'y'],
                         [39, 40.2, 'z']],

                        [[41, 42.6, 'A'],
                         [43, 44.9, 'B'],
                         [45, 46.3, 'C'],
                         [47, 48.7, 'D'],
                         [49, 50.1, 'E']]])

# Variable tridimensional 3x6x2 con valores de enteros, flotantes y texto
mixto_3x6x2 = np.array([[[51, 52.5, 'F'],
                         [53, 54.7, 'G'],
                         [55, 56.3, 'H'],
                         [57, 58.2, 'I'],
                         [59, 60.6, 'J'],
                         [61, 62.9, 'K']],

                        [[63, 64.3, 'L'],
                         [65, 66.7, 'M'],
                         [67, 68.1, 'N'],
                         [69, 70.4, 'O'],
                         [71, 72.8, 'P'],
                         [73, 74.2, 'Q']],

                        [[75, 76.6, 'R'],
                         [77, 78.9, 'S'],
                         [79, 80.3, 'T'],
                         [81, 82.7, 'U'],
                         [83, 84.1, 'V'],
                         [85, 86.5, 'W']]])
print(mixto_2x3x2)
print(mixto_5x5x1)
print(mixto_3x6x2)
