from utils import *
from pprint import pprint
import time

starttime = time.time()

class ScratchCard():
    def __init__(self, winningNumbers, cardNumbers) -> None:
        self.winningNumbers = winningNumbers
        self.cardNumbers = cardNumbers
        self.copyCount = 1
    
    def partOneScore(self):
        cardScore = 0
        for number in self.cardNumbers:
            if number in self.winningNumbers:
                cardScore = 1 if cardScore == 0 else cardScore * 2
        return cardScore
    
    def getMatchingNumbersCount(self):
        count = 0
        for number in self.cardNumbers:
            if number in self.winningNumbers:
                count += 1
        return count

scratchCards = [ ]
for line in splitFile("day_04_input.txt", "\n"):
    rawCard = splitString(splitString(line, ":")[1], " |")
    winningNumbers = splitString(rawCard[0], " ")
    cardNumbers = splitString(rawCard[1], " ")
    scratchCards.append(ScratchCard(winningNumbers, cardNumbers))

# Part 1
partOneScore = 0
for card in scratchCards:
    partOneScore += card.partOneScore()

# Part 2
partTwoScore = 0
for i, card in enumerate(scratchCards):
    for nextIndex in rangeInclusive(i + 1, i + card.getMatchingNumbersCount()):
        scratchCards[nextIndex].copyCount += card.copyCount
    partTwoScore += card.copyCount

print(partOneScore)
print(partTwoScore)
print("Execution time: " + str((time.time() - starttime) * 1000) + " ms")

test = False
if test:
    print("asdf")