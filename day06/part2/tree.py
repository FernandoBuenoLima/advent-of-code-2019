class Node:
    def __init__(this, name):
        this.name = name
        this.children = []
        this.parent = None

    def addChild(this, node):
        this.children.append(node)
        node.parent = this
    
    def setParent(this, node):
        this.parent = node
        node.children.append(this)
    
    def countOrbits(this):
        count = 0
        current = this.parent
        while current is not None:
            count += 1
            current = current.parent
        return count


class Tree:
    def __init__(this):
        this.nodes = []
        
    def getNode(this, name):
        for node in this.nodes:
            if node.name == name:
                return node
        return None
        
    def addOrbit(this, orbitedName, orbiterName):
        orbited = this.getNode(orbitedName)
        orbiter = this.getNode(orbiterName)
        if orbited is None:
            orbited = Node(orbitedName)
            this.nodes.append(orbited)
        if orbiter is None:
            orbiter = Node(orbiterName)
            this.nodes.append(orbiter)
        orbited.addChild(orbiter)
    
    def countOrbits(this):
        total = 0
        for node in this.nodes:
            total += node.countOrbits()
        return total
