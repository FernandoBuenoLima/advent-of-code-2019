#return types
DEFAULT = 0
INPUT_UPDATE = 1
GAME_OVER = 2

class Arcade:
    def __init__(this, computer, gridSize):
        this.computer = computer
        this.height = gridSize[0]
        this.width = gridSize[1]
        this.grid = [[0 for i in range(this.height)] for j in range(this.width)]
        this.score = 0
    
    def updateGrid(this, command):
        if command[0] == -1 and command[1] == 0:
            if command[2] == 0:
                print("Final score:", this.score)
            this.score = command[2]
        else:
            this.grid[command[0]][command[1]] = command[2]
    
    def start(this):
        output = this.computer.run()
        while output != []:
            this.updateGrid(output)
            output = this.computer.run()
    
    def run(this, joystick = []):
        output = this.computer.run(joystick)
        if output == None:
            return GAME_OVER
        elif len(output) == 0:
            return INPUT_UPDATE
        else:
            this.updateGrid(output)
            return DEFAULT
