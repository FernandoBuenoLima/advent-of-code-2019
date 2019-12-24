from lib import *

reactionStrings = [l.strip() for l in open("input.txt").readlines()]

reactions = dict()

#load reactions
for rString in reactionStrings:
    parts = [p.strip() for p in rString.split("=>")]    
    inputs = [i.split() for i in [p.strip() for p in parts[0].split(',')]]
    output = parts[1].split()
    for i in inputs:
        i[0] = int(i[0])
    output[0] = int(output[0])
    reactions[output[1]] = Reaction(inputs, output)

fuel = 1
ore = getOreToBuildFuel(fuel, reactions)
oreToBuildOneFuel = ore

#I know, I'm disgusting
#It's 1am, sue me
while ore < 1000000000000:
    fuel += 1000
    ore = getOreToBuildFuel(fuel, reactions)

while ore > 1000000000000:
    fuel -= 100
    ore = getOreToBuildFuel(fuel, reactions)

while ore < 1000000000000:
    fuel += 1
    ore = getOreToBuildFuel(fuel, reactions)

print(fuel - 1)