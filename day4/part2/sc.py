
def hasExactlyDoubleDigits(p):
    previous = ''
    equalDigitsCount = 0
    for c in p:
        if c == previous:
            equalDigitsCount += 1
        else:
            if equalDigitsCount == 1:
                return True
            else:
                equalDigitsCount = 0
        previous = c
    return equalDigitsCount == 1

def neverDecreases(p):
    previous = -1
    for c in p:
        current = int(c)
        if current < previous:
            return False
        previous = current
    return True
    
def isValidPassword(p):
    return hasExactlyDoubleDigits(p) and neverDecreases(p)


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
