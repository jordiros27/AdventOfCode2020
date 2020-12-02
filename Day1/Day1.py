
# Abrir el archivo
file = open('/Users/jordiros27/Desktop/AdventOfCode2020/Day1/datosDay1.txt', 'r')

datos = []

# Añadir los datos en lista
for line in file:
    datos.append(int(line.strip()))

for i in range(len(datos)):
    for j in range(len(datos)):
        if datos[i] + datos[j] == 2020:
            print(datos[i] * datos[j])

for i in range(len(datos)):
    for j in range(len(datos)):
        for k in range(len(datos)):
            if datos[i] + datos[j] + datos[k] == 2020:
                print(datos[i] * datos[j] * datos[k])