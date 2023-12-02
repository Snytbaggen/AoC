from utils import *

number_strings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lines = splitFile("day_01_input.txt", "\n")
total_sum = 0
for line in lines:
    numbers = [ ]
    for i, c in enumerate(line):
        if (c.isdigit()):
            numbers.append(c)
        else:
            for key in number_strings.keys():
                if line[i:].startswith(key):
                    numbers.append(number_strings[key])
                    break
    line_sum = numbers[0] + numbers[-1]
    total_sum += int(line_sum)

print("Total sum: " + str(total_sum))