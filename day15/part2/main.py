from intcode import IntcodeComputer
from lib import *
from explorer import Explorer

computer = IntcodeComputer(open("input.txt").read())
map = [[UNKNOWN for i in range(250)] for j in range(250)]
droid = [125, 125]
map[droid[0]][droid[1]] = EMPTY

droid = DroidControl(computer, map, droid)

explorer = Explorer(droid)
explorer.explore()

r = droid.fillMapWithOxygen()

droid.drawMap()
print(r)