from utils import *

lines = list(splitFile("day_06_input.txt", "\n"))
times = list(map(int, lines[0].split()[1:]))
dists = list(map(int, lines[1].split()[1:]))

def getRaceScore(time, dist):
    raceCounter = 0
    for holdTime in rangeInclusive(0, time):
        travelDist = (time - holdTime) * holdTime
        if travelDist > dist:
            raceCounter += 1
    return raceCounter

# Part 1
counter = 1
for i in range(0, len(times)):
    time = times[i]
    dist = dists[i]
    raceCounter = getRaceScore(time, dist)
    counter = counter * raceCounter if raceCounter >= 1 else counter
print(counter)

# Part 2
time = int(''.join(list(map(str, times))))
dist = int(''.join(list(map(str, dists))))
print(getRaceScore(time, dist))

    