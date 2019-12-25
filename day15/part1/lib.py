#MOVEMENT
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

directionNamesDict = { 'w': NORTH, 's': SOUTH, 'a': WEST, 'd': EAST }
directionsDict = { NORTH: [0, -1], SOUTH: [0, 1], WEST: [-1, 0], EAST:[1, 0] }

#RESPONSES
HIT_WALL = 0
MOVED = 1
FOUND_SYSTEM = 2

#MAP
UNKNOWN = ' '
EMPTY = '.'
WALL = '#'
OXYGEN_SYSTEM = 'O'

class DroidControl:
    def __init__(this, computer, map, startingPosition):
        this.computer = computer
        this.map = map
        this.startingPosition = startingPosition
        this.position = startingPosition.copy()
        
    def getPositionContent(this, p):
        return this.map[p[0]][p[1]]
    
    def getCurrentPositionContent(this):
        return this.getPositionContent(this.position)
    
    def isAdjacent(this, p):
        return abs(this.position[0]-p[0]) + abs(this.position[1]-p[1]) == 1
    
    def move(this, direction):
        delta = directionsDict[direction]
        
        newPosition = this.position.copy()
        newPosition[0] += delta[0]
        newPosition[1] += delta[1]
        
        response = this.computer.run([direction])
        
        if response == HIT_WALL:
            this.map[newPosition[0]][newPosition[1]] = WALL
        elif response == MOVED:
            this.map[newPosition[0]][newPosition[1]] = EMPTY
            this.position = newPosition
        else:
            assert response == FOUND_SYSTEM
            this.map[newPosition[0]][newPosition[1]] = OXYGEN_SYSTEM
            this.position = newPosition
        
        return response
    
    def moveToAdjacentPosition(this, p):
        assert this.isAdjacent(p)
        
        if p[0] < this.position[0]:
            assert p[1] == this.position[1]
            assert p[0] + 1 == this.position[0]
            this.move(WEST)
        elif p[0] > this.position[0]:
            assert p[1] == this.position[1]
            assert p[0] - 1 == this.position[0]
            this.move(EAST)
        elif p[1] < this.position[1]:
            assert p[0] == this.position[0]
            assert p[1] + 1 == this.position[1]
            this.move(NORTH)
        else:
            assert p[0] == this.position[0]
            assert p[1] - 1 == this.position[1]
            this.move(SOUTH)
    
    def moveThroughPath(this, path):
        for step in path:
            this.moveToAdjacentPosition(step)
    
    def drawMap(this, rangeX = 15, rangeY = 9):
        map = this.map
        droid = this.position
        
        print("\n\n")
        yBarrier = ""
        for i in range(rangeX*2  + 3):
            yBarrier += '='
            
        print(yBarrier)
        for y in range(droid[1]-rangeY, droid[1]+rangeY+1):
            line = '|'
            for x in range(droid[0]-rangeX, droid[0]+rangeX+1):
                if [x, y] == droid:
                    line += 'D'
                else:
                    line += map[x][y]
            line += '|'
            print(line)
        print(yBarrier)
        print("\n")

    def activateManualControl(this):
        while True:
            this.drawMap()
            dir = input("direction? ")
            while dir not in ['w','a','s','d']:
                if dir == 'q':
                    return False
                dir = input("direction? ")
            
            dir = directionNamesDict[dir]
            response = this.move(dir)
            
            if response == FOUND_SYSTEM:
                print("\n\n\nFOUND SYSTEM\n\n")
                return True
                