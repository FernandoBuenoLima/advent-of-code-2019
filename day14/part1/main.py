from lib import *

reactionStrings = [l.strip() for l in open("input.txt").readlines()]

reactions = dict()
components = dict()
ore = 0

#load reactions
for rString in reactionStrings:
    parts = [p.strip() for p in rString.split("=>")]    
    inputs = [i.split() for i in [p.strip() for p in parts[0].split(',')]]
    output = parts[1].split()
    for i in inputs:
        i[0] = int(i[0])
    output[0] = int(output[0])
    reactions[output[1]] = Reaction(inputs, output)

#load components
for v in reactions:    
    components[v] = 0
components["FUEL"] = 1

#solve it
nextName = getNextRequirement(components)

while nextName is not None:
    reaction = reactions[nextName]
    amountRequired = components[nextName]
    amountProduced = reaction.output[0]
    amountOfReactions = amountRequired // amountProduced
    
    if amountRequired > amountProduced * amountOfReactions:
        amountOfReactions += 1
    
    components[nextName] -= (amountProduced * amountOfReactions)
    for c in reaction.inputs:
        if c[1] == "ORE":
            ore += (c[0] * amountOfReactions)
        else:
            components[c[1]] += (c[0] * amountOfReactions)
    
    nextName = getNextRequirement(components)
    
print(ore)