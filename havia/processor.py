import time

class Processor:
    def __init__(self, program: list, ram: list):
        self.pc = 0
        self.program = program
        self.ram = ram
        self.cache = 0x00
        self.regA = 0x00
        self.regB = 0x00
        self.regC = 0x00
        self.instruction = None

    def get_ram(self):
        return self.ram
    
    def get_program(self):
        return self.program
    
    def get_program_counter(self):
        return self.pc

    def Fetch(self):
        self.instruction = self.program[self.pc]
    
    def INC(self):
        self.pc += 1
    
    def LDI(self, address, value):
        self.ram[address] = value
    
    def ADD(self, address1, address2, destination):
        self.ram[destination] = address1 + address2
    
    def SUB(self, address1, address2, destination):
        self.ram[destination] = address1 - address2
    
    def JMP(self, value):
        self.pc = value
    
    def JSR(self, value):
        self.cache = self.pc
        self.pc = value
    
    def RTS(self):
        self.pc = self.cache

    def HALT(self):
        self.pc = -1
    
    def LDA(self, value):
        self.regA = value
    
    def LDB(self, value):
        self.regB = value
    
    def LDC(self, value):
        self.regC = value
    
    def MUL(self, address1, address2, destination):
        self.ram[destination] = address1 * address2
    
    def DIV(self, address1, address2, destination):
        self.ram[destination] = address1 / address2
    
    def FLOORDIV(self, address1, address2, destination):
        self.ram[destination] = address1 // address2
    
    def INTERRUPT(self, delay: int):
        time.sleep(delay)
    
    def EA(self):
        return

    def execute_instruction(self):
        self.Fetch()
        
        if self.instruction > 0xff: #? Ram Size Error
            self.RamSizeError()
            self.HALT()
            return None


        if self.instruction == 0x9a: #? Load Directly Into Ram
            self.INC()
            self.Fetch()
            addr = self.instruction
            self.INC()
            self.Fetch()
            value = self.instruction()
            self.LDI(addr, value)


        elif self.instruction == 0x2d: #? Addition
            self.INC()
            self.Fetch()
            addr1 = self.instruction
            self.INC()
            self.Fetch()
            addr2 = self.instruction
            self.INC()
            self.Fetch()
            dest = self.instruction
            self.ADD(addr1, addr2, dest)
        
        elif self.instruction == 0x2e: #? Subtract
            self.INC()
            self.Fetch()
            addr1 = self.instruction
            self.INC()
            self.Fetch()
            addr2 = self.instruction
            self.INC()
            self.Fetch()
            dest = self.instruction
            self.SUB(addr1, addr2, dest)
        
        elif self.instruction == 0xea: #? No OP (0xea)
            self.EA()
        
        elif self.instruction == 0x21: #? JMP
            self.INC()
            self.Fetch()
            value = self.instruction
            self.JMP(value)
        
        elif self.instruction == 0x22: #? JSR
            self.INC()
            self.Fetch()
            value = self.instruction
            self.JSR(value)
        
        elif self.instruction == 0x23: #? RTS
            self.RTS()
        
        elif self.instruction == 0x2a: #? Multiply
            self.INC()
            self.Fetch()
            addr1 = self.instruction
            self.INC()
            self.Fetch()
            addr2 = self.instruction
            self.INC()
            self.Fetch()
            dest = self.instruction
            self.MUL(addr1, addr2, dest)
        
        elif self.instruction == 0x2b: #? Divide
            self.INC()
            self.Fetch()
            addr1 = self.instruction
            self.INC()
            self.Fetch()
            addr2 = self.instruction
            self.INC()
            self.Fetch()
            dest = self.instruction
            self.DIV(addr1, addr2, dest)
        
        elif self.instruction == 0x2c: #? Floor Divide (True Divide)
            self.INC()
            self.Fetch()
            addr1 = self.instruction
            self.INC()
            self.Fetch()
            addr2 = self.instruction
            self.INC()
            self.Fetch()
            dest = self.instruction
            self.FLOORDIV(addr1, addr2, dest)
        
        elif self.instruction == 0xee: #? Interrupt
            self.INC()
            self.Fetch()
            value = self.instruction
            self.INTERRUPT(value)
        
        elif self.instruction == 0xaa: #? LDA
            self.INC()
            self.Fetch()
            value = self.instruction
            self.LDA(value)
        
        elif self.instruction == 0xbb: #? LDB
            self.INC()
            self.Fetch()
            value = self.instruction
            self.LDB(value)
        
        elif self.instruction == 0xcc: #? LDC
            self.INC()
            self.Fetch()
            value = self.instruction
            self.LDC(value)
        return None