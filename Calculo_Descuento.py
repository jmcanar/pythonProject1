def calcular_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final
# valores
precio_inicial = 1000 #valor de la compra
descuento_porcentaje = 10 #porcentaje de descuento
descuento_porcentaje2 = 10#porcentaje de descuento2
#llamada de la funcion
precio_con_descuento = calcular_descuento(precio_inicial, descuento_porcentaje)
print(f"El precio original es: ${precio_inicial}")
print(f"El descuento aplicado es del {descuento_porcentaje}%")
print(f"El precio final con descuento uno es: ${precio_con_descuento}")
#llamamos nuevamente a la funcion
precio_con_descuento2 = calcular_descuento(precio_con_descuento,descuento_porcentaje2)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print("tiene una promocion de descuento del 10% del valor final")
print(f"El precio final con descuento dos  es: ${precio_con_descuento2}")


#Marcelo Canar