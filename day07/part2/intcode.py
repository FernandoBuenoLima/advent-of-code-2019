
class IntcodeComputer: #{
    def __init__(this, program):
        this.program = program.copy()
        this.reset()
        this.pointer = 0

    def reset(this):
        this.memory = this.program.copy()
        
    def getData(this, address, accessMode):
        if accessMode == 0: #position mode
            return this.memory[this.memory[address]]
        elif accessMode == 1: #immediate mode
            return this.memory[address]
        print("getData() error - unrecognized accessMode: '" + accessMode + "'")
        return "error"
        
    def perform_sum(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        memory[memory[address+3]] = this.getData(address+1, parameterAccessModes[0]) + this.getData(address+2, parameterAccessModes[1])
        this.pointer += 4
        
    def perform_multiply(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        memory[memory[address+3]] = this.getData(address+1, parameterAccessModes[0]) * this.getData(address+2, parameterAccessModes[1])
        this.pointer += 4
        
    def perform_jumpIfTrue(this, parameterAccessModes):
        address = this.pointer
        if this.getData(address+1, parameterAccessModes[0]) != 0:
            this.pointer = this.getData(address+2, parameterAccessModes[1])
        else:
            this.pointer += 3
    
    def perform_jumpIfFalse(this, parameterAccessModes):
        address = this.pointer
        if this.getData(address+1, parameterAccessModes[0]) == 0:
            this.pointer = this.getData(address+2, parameterAccessModes[1])
        else:
            this.pointer += 3
    
    def perform_lessThan(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        a = this.getData(address+1, parameterAccessModes[0])
        b = this.getData(address+2, parameterAccessModes[1])
        memory[memory[address+3]] = 1 if a < b else 0
        this.pointer += 4
    
    def perform_equals(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        a = this.getData(address+1, parameterAccessModes[0])
        b = this.getData(address+2, parameterAccessModes[1])
        memory[memory[address+3]] = 1 if a == b else 0
        this.pointer += 4
    
    def perform_input(this, providedInput):
        memory = this.memory
        memory[memory[this.pointer+1]] = providedInput
        this.pointer += 2
    
    def perform_output(this, parameterAccessModes):
        output = this.getData(this.pointer+1, parameterAccessModes[0])
        this.pointer += 2
        return output
    
    def parseInstruction(this):
        instruction = str(this.getData(this.pointer, 1))
        
        if len(instruction) == 1:
            return int(instruction), [0, 0, 0]
            
        opcode = int(instruction[-2:])
        parameterAccessModes = [0, 0, 0]
        parameterPosition = 0
        
        for i in range(len(instruction) - 3, -1, -1):
            parameterAccessModes[parameterPosition] = int(instruction[i])
            parameterPosition += 1
        
        return opcode, parameterAccessModes
    
    def run(this, inputs): #{
        opcode, parameterAccessModes = this.parseInstruction()
        nextInputIndex = 0
        
        while opcode != 99: #{
            if opcode == 1:
                this.perform_sum(parameterAccessModes)
            elif opcode == 2:
                this.perform_multiply(parameterAccessModes)
            elif opcode == 5:
                this.perform_jumpIfTrue(parameterAccessModes)
            elif opcode == 6:
                this.perform_jumpIfFalse(parameterAccessModes)
            elif opcode == 7:
                this.perform_lessThan(parameterAccessModes)
            elif opcode == 8:
                this.perform_equals(parameterAccessModes)
            elif opcode == 3:
                this.perform_input(inputs[nextInputIndex])
                nextInputIndex += 1
            elif opcode == 4:
                return this.perform_output(parameterAccessModes)
            else:
                print("run() error - unrecognized opcode: '" + str(opcode) + "'")
                input()
                return "error"
            opcode, parameterAccessModes = this.parseInstruction()
        #}
        return None
    #}
#}