def calcular_temperatura_promedio(datos):
    temperaturas_ciudades = {}

    for ciudad, semanas in datos.items():
        suma_temperaturas = 0
        total_semanas = len(semanas)

        for semana in semanas:
            suma_temperaturas += semana

        temperatura_promedio = suma_temperaturas / total_semanas
        temperaturas_ciudades[ciudad] = temperatura_promedio

    return temperaturas_ciudades


# Ejemplo de uso
datos = {
    "Quito": [22, 23, 21, 20],
    "Guayaquil": [28, 30, 29, 27],
    "Cuenca": [20, 18, 19, 21]
}

temperaturas_promedio = calcular_temperatura_promedio(datos)

for ciudad, temperatura in temperaturas_promedio.items():
    print(f"La temperatura promedio en {ciudad} es de {temperatura} grados Celsius.")