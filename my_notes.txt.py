# Creación del archivo my_notes.txt y escritura de notas personales
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: hola mi nombre es.\n")
    file.write("Nota 2: marcelo cañar.\n")
    file.write("Nota 3: cual es su nombre.\n")

# Lectura del archivo my_notes.txt y mostrar su contenido línea por línea
with open('my_notes.txt', 'r') as file:
    print("Contenido del archivo my_notes.txt:")
    for line in file.readlines():
        print(line.strip())  # Strip para eliminar cualquier espacio en blanco o caracteres de nueva línea
