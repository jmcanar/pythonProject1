# Creación del archivo my_notes.txt y escritura de notas personales
with open("my_notes.txt", "w") as archivo:
    archivo.write("mi nombre es\n")
    archivo.write("marcelo cañar\n")
    archivo.write("cual es su nombre\n")

# Lectura del archivo my_notes.txt y mostrar su contenido línea por línea

with open("my_notes.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())  # Strip para eliminar cualquier espacio en blanco o caracteres de nueva línea
# Cierre de archivos
archivo.close()
