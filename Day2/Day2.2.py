# Abrir el archivo
file = open('/Users/jordiros27/Desktop/AdventOfCode2020/Day2/datosDay2.txt', 'r')

countTrue = 0

for line in file:

    corte1 = line.find('-')
    corte2 = line.find(' ')
    corte3 = line.find(':')

    pos1 = int(line[0:corte1])
    pos2 = int(line[corte1 + 1:corte2])
    character = line[corte2 + 1:corte3]
    cadena = line[corte3 + 2: len(line)]

    count = 0
    for i in cadena:
        if cadena[pos1 - 1] == character and cadena[pos2 - 1] == character:
            count = 2
        elif cadena[pos1 - 1] == character:
            count = 1
        elif cadena[pos2 - 1] == character:
            count = 1


    if count == 1:
        countTrue = countTrue + 1

print(countTrue)