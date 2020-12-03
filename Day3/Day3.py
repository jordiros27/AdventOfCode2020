file = open('inputDay3.txt', 'r')

datos = []
arboles = 0
for line in file:
    datos.append(line[:-1])

posX, posY = 0, 0
for i in range(len(datos) - 1):
    posX = (posX + 3) % len(datos[i])
    if datos[i + 1][posX] == "#":
        arboles += 1
print(arboles)
