from ehpr import EmergencyHullPaintingRobot

program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))
        
robot = EmergencyHullPaintingRobot(program)
robot.start()
panels = robot.paintedPanels

biggestX = -1
biggestY = -1

for p in panels:
    if p[0] > biggestX:
        biggestX = p[0]
    if p[1] > biggestY:
        biggestY = p[1]
        
image = []
for i in range(biggestX+1):
    image.append(['.'] * (biggestY+1))
    
for p in panels:
    image[p[0]][p[1]] = '.' if panels[p] == 0 else '#'

for line in image:
    s = ""
    for c in line:
        s += c
    print(s)
