from utils import *
from pprint import pprint

visitedTailPositions = {0: [0]}

numberOfSegments = 10
segmentPositions = []
for i in range(0, numberOfSegments):
    segmentPositions.append([0, 0])

def printExampleGrid():
    for row in rangeInclusive(4, 0, -1):
        rowStr = ''
        for col in rangeInclusive(0, 5):
            charFound = False
            for i in range(0, len(segmentPositions)):
                if row == segmentPositions[i][0] and col == segmentPositions[i][1]:
                    if i == 0: rowStr += 'H'
                    else: rowStr += str(i)
                    charFound = True
                    break
            if charFound: continue
            elif row == 0 and col == 0: rowStr += 's'
            else: rowStr += '.'
        print(rowStr)
    print("")

def moveSegment(parentSegment, childSegment): 
    xDiff = parentSegment[0] - childSegment[0]
    yDiff = parentSegment[1] - childSegment[1]

    if abs(xDiff) + abs(yDiff) >= 3: # Diagonal move
        if xDiff > 0: childSegment[0] += 1
        else: childSegment[0] -= 1

        if yDiff > 0: childSegment[1] += 1
        else: childSegment[-1] -= 1
    elif abs(xDiff) == 2: #Horizontal move
        if xDiff > 0: childSegment[0] += 1
        else: childSegment[0] -= 1
    elif abs(yDiff) == 2: #Vertical move
        if yDiff > 0: childSegment[1] += 1
        else: childSegment[1] -= 1

#printExampleGrid()

for line in splitFile("day_09_input.txt", "\n"):
    move = splitString(line, " ")
    direction = move[0]
    steps = int(move[1])

    for i in range(0, steps):
        if   direction == 'U': segmentPositions[0][0] += 1
        elif direction == 'D': segmentPositions[0][0] -= 1
        elif direction == 'L': segmentPositions[0][1] -= 1
        elif direction == 'R': segmentPositions[0][1] += 1

        for childIndex in range(0, numberOfSegments-1):
            moveSegment(segmentPositions[childIndex], segmentPositions[childIndex+1])

        tailXPos = segmentPositions[numberOfSegments-1][0]
        tailYPos = segmentPositions[numberOfSegments-1][1]
        if tailXPos not in visitedTailPositions:
            visitedTailPositions[tailXPos] = []

        if tailYPos not in visitedTailPositions[tailXPos]:
            visitedTailPositions[tailXPos].append(tailYPos)

        #printExampleGrid()

numberOfPositions = 0
for row in visitedTailPositions:
        numberOfPositions += len(visitedTailPositions[row])
print("Number of visited positions", numberOfPositions)