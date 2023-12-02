def splitFile(filename, regex):
    with open(filename) as f:
        return filter(None, f.read().split(regex))

def splitString(source, regex):
    return list(filter(None, source.split(regex)))

def splitStringAsNumbers(source, regex):
    return list(map(int, splitString(source, regex)))

def sumStringList(list):
    return sum(map(int, list))

def rangeInclusive(start, end, step = 1):
    return range(start, end + 1, step)