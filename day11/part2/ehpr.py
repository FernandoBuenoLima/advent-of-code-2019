from intcode import IntcodeComputer

class EmergencyHullPaintingRobot:
    def __init__(this, program):
        this.computer = IntcodeComputer(program)
        this.position = (0,0)
        this.direction = 'U'
        this.paintedPanels = dict()
        this.paintedPanels[(0,0)] = 1
    
    def getCurrentPanelColor(this):
        panel = this.position
        if panel not in this.paintedPanels:
            return 0
        return this.paintedPanels[panel]
    
    def paintPanel(this, color):
        this.paintedPanels[this.position] = color
    
    def turn(this, direction):
        if this.direction == 'U':
            this.direction = 'L' if direction == 0 else 'R'
        elif this.direction == 'R':
            this.direction = 'U' if direction == 0 else 'D'
        elif this.direction == 'D':
            this.direction = 'R' if direction == 0 else 'L'
        elif this.direction == 'L':
            this.direction = 'D' if direction == 0 else 'U'
    
    def move(this, direction):
        this.turn(direction)
        pos = this.position
        if this.direction == 'U':
            this.position = (pos[0]-1, pos[1])
        elif this.direction == 'R':
            this.position = (pos[0], pos[1]+1)
        elif this.direction == 'D':
            this.position = (pos[0]+1, pos[1])
        elif this.direction == 'L':
            this.position = (pos[0], pos[1]-1)
    
    def start(this):
        output = this.computer.run([this.getCurrentPanelColor()])
        
        while output is not None:
            this.paintPanel(output)
            output = this.computer.run()
            if output is None:
                break
            this.move(output)
            output = this.computer.run([this.getCurrentPanelColor()])
