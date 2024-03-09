# Desarrollo de Función para Calcular Temperaturas Promedio en Python
#DEFINIMOS LA FUNCION
def calcular_temperatura_promedio(datos):
    temperaturas_ciudades = {}
#REAlizAMOS UN RECORRIDO EN LA MATRIZ  EN NUETRO ARREGLO CON BUCLE FOR
    for ciudad, semanas in datos.items():
        suma_temperaturas = 0
        total_semanas = len(semanas)

        for semana in semanas:
            suma_temperaturas += semana

        temperatura_promedio = suma_temperaturas / total_semanas
        temperaturas_ciudades[ciudad] = temperatura_promedio

    return temperaturas_ciudades


# DATOS DE TEMPERATURAS DE DIFERENTES CUIDADES
datos = {
    "Quito": [22, 23, 21, 20],
    "Guayaquil": [28, 30, 29, 27],
    "Cuenca": [20, 18, 19, 21]
}
#LLAMADA A LA FUNCION
temperaturas_promedio = calcular_temperatura_promedio(datos)
#IMPRIMIMOS EL RESULTADO
for ciudad, temperatura in temperaturas_promedio.items():
    print(f"La temperatura promedio en {ciudad} es de {temperatura} grados Celsius.")


#NOMBRE: MARCELO CAÑAR