import copy

class Point:
    def __init__(this, x, y):
        this.x = x
        this.y = y
    
    def __str__(this):
        return "[" + str(this.x) + ", " + str(this.y) + "]"
    def __repr__(this):
        return str(this)
    
    def distanceFromOrigin(this):
        return abs(this.x) + abs(this.y)
    
class Edge:
    def __init__(this, a, b):
        this.a = a
        this.b = b
    
    def isHorizontal(this):
        return this.a.y == this.b.y
        
    def __str__(this):
        return str(this.a) + " - " + str(this.b)
    
class Command:
    def __init__(this, scode):
        this.direction = scode[0]
        this.scale = int(scode[1:])
    
    def __str__(this):
        return this.direction + str(this.scale)
    def __repr__(this):
        return str(this)

def addCommandToPoint(point, command):
    a = copy.deepcopy(point)
    if command.direction == 'U':
        return Point(a.x, a.y + command.scale)
    elif command.direction == 'R':
        return Point(a.x + command.scale, a.y)
    elif command.direction == 'D':
        return Point(a.x, a.y - command.scale)
    elif command.direction == 'L':
        return Point(a.x - command.scale, a.y) 
        
def buildEdgeFromPointAndCommand(a, command):
    a = copy.deepcopy(a)
    b = addCommandToPoint(a, command)
    
    if command.direction == 'U' or command.direction == 'R':        
        return Edge(a, b), b
    else:        
        return Edge(b, a), b
    
    
class Wire:
    def __init__(this, commands):
        p = Point(0, 0)
        this.edges = []
        
        for c in commands:
            edge, p = buildEdgeFromPointAndCommand(p, c)
            this.edges.append(edge)
    
    def __str__(this):
        r = ""
        for e in this.edges:
            r += "\n" + str(e)
        return r[1:]
        