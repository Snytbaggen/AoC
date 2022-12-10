from utils import *
import day_10_state as state

state.instructions = list(splitFile("day_10_input.txt", "\n"))

printInstructions = False

signalStrength = 0
def checkSignalStrength():
    global signalStrength
    if state.cpuCycles == 20 or (state.cpuCycles - 20) % 40 == 0:
        signalStrength += state.cpuCycles * state.registerX

currentLine = ''
def checkDrawState():
    global currentLine
    currentLinePos = (state.cpuCycles - 1) % 40
    if currentLinePos in range(state.registerX-1, state.registerX+2):
        currentLine += '#'
    else:
        currentLine += '.'
    if currentLinePos == 39:
        print(currentLine)
        currentLine = ''


def checkCycle():
    checkSignalStrength()
    checkDrawState()

def fetchNextInstruction():
    state.programCounter += 1
    if (state.programCounter >= len(state.instructions)):
        state.halt = True
    else:
        state.currentInstruction = splitString(state.instructions[state.programCounter], " ")
    state.instructionCounter = 0

def isCurrentInstructionExecuting():
    return state.instructionCounter < state.instructionCycles[state.currentInstruction[0]]

fetchNextInstruction()
while not state.halt:
    state.cpuCycles += 1
    state.instructionCounter += 1
    checkCycle()

    if (isCurrentInstructionExecuting()):
        if printInstructions: print(state.cpuCycles, "Waiting", state.currentInstruction[0])
        continue

    instructionType = state.currentInstruction[0]
    if (instructionType == "noop"):
        if printInstructions: print(state.cpuCycles, "Noop")
    elif (instructionType == "addx"):
        if printInstructions: print(state.cpuCycles, "Adding", int(state.currentInstruction[1]))
        state.registerX += int(state.currentInstruction[1])
    
    fetchNextInstruction()

print("Signal strength:", signalStrength)