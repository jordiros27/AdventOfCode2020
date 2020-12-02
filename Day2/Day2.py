
# Abrir el archivo
file = open('/Users/jordiros27/Desktop/AdventOfCode2020/Day2/datosDay2.txt', 'r')

countTrue = 0

for line in file:

    corte1 = line.find('-')
    corte2 = line.find(' ')
    corte3 = line.find(':')

    numInicio = int(line[0:corte1])
    numFinal = int(line[corte1 + 1:corte2])
    character = line[corte2 + 1:corte3]
    cadena = line[corte3 + 2: len(line)]

    count = 0
    x = 0
    for i in cadena:
        if character == cadena[x]:
            count = count + 1
        x = x + 1

    if count >= numInicio and count <= numFinal:
        countTrue = countTrue + 1

print(countTrue)