
def hasDoubleDigits(p):
    previous = ''
    for c in p:
        if c == previous:
            return True
        previous = c
    return False

def neverDecreases(p):
    previous = -1
    for c in p:
        current = int(c)
        if current < previous:
            return False
        previous = current
    return True
    
def isValidPassword(p):
    return hasDoubleDigits(p) and neverDecreases(p)


def findNumberOfPasswords(min, max):
    current = min
    count = 0
    while current <= max:
        s = str(current)
        if isValidPassword(s):
            count += 1
        current += 1

    return count

MIN_VALUE = 245182
MAX_VALUE = 790572

print(findNumberOfPasswords(MIN_VALUE, MAX_VALUE))
