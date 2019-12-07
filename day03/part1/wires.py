from ds import *

def getIntersection(e1, e2):
    if e1.isHorizontal() == e2.isHorizontal():
        return None
    
    hor = e1 if e1.isHorizontal() else e2
    ver = e1 if not e1.isHorizontal() else e2
    
    yh = hor.a.y
    xv = ver.a.x
    
    if yh < ver.a.y or yh > ver.b.y or xv < hor.a.x or xv > hor.b.x:
        return None
    
    return Point(xv, yh)

def getIntersectionClosestToOriginDistance(w1, w2):
    intersections = []
    
    for e1 in w1.edges:
        for e2 in w2.edges:
            p = getIntersection(e1, e2)
            if not p:
                continue    
            if p.distanceFromOrigin() == 0:
                continue        
            intersections.append(p)
    
    closest = intersections[0].distanceFromOrigin()
    for i in intersections:
        if i.distanceFromOrigin() < closest:
            closest = i.distanceFromOrigin()
    return closest

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

result = getIntersectionClosestToOriginDistance(w1, w2)
    
print(result)
