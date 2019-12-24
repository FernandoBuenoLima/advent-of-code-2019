
class Reaction:
    def __init__(this, inputs, output):
        this.inputs = inputs
        this.output = output

    def __str__(this):
        return str(this.inputs) + " - " + str(this.output)

    def __repr__(this):
        return str(this)
        
def getNextRequirement(components):
    for c in components:
        if components[c] > 0:
            return c
    return None

def getOreToBuildFuel(amount, reactions):
    components = dict()
    ore = 0
    
    #load components
    for v in reactions:    
        components[v] = 0
    components["FUEL"] = amount
    
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
        
    return ore