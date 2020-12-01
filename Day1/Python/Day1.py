
# Abrir el archivo
file = open('/Users/jordiros27/Desktop/AdventOfCode2020/Python/datos.txt', 'r')

datos = []

# Añadir los datos en lista
for line in file:
    datos.append(int(line.strip()))

for i in datos:
    for j in datos:
        for k in datos:
            if i + j + k == 2020:
                print(i * j * k)
