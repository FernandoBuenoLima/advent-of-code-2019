
def calculateFuelForModuleWithMass(mass):
    return (mass // 3) - 2


sum = 0

with open("input.txt") as file:
    for line in file:
        moduleMass = int(line)
        sum += calculateFuelForModuleWithMass(moduleMass)
        
print(sum)
