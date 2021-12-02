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

opCode = Signal(intbv(0)[32:])
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

# TESTBENCH
# opCodes = [51,3,35,99,19,103,111,55]
# import random
# @block
# def testbench():
#     opCode = Signal(intbv(0, min=0, max=112))
#     bool_signals = [Signal(bool(0)) for i in range(6)]
#     int_signals = [Signal(intbv(0)) for i in range(4)]
#     cu = ControlUnit(opCode, *bool_signals, *int_signals)

#     @instance
#     def stimulus():
#         for i in opCodes: