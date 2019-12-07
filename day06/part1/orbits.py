from tree import *

orbits = []

with open("input.txt") as file:
    for line in file:
        orbits.append(line.strip())

tree = Tree()

for orbit in orbits:
    orbitNames = orbit.split(')')
    tree.addOrbit(orbitNames[0], orbitNames[1])

print(tree.countOrbits())
