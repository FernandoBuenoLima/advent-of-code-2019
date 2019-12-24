
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
    