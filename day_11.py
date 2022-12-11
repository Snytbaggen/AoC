from utils import *
from pprint import pprint
from functools import cmp_to_key
from math import floor

class Operation():
    def __init__(self, operator, operand) -> None:
        self.operator: str = operator
        self.operand: str = operand

class Monkey():
    def __init__(self, items, operation, testValue, targetIfTrue, targetIfFalse) -> None:
        self.items: list[int] = items
        self.operation: Operation = operation
        self.testValue: int = int(testValue)
        self.targetIfTrue = int(targetIfTrue)
        self.targetIfFalse = int(targetIfFalse)
        self.inspectionCount = 0

def parseMonkey(rawMonkey):
    rawItems = splitString(rawMonkey[1], ": ")
    items = splitStringAsNumbers(rawItems[1], ", ")

    rawOperation = splitString(rawMonkey[2], " = ")
    operation = splitString(rawOperation[1], " ")

    testValue = splitString(rawMonkey[3], " ")[-1]
    targetIfTrue = splitString(rawMonkey[4], " ")[-1]
    targetIfFalse = splitString(rawMonkey[5], " ")[-1]
    return Monkey(items, Operation(operation[1], operation[2]), testValue, targetIfTrue, targetIfFalse)

def printMonkey(monkey: Monkey):
    print("Items:", monkey.items)
    print("Operator:", monkey.operation.operator, monkey.operation.operand)
    print("Test value:", monkey.testValue)
    print("If true:", monkey.targetIfTrue)
    print("If false:", monkey.targetIfFalse)

monkeys: list[Monkey] = []
for rawMonkey in splitFile("day_11_input.txt", "\n\n"):
    monkeys.append(parseMonkey(splitString(rawMonkey, "\n")))

lcd = 1
for monkey in monkeys:
    lcd *= monkey.testValue

for i in range(0, 10000):
    for monkey in monkeys:
        operator = monkey.operation.operator
        for worryLevel in monkey.items:
            monkey.inspectionCount += 1

            operand = worryLevel if monkey.operation.operand == "old" else int(monkey.operation.operand)
            if operator == "*":
                worryLevel *= operand
            elif operator == "+":
                worryLevel += operand
            elif operator == "-":
                worryLevel -= operand
            elif operator == "/":
                worryLevel = floor(worryLevel / operand)

            worryLevel = worryLevel % lcd
            # worryLevel = floor(worryLevel / 3)

            if (worryLevel % monkey.testValue == 0):
                monkeys[monkey.targetIfTrue].items.append(worryLevel)
            else:
                monkeys[monkey.targetIfFalse].items.append(worryLevel)
        monkey.items = []

sortedMonkeys = sorted(monkeys, key=cmp_to_key(lambda m1, m2: m2.inspectionCount - m1.inspectionCount))
print("Sum:", sortedMonkeys[0].inspectionCount * sortedMonkeys[1].inspectionCount)