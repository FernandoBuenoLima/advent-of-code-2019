
def calculateEnergy(a):
    return abs(a[0]) + abs(a[1]) + abs(a[2])

class Moon:
    def __init__(this, name, position):
        this.name = name
        this.position = position
        this.velocity = [0, 0, 0]

    def __str__(this):
        s = "pos=<" + str(this.position[0])
        s += ", " + str(this.position[1])
        s += ", " + str(this.position[2]) + ">, "
        s += "vel=<" + str(this.velocity[0])
        s += ", " + str(this.velocity[1])
        s += ", " + str(this.velocity[2]) + ">"
        return s
    
    def getPotentialEnergy(this):
        return calculateEnergy(this.position)
        
    def getKineticEnergy(this):
        return calculateEnergy(this.velocity)
        
    def getTotalEnergy(this):
        return this.getPotentialEnergy() * this.getKineticEnergy()
        
    def addVelocityToAxis(this, axis, value):
        this.velocity[axis] += value
        
    def move(this):
        this.position[0] += this.velocity[0]
        this.position[1] += this.velocity[1]
        this.position[2] += this.velocity[2]

class MoonSystem:
    def __init__(this, positions):
        this.moons = []
        
        names = ["Io", "Europa", "Ganymede", "Callisto"]
        for i in range(len(positions)):
            this.moons.append(Moon(names[i], positions[i]))
    
    def __str__(this):
        s = ""
        for m in this.moons:
            s += str(m) + "\n"
        return s
    
    def getTotalEnergy(this):
        total = 0
        for moon in this.moons:
            total += moon.getTotalEnergy()
        return total
    
    def simulate(this, steps):
        for s in range(steps):
            this.step()
            #print("After", s+1, "steps:")
            #print(str(this))
            
    def step(this):
        for i in range(len(this.moons)-1):
            for j in range(i+1, len(this.moons)):
                this.applyGravity(this.moons[i], this.moons[j])
        for moon in this.moons:
            moon.move()
                
    def applyGravity(this, m1, m2):
        for i in range(3):
            m1i = m1.position[i]
            m2i = m2.position[i]
            if m1i > m2i:
                m1.addVelocityToAxis(i, -1)
                m2.addVelocityToAxis(i, 1)
            elif m1i < m2i:
                m1.addVelocityToAxis(i, 1)
                m2.addVelocityToAxis(i, -1)
