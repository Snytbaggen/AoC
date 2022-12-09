from operator import indexOf
import re
from utils import *
from pprint import pprint

# A, B, C -> Rock(1), Paper(2), Scissors(3)
# X, Y, Z -> Lose, Draw, Win
# Loss, draw, win -> 0, 3, 6

points = { "X": 1, "Y": 2, "Z": 3}
beats = { "A": "Y", "B": "Z", "C": "X"}
draws = { "A": "X", "B": "Y", "C": "Z"}

partTwoRoundPoints = { "X": 0, "Y": 3, "Z": 6 }
partTwoIndexOffset = { "X": -1, "Y": 0, "Z": 1 }
partTwoChoicePoints = { "A": 1, "B": 2, "C": 3 }

partOneScore = 0
partTwoScore = 0
for round in splitFile("day_02_input.txt", "\n"):
    inputs = splitString(round, " ")
    if len(inputs) == 2:
        partOneScore += points[inputs[1]]
        if beats[inputs[0]] == inputs[1]:
            partOneScore += 6
        elif draws[inputs[0]] == inputs[1]:
            partOneScore += 3
        
        partTwoScore += partTwoRoundPoints[inputs[1]]
        pointIndex = indexOf(partTwoChoicePoints, inputs[0]) + partTwoIndexOffset[inputs[1]]
        if (pointIndex > 0):
            pointIndex = pointIndex % len(partTwoChoicePoints)
        partTwoScore += list(partTwoChoicePoints.values())[pointIndex]
print("Part 1 score: " + str(partOneScore))
print("Part 2 score: " + str(partTwoScore))
