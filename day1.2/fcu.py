
def calculateFuelForMass(mass):
    return (mass // 3) - 2

def calculateTotalFuelForModule(mass):
    total = 0
    add = calculateFuelForMass(mass)
    while add > 0:
        total += add
        add = calculateFuelForMass(add)
    return total
    
    
sum = 0

with open("input.txt") as file:
    for line in file:
        sum += calculateTotalFuelForModule(int(line))
        
print(sum)
