from myhdl import *

DW = 32
AW = DW/4

@block
def InstructionMemory(addr, inst_out, INSTRUCTIONS):
    
    @always_comb
    def read():
        inst_out.next = INSTRUCTIONS[int(addr)]
    return read

# def loadmemoryfromfile(pathToFile):
#     file = open(pathToFile, "r")
#     return tuple([int("0x"+inst, 16) for inst in open(pathToFile, "r").read().split("\n")])