from utils import *
import sys

class MapRange():
    def __init__(self, rawRange) -> None:
        range = splitStringAsNumbers(rawRange, " ")
        self.destStart = range[0]
        self.sourceStart = range[1]
        self.length = range[2]

    def getMappedNumber(self, sourceNumber):
        return self.destStart + (sourceNumber - self.sourceStart) if self.contains(sourceNumber) else sourceNumber
    
    def contains(self, sourceNumber):
        return sourceNumber >= self.sourceStart and sourceNumber < self.sourceStart + self.length

class AocMap():
    def __init__(self, rawMap) -> None:
        self.ranges = [ ]
        for i, line in enumerate(splitString(rawMap, "\n")):
            if i == 0:
                self.title = line
            else:
                self.ranges.append(MapRange(line))
    
    def getMappedNumber(self, sourceNumber):
        for range in self.ranges:
            if range.contains(sourceNumber):
                return range.getMappedNumber(sourceNumber)
        return sourceNumber

seeds = [ ]
out = [ ]
maps = [ ]
for i, block in enumerate(splitFile("day_05_input.txt", "\n\n")):
    if (i == 0):
        seeds = list(map(int, splitString(block, " ")[1:]))
        out = seeds.copy()
    else:
        maps.append(AocMap(block))

# Part 1
for map in maps:
    for i, seed in enumerate(seeds):
        out[i] = map.getMappedNumber(seed)
print(min(out))

# Part 2
# This is really inefficient and takes almost 5 hours to complete on an M1 Pro.
# It'd be better to look at ranges instead of every number, but this was easier to implement.
closestSeed = sys.maxsize
for i in range(0, len(seeds)-1, 2):
    for seed in range(seeds[i], seeds[i] + seeds[i+1]):
        val = seed
        for map in maps:
            val = map.getMappedNumber(val)
        closestSeed = min(val, closestSeed)
print(closestSeed)

