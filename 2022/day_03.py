from fileinput import filename
from operator import contains
from utils import *
from pprint import pprint

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
rucksacks = list(splitFile("day_03_input.txt", "\n"))
for rucksack in rucksacks:
    firstCompartment = rucksack[slice(0, len(rucksack)//2)]
    secondCompartment = rucksack[slice(len(rucksack)//2, len(rucksack))]
    for item in firstCompartment:
        if item in secondCompartment:
            sum += alphabet.index(item) + 1 # Offset for 0-indexing
            break
print("Total part 1 sum: ", sum)

sum = 0
for i in range(0, len(rucksacks)-2, 3):
    for item in rucksacks[i]:
        if item in rucksacks[i+1] and item in rucksacks[i+2]:
            sum += alphabet.index(item) + 1 # OFfset for 0-indexing
            break
print("Total part 2 sum: ", sum)
