from lib import *

model = []

with open("input.txt") as file:
    for line in file:
        model.append(line.strip())

map = getMapFromInput(model)
map.show()

biggestScore = -1
biggestScoreLocation = None
asteroids = map.getAllAsteroids()

for a in asteroids:
    currentMap = map.getCopy()
    currentMap.removeAllAsteroidsNotSeenFromStation(a[0], a[1])
    count = currentMap.getAsteroidCount() - 1
    if count > biggestScore:
        biggestScore = count
        biggestScoreLocation = a
    

print(biggestScoreLocation[0], biggestScoreLocation[1], " - ", biggestScore)