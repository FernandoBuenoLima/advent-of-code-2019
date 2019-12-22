from lib import *

def readPositionFromString(s):
    x = s.find('x') + 2
    y = s.find('y') + 2
    z = s.find('z') + 2
    x_end = s.find(',', x)
    y_end = s.find(',', y)
    z_end = s.find('>', z)
    return [int(s[x:x_end]), int(s[y:y_end]), int(s[z:z_end])]
    
positions = []
    
with open("input.txt") as file:
    for line in file:
        positions.append(readPositionFromString(line))
        
system = MoonSystem(positions)
system.simulate(100000)
print(system.getTotalEnergy())
