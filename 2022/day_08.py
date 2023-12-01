from utils import *
from pprint import pprint

treeGrid = []
for line in splitFile("day_08_input.txt", "\n"):
    treeCol = []
    for tree in line:
        treeCol.append(tree)
    treeGrid.append(treeCol)

def isTreeVisible(tree, col, row):
    isVisibleTop = True
    isVisibleBottom = True
    for tmpCol in range(0, len(treeGrid)):
        treeToCheck = int(treeGrid[tmpCol][row])
        if tmpCol < col and treeToCheck >= tree:
            isVisibleTop = False
        elif tmpCol > col and treeToCheck >= tree:
            isVisibleBottom = False
    
    isVisibleLeft = True
    isVisibleRight = True
    for tmpRow in range(0, len(treeGrid[0])):
        treeToCheck = int(treeGrid[col][tmpRow])
        if tmpRow < row and treeToCheck >= tree:
            isVisibleLeft = False
        elif tmpRow > row and treeToCheck >= tree:
            isVisibleRight = False
    return isVisibleTop or isVisibleRight or isVisibleBottom or isVisibleLeft

def getTreeScore(tree, col, row):
    scoreTop = 0
    for tmpCol in range(max(0, col - 1), -1, -1):
        if tmpCol == col: continue
        scoreTop += 1
        if (int(treeGrid[tmpCol][row]) >= tree):
            break

    scoreBottom = 0
    for tmpCol in range(min(col+1, len(treeGrid)), len(treeGrid)):
        if tmpCol == col: continue
        scoreBottom += 1
        if (int(treeGrid[tmpCol][row]) >= tree):
            break

    scoreLeft = 0
    for tmpRow in range(max(0, row - 1), -1, -1):
        if tmpRow == row: continue
        scoreLeft += 1
        if (int(treeGrid[col][tmpRow]) >= tree):
            break

    scoreRight = 0
    for tmpRow in range(min(row + 1, len(treeGrid[0])), len(treeGrid[0])):
        if tmpRow == row: continue
        scoreRight += 1
        if (int(treeGrid[col][tmpRow]) >= tree):
            break

    return scoreTop * scoreBottom * scoreLeft * scoreRight

visibleTrees = 0
largestTreeScore = 0
for colIndex in range(0, len(treeGrid)):
    for rowIndex in range(0, len(treeGrid[0])):
        tree = int(treeGrid[colIndex][rowIndex])
        if isTreeVisible(tree, colIndex, rowIndex):
            visibleTrees += 1

        currentTreeScore = getTreeScore(tree, colIndex, rowIndex)
        if (currentTreeScore > largestTreeScore):
            largestTreeScore = currentTreeScore

print("Visible trees:", visibleTrees)
print("Largest tree score:", largestTreeScore)
