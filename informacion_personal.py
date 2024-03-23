# Creamos el diccionario
informacion_personal = {
    "nombre": "Marcelo",
    "edad": 33,
    "ciudad": "CUENCA",
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = ("LOJA")

# Agregar una nueva clave-valor representando la profesión
informacion_personal["profesion"] = "ELECTRICISTA"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0990178513"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
