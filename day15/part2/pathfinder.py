from lib import *

class Pathfinder:
    def __init__(this, map):
        this.map = map
        this.a = None
        this.b = None
        
    def getWaysFromPoint(this, point):
        paths = []
        possiblePaths = []
        
        possiblePaths.append([point[0], point[1]-1])
        possiblePaths.append([point[0]+1, point[1]])
        possiblePaths.append([point[0], point[1]+1])
        possiblePaths.append([point[0]-1, point[1]])
        
        for p in possiblePaths:
            if this.map[p[0]][p[1]] in [EMPTY, OXYGEN_SYSTEM]:
                paths.append(p)
        return paths
        
    def find(this, a, b):
        this.a = a
        this.b = b
        path = []
        path = this._findRec(path, a)
        del path[0]
        return path
    
    def _findRec(this, path, current):
        path.append(current)
        if current == this.b:
            return path
        for way in this.getWaysFromPoint(current):
            if way not in path:
                ret = this._findRec(path.copy(), way)
                if ret is not None:
                    return ret
        return None
    