from copy import deepcopy

def getMapFromInput(inputMap):
    innerMap = []
    for line in inputMap:
        nl = []
        for c in line:
            nl.append(c)
        innerMap.append(nl)
    return Map(innerMap)

def simplify(x, y):
    d = abs(y)
    while d > 1:
        if x % d == 0 and y % d == 0:
             return simplify(x // d, y // d)
        d -= 1
    return x, y

class Map:
    def __init__(this, model):
        this.innerMap = model
        this.width = len(this.innerMap[0])
        this.height = len(this.innerMap)
    
    def getCopy(this):
        return Map(deepcopy(this.innerMap))
    
    def show(this):
        for line in this.innerMap:
            print(line)
        print("\n\n")
    
    def isAsteroid(this, x, y):
        return this.getData(x, y) == '#'
    
    def isEmpty(this, x, y):
        return this.getData(x, y) == '.'
    
    def getData(this, x, y):
        return this.innerMap[y][x]
    
    def setData(this, x, y, data):
        this.innerMap[y][x] = data

    def getAllAsteroids(this):
        asteroids = []
        for y in range(this.height):
            for x in range(this.width):
                if this.isAsteroid(x, y):
                    asteroids.append([x, y])
        return asteroids
    
    def getAsteroidCount(this):
        return len(this.getAllAsteroids())
    
    def removeAllAsteroidsNotSeenFromStation(this, x, y):
        asteroids = this.getAllAsteroids()
        asteroids.remove([x,y])
        asteroidsRemoved = asteroids.copy()
            
        for asteroid in asteroids:
            start_x, start_y = asteroid[0], asteroid[1]
            diff_x, diff_y = 0, 0
            if x == start_x:
                diff_y = 1 if start_y > y else -1
            elif y == start_y:
                diff_x = 1 if start_x > x else -1
            else:
                diff_x = start_x - x
                diff_y = start_y - y
                diff_x, diff_y = simplify(diff_x, diff_y)
            
            start_x += diff_x
            start_y += diff_y
            
            while start_x >= 0 and start_y >= 0 and start_x < this.width and start_y < this.height:
                if [start_x, start_y] in asteroidsRemoved:
                    asteroidsRemoved.remove([start_x, start_y])
                    this.setData(start_x, start_y, '.')
                start_x += diff_x
                start_y += diff_y
