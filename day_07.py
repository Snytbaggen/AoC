from __future__ import annotations
from utils import *

class File():
    def __init__(self, parent, name, type, size) -> None:
        self.parent: File = parent
        self.name: str = name
        self.type: str = type
        self.size: int = size
        self.files: list[File] = []

def findDir(folder: File, name):
    if name == '/' and folder.name == '/': return folder
    for f in folder.files:
        if f.name == name and f.type == 'dir':
            return f

def findDirectorySize(folder:File, sizeLimit = -1):
    sum = 0
    for file in folder.files:
        if (file.type == 'dir'):
            sum += findDirectorySize(file)
        else:
            sum += file.size
    return sum

def sumAllfolders(root:File, sizeLimit):
    sum = 0
    for file in root.files:
        if (file.type == 'dir'):
            dirSize = findDirectorySize(file)
            if (dirSize < sizeLimit):
                sum += dirSize
            sum += sumAllfolders(file, sizeLimit)
    return sum

def findSmallestFolderAbove(root: File, targetSize, currentSmallest = -1):
    for file in root.files:
        if file.type == 'dir':
            dirSize = findDirectorySize(file)
            if dirSize > targetSize and (dirSize < currentSmallest or currentSmallest == -1):
                currentSmallest = dirSize
            currentSmallest = findSmallestFolderAbove(file, targetSize, currentSmallest)
    return currentSmallest

structure = File(None, '/', 'dir', 0)
currentFolder = structure
for cmd in splitFile("day_07_input.txt", "\n"):
    elements = splitString(cmd, " ")
    if elements[0] == '$':
        if elements[1] == 'cd':
            if elements[2] == '..':
                currentFolder = currentFolder.parent
            else:
                currentFolder = findDir(currentFolder, elements[2])
        elif elements[1] == 'ls':
            None # Ignore the command
    elif elements[0] == 'dir':
        currentFolder.files.append(File(currentFolder, elements[1], 'dir', 0))
    else:
        currentFolder.files.append(File(currentFolder, elements[1], 'file', int(elements[0])))

totalSize = findDirectorySize(structure)
emptySpace = 70000000 - totalSize
spaceNeeded = 30000000 - emptySpace

print("Sum of folders smaller than 100000: ", sumAllfolders(structure, 100000))
print("Smallest folder to delete: ", findSmallestFolderAbove(structure, spaceNeeded))
