
class IntcodeComputer: #{
    def __init__(this, program):
        this.program = [int(s) for s in program.split(',')]
        this.reset()

    def reset(this):
        this.memory = this.program.copy()
        this.pointer = 0
        this.relativeBase = 0
        this.inputIndex = 0
    
    def getDataFromAddress(this, address):
        if address >= len(this.memory):
            return 0
        return this.memory[address]
    
    def getData(this, address, accessMode):
        if accessMode == 0: #position mode
            return this.getDataFromAddress(this.memory[address])
        elif accessMode == 1: #immediate mode
            return this.getDataFromAddress(address)
        elif accessMode == 2: #relative mode
            return this.getDataFromAddress(this.memory[address] + this.relativeBase)
            
        print("getData() error - invalid accessMode code: '" + accessMode + "'")
        return "error"
        
    def setDataToAddress(this, address, value):
        if address >= len(this.memory):
            this.memory.extend([0] * (address - len(this.memory) + 1))
        this.memory[address] = value
        
    def setData(this, address, value, accessMode):
        if accessMode == 0: #position mode
            this.setDataToAddress(this.memory[address], value)
            return True
        elif accessMode == 2: #relative mode
            this.setDataToAddress(this.memory[address] + this.relativeBase, value)
            return True
            
        print("setData() error - invalid accessMode code: '" + accessMode + "'")
        return False
        
    def perform_sum(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        value = this.getData(address+1, parameterAccessModes[0]) + this.getData(address+2, parameterAccessModes[1])
        this.setData(address+3, value, parameterAccessModes[2])
        this.pointer += 4
        
    def perform_multiply(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        value = this.getData(address+1, parameterAccessModes[0]) * this.getData(address+2, parameterAccessModes[1])
        this.setData(address+3, value, parameterAccessModes[2])
        this.pointer += 4
    
    def perform_input(this, providedInputs, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        
        if this.inputIndex >= len(providedInputs):
            inputValue = int(input("input[" + str(this.inputIndex) + "]> "))
        else:
            inputValue = providedInputs[this.inputIndex]
        this.inputIndex += 1
        
        this.setData(address+1, inputValue, parameterAccessModes[0])
        this.pointer += 2
    
    def perform_output(this, parameterAccessModes):
        output = this.getData(this.pointer+1, parameterAccessModes[0])
        this.pointer += 2
        return output
        
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
        this.setData(address+3, 1 if a < b else 0, parameterAccessModes[2])
        this.pointer += 4
    
    def perform_equals(this, parameterAccessModes):
        address = this.pointer
        memory = this.memory
        a = this.getData(address+1, parameterAccessModes[0])
        b = this.getData(address+2, parameterAccessModes[1])
        this.setData(address+3, 1 if a == b else 0, parameterAccessModes[2])
        this.pointer += 4
    
    def perform_relativeBaseOffset(this, parameterAccessModes):
        address = this.pointer
        offset = this.getData(address+1, parameterAccessModes[0])
        this.relativeBase += offset
        this.pointer += 2
    
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
    
    def run(this, inputs = []): #{
        opcode, parameterAccessModes = this.parseInstruction()
        this.inputIndex = 0
        while opcode != 99: #{
            #print('>', this.pointer, this.getData(this.pointer, 1))
            if opcode == 1:
                this.perform_sum(parameterAccessModes)
            elif opcode == 2:
                this.perform_multiply(parameterAccessModes)
            elif opcode == 3:
                this.perform_input(inputs, parameterAccessModes)
            elif opcode == 4:
                return this.perform_output(parameterAccessModes)
            elif opcode == 5:
                this.perform_jumpIfTrue(parameterAccessModes)
            elif opcode == 6:
                this.perform_jumpIfFalse(parameterAccessModes)
            elif opcode == 7:
                this.perform_lessThan(parameterAccessModes)
            elif opcode == 8:
                this.perform_equals(parameterAccessModes)
            elif opcode == 9:
                this.perform_relativeBaseOffset(parameterAccessModes)
            else:
                print("run() error - invalid opcode: '" + str(opcode) + "'")
                input()
                return "error"
            opcode, parameterAccessModes = this.parseInstruction()
        #}
        return None
    #}
#}