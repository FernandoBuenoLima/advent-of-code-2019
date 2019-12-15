from lib import *
from math import atan, degrees

def addAsteroidToList(list, asteroid, angle, distance):
    for o in list:
        if o[0] == angle:
            o[1].append((distance, asteroid))
            return
    list.append([angle, [(distance, asteroid)]])

def sortAnglesList(angles):
    angles.sort()
    for a in angles:
        a[1].sort()

def getAllAnglesFromAsteroid(asteroid, targets):
    angles = []
    for t in targets:
        x = t[0] - asteroid[0]
        y = t[1] - asteroid[1]
        if x >= 0 and y < 0:
            y = abs(y)
            angle = degrees(atan(x / y))
        elif x > 0 and y >= 0:
            angle = degrees(atan(y / x)) + 90
        elif x <= 0 and y > 0:
            x = abs(x)
            angle = degrees(atan(x / y)) + 180
        elif x < 0 and y <= 0:
            x = abs(x)
            y = abs(y)
            angle = degrees(atan(y / x)) + 270
        
        distance = x + y
        
        addAsteroidToList(angles, t, angle, distance)
    return angles
    

model = []

with open("input.txt") as file:
    for line in file:
        model.append(line.strip())

map = getMapFromInput(model)

asteroid = [26, 36]

targets = map.getAllAsteroids()
targets.remove(asteroid)
angles = getAllAnglesFromAsteroid(asteroid, targets)
sortAnglesList(angles)

asteroidsDestroyed = 0
currentRow = 0

while True:
    for a in angles:
        asts = a[1]
        if currentRow < len(asts):
            asteroidsDestroyed += 1
            if asteroidsDestroyed == 200:
                print("200th asteroid vaporized:", asts[currentRow][1])
                exit()
    currentRow += 1
