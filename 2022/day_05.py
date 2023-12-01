from utils import *
from pprint import pprint

# Input:
# [M] [H]         [N]                
# [S] [W]         [F]     [W] [V]    
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M'],
    ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H'],
    ['W', 'R', 'C', 'D', 'G'],
    ['N', 'B', 'S'],
    ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N'],
    ['P', 'R', 'M', 'W'],
    ['R', 'T', 'N', 'G', 'L', 'S', 'W'],
    ['Q', 'T', 'H', 'F', 'N', 'B', 'V'],
    ['L', 'M', 'H', 'Z', 'N', 'F']
  ]

steps = []

for line in splitFile("day_05_input.txt", "\n"):
    elements = splitString(line, " ")
    steps.append(
        [int(elements[1]), int(elements[3])-1, int(elements[5])-1]
    )

for step in steps:
    targetStack = stacks[step[1]]
    rangeToModify = slice(len(targetStack) - step[0], len(targetStack))
    stacks[step[2]].extend(targetStack[rangeToModify])
    del targetStack[rangeToModify]

    # for i in range(0, step[0]):
    #     stacks[step[2]].append(stacks[step[1]].pop())

pprint(stacks)

result = ''
for stack in stacks:
    result += stack.pop()
print(result)