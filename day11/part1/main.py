from ehpr import EmergencyHullPaintingRobot

program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))
        
robot = EmergencyHullPaintingRobot(program)
robot.start()

print(len(robot.paintedPanels))