from ds import *

def getIntersectionAndCost(e1, e2):
    if e1.isHorizontal() == e2.isHorizontal():
        return None, None
    
    hor = e1 if e1.isHorizontal() else e2
    ver = e1 if not e1.isHorizontal() else e2
    
    yh = hor.a.y
    xv = ver.a.x
    
    if yh < ver.a.y or yh > ver.b.y or xv < hor.a.x or xv > hor.b.x:
        return None, None

    p = Point(xv, yh)
    c = hor.cost + ver.cost
    
    c += hor.i.distanceFromPoint(p) + ver.i.distanceFromPoint(p)
    
    return p, c

def getIntersectionWithLowestCost(w1, w2):
    costs = []
    
    for e1 in w1.edges:
        for e2 in w2.edges:
            p, c = getIntersectionAndCost(e1, e2)
            if not p:
                continue    
            if p.distanceFromOrigin() == 0:
                continue        
            costs.append(c)
    
    lowest = costs[0]
    for c in costs:
        if c < lowest:
            lowest = c
    return lowest

arrays = []
with open("input.txt") as file:
    for line in file:
        arrays.append([s.strip() for s in line.split(',')])

s1 = arrays[0]
s2 = arrays[1]

c1 = [Command(s) for s in s1]
c2 = [Command(s) for s in s2]

w1 = Wire(c1)
w2 = Wire(c2)

result = getIntersectionWithLowestCost(w1, w2)
    
print(result)
