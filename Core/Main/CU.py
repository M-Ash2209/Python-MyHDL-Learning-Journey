from myhdl import *
from Tdecode import Tdecode
from Ctrldecode import Cdecode

@block 
def ControlUnit(opCode,
                MemWrite,
                Branch,
                MemRead,
                RegWrite,
                MemToReg,
                Operand_b_Sel,
                AluOp,
                Auimm,
                Uimm,
                jal,
                jalr
                ):

    R, L, S, B, I, Jr, J, Li,Ai = [Signal(bool(0)) for i in range(9)]
    td = Tdecode(opCode, R, L, S, B, I, Jr, J, Li,Ai)
    cd = Cdecode(R, L, S, B, I, Jr, J, Li,Ai, MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Auimm,Uimm,jal,jalr)

    return td,cd

# opCode = Signal(intbv(0)[7:])
# MemWrite = Signal(bool(0))
# Branch = Signal(bool(0))
# MemRead = Signal(bool(0))
# RegWrite = Signal(bool(0))
# MemToReg = Signal(bool(0))
# Operand_b_Sel = Signal(bool(0))
# AluOp = Signal(intbv(0,min=0)[3:])
# Auimm = Signal(bool(0))
# Uimm = Signal(bool(0))
# jal = Signal(bool(0))
# jalr = Signal(bool(0))

# control = ControlUnit(opCode,MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Auimm,Uimm,jal,jalr)
# control.convert('Verilog')

# TESTBENCH
opCodes = [51,3,35,99,19,103,111,55,23]
import random
@block
def testbench():
    opCode = Signal(intbv(0, min=0, max=112))
    MemWrite = Signal(bool(0))
    Branch = Signal(bool(0))
    MemRead = Signal(bool(0))
    RegWrite = Signal(bool(0))
    MemToReg = Signal(bool(0))
    Operand_b_Sel = Signal(bool(0))
    AluOp = Signal(intbv(0,min=0)[3:])
    Auimm = Signal(bool(0))
    Uimm = Signal(bool(0))
    jal = Signal(bool(0))
    jalr = Signal(bool(0))

    control = ControlUnit(opCode,MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Auimm,Uimm,jal,jalr)
    control.convert('Verilog')

    @instance
    def stimulus():
        fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:5} | {10:5} | {11:5}"
        print(fmt.format("OpCode","MW", "Brn", "MR", "RW", "MTR", "OPB","Aluop", "Auipc", "uimm","jal","jalr"))
        for i in opCodes:
            opCode.next = i 
            yield delay(10)
            print(fmt.format(str(int(opCode)),str(int(MemWrite)),str(int(Branch)),str(int(MemRead)),str(int(RegWrite)),str(int(MemToReg)),str(int(Operand_b_Sel)),str(int(AluOp)),str(int(Auimm)),str(int(Uimm)),str(int(jal)),str(int(jalr))))
        raise StopSimulation

    return control,stimulus

tb = testbench()
tb.run_sim()