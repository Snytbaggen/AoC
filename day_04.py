from utils import *

# Returns True if range1 contains range2
def containsRange(range1, range2):
    return range2[0] >= range1[0] and range2[1] <= range1[1]

# Returns True if range1 contains range2
def overlapsRange(range1, range2):
    return range2[0] >= range1[0] and range2[0] <= range1[1]

duplicateRanges = 0
overlappingRanges = 0
for pair in splitFile("day_04_input.txt", "\n"):
    elves = splitString(pair, ",")
    elfOne = splitStringAsNumbers(elves[0], "-")
    elfTwo = splitStringAsNumbers(elves[1], "-")
    if containsRange(elfOne, elfTwo) or containsRange(elfTwo, elfOne):
        duplicateRanges += 1
    if overlapsRange(elfOne, elfTwo) or overlapsRange(elfTwo, elfOne):
        overlappingRanges += 1

print("Duplicate ranges: ", duplicateRanges)
print("Overlapping ranges: ", overlappingRanges)