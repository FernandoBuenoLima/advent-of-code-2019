from tree import *
    
def pathfind(origin, target):
    path = [origin]
    return doPathfindRecursive(path, target)
    
def doPathfindRecursive(path, target):
    current = path[-1]
    if current == target:
        return len(path)-1
    nodes = []

    for node in current.children:
        if node not in path:
            nodes.append(node)

    if current.parent not in path:
        nodes.append(current.parent)
    
    for node in nodes:
        newPath = path.copy()
        newPath.append(node)
        ret = doPathfindRecursive(newPath, target)
        if ret > -1:
            return ret
    return -1
    
    
orbits = []

with open("input.txt") as file:
    for line in file:
        orbits.append(line.strip())

tree = Tree()

for orbit in orbits:
    orbitNames = orbit.split(')')
    tree.addOrbit(orbitNames[0], orbitNames[1])

you = tree.getNode("YOU")
san = tree.getNode("SAN")

print(pathfind(you.parent, san.parent))
