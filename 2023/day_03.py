from utils import *
from pprint import pprint

class Gear():
    def __init__(self, coord, gear):
        self.coord = coord
        self.gears = [gear]

lines = []
for line in splitFile("day_03_input.txt", "\n"):
    lines.append("." + line + ".")

gears = { }

def getNumber(row, column):
    global lines
    return line[column:column + findNumberLength(row, column)]

def findNumberLength(row, column):
    global lines
    count = 0
    for c in lines[row][column:]:
        if (c.isdigit()):
            count += 1
        else:
            return count
    return count

def isNumberValid(row, column):
    global lines
    global gears
    isValid = False
    for i in rangeInclusive(column, column + findNumberLength(row, column)):
        for lineIndex in rangeInclusive(max(0, row-1), min(len(lines)-1, row+1)):
            for colIndex in range(max(0, i-1), min(len(lines[row])-1, i+1)):
                c = lines[lineIndex][colIndex]
                if (c != '.' and not c.isdigit()):
                    if (c == '*'):
                        coords = str(lineIndex) + ',' + str(colIndex)
                        if (gears.get(coords)) is None:
                            gears[coords] = []
                        gears.get(coords).append(getNumber(row, column))
                    return True
    return False

sum = 0
for row, line in enumerate(lines):
    for column, c in enumerate(line):
        if column == 0 or not line[column-1].isdigit():
            if (c.isdigit() and isNumberValid(row, column)):
                number = getNumber(row, column)
                if (number != ''):
                    sum += int(number)
print(sum)
gearsum = 0
for gear in gears.values():
    if len(gear) == 2:
        gearsum += int(gear[0]) * int(gear[1])
print(gearsum)