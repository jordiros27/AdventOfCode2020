file = open('inputDay3.txt', 'r')

datos = []
for line in file:
    datos.append(line[:-1])

movimientos = [(1,1),(3,1),(5,1),(7,1),(1,2)]
resultados = 1

for i in movimientos:
    posX= 0
    arboles = 0
    j = 0
    while j < len(datos) - 1:
        posX = (posX + i[0]) % len(datos[i[1]])
        j = j + i[1]
        if datos[j][posX] == "#":
            arboles += 1
    resultados = resultados * arboles
print(resultados)
