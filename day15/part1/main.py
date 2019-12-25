from intcode import IntcodeComputer
from lib import *
from explorer import Explorer

computer = IntcodeComputer(open("input.txt").read())
map = [[UNKNOWN for i in range(1000)] for j in range(1000)]
droid = [500, 500]
map[droid[0]][droid[1]] = EMPTY

droid = DroidControl(computer, map, droid)

explorer = Explorer(droid)
print(len(explorer.explore()))

#droid.activateManualControl()
