import imp
from utils import *

elves = [ ]
for elf in splitFile("day_01_input.txt", "\n\n"):
    elves.append(sumStringList(splitString(elf, "\n")))

elves.sort(reverse=True)
print("First elf carries " + str(elves[0]) + " calories")
print("First three elves carry " + str(elves[0] + elves[1] + elves[2]) + " calories")