from lib import *
from pathfinder import Pathfinder

class Explorer:
    def __init__(this, droid):
        this.droid = droid
        this.pathfinder = Pathfinder(this.droid.map)
        this.visited = []
        this.intersections = []
        
    def explore(this):
        while True:
            this.visited.append(this.droid.position)
            exits = this.getExitsFromCurrentPosition()
            
            if len(exits) == 0:
                if len(this.intersections) == 0:
                    return
                inter = this.intersections[-1]
                path = this.pathfinder.find(this.droid.position, inter)
                this.droid.moveThroughPath(path)
                if len(this.getExitsFromCurrentPosition()) == 1:
                    this.intersections.pop()
            elif len(exits) == 1:
                this.droid.move(exits[0])
            else:
                assert len(exits) > 1
                if this.droid.position not in this.intersections:
                    this.intersections.append(this.droid.position)
                this.droid.move(exits[0])
                
            
    
    def getExitsFromCurrentPosition(this):
        ret = []
        droid = this.droid
        
        result = droid.move(NORTH)
        if result in [MOVED, FOUND_SYSTEM]:
            if droid.position not in this.visited:
                ret.append(NORTH)
            droid.move(SOUTH)
            
        result = droid.move(SOUTH)
        if result in [MOVED, FOUND_SYSTEM]:
            if droid.position not in this.visited:
                ret.append(SOUTH)
            droid.move(NORTH)
        
        result = droid.move(EAST)
        if result in [MOVED, FOUND_SYSTEM]:
            if droid.position not in this.visited:
                ret.append(EAST)
            droid.move(WEST)
            
        result = droid.move(WEST)
        if result in [MOVED, FOUND_SYSTEM]:
            if droid.position not in this.visited:
                ret.append(WEST)
            droid.move(EAST)
        
        return ret