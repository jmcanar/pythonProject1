def calcular_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final
# valores
precio_inicial = 100 #valor de la compra
descuento_porcentaje = 10 #porcentaje de descuento
#llamada de la funcion
precio_con_descuento = calcular_descuento(precio_inicial, descuento_porcentaje)
print(f"El precio original es: ${precio_inicial}")
print(f"El descuento aplicado es del {descuento_porcentaje}%")
print(f"El precio final con descuento es: ${precio_con_descuento}")