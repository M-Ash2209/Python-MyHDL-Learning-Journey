from myhdl import *

@block
def Cdecode(
                    RType,
                    Load,
                    Store,
                    SBType,
                    IType,
                    Jalr,
                    Jal,
                    Lui,
                    Aui,
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

    @always_comb
    def run():

        if RType == 1:
            RegWrite.next = 1
        elif Load == 1:

            MemRead.next = 1
            RegWrite.next = 1
            MemToReg.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(3,0)   

        elif Store == 1:

            MemWrite.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(2,0) 
        elif SBType == 1:
            Branch.next = 1
            AluOp.next = intbv(1,0) 
        elif IType == 1:

            RegWrite.next = 1
            Operand_b_Sel.next = 1
        elif Jalr == 1:
            RegWrite.next = 1
            jalr.next = 1
            Operand_b_Sel.next = 1
           
        elif Jal == 1:

            RegWrite.next = 1
            jal.next = 1
            
        elif Lui == 1:

            RegWrite.next = 1
            Uimm.next = 1
            
        elif Aui == 1:

            RegWrite.next = 1
            Auimm.next = 1
            

    return run

RType = Signal(bool(0))
Load = Signal(bool(0))
Store = Signal(bool(0))
SBType = Signal(bool(0))
IType = Signal(bool(0))
Jalr = Signal(bool(0))
Jal = Signal(bool(0))
Lui = Signal(bool(0))
Aui = Signal(bool(0))
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

CD_inst = Cdecode(
                                    RType,
                                    Load,
                                    Store,
                                    SBType,
                                    IType,
                                    Jalr,
                                    Jal,
                                    Lui,
                                    Aui,
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
                                )
CD_inst.convert(hdl='Verilog')

opCodes = [51,3,35,99,19,103,111,55,23]
# from Tdecode import Tdecode
# import random
# @block
# def itdTest():

#     R, L, S, B, I, Jr, J, Li,Ai = [Signal(bool(0)) for i in range(9)]
#     opCode = Signal(intbv(0, min=0, max=112))
#     bool_signals = [Signal(bool(0)) for i in range(6)]
#     int_signals = [Signal(intbv(0)) for i in range(4)]

#     itd_1 = Tdecode(opCode, R, L, S, B, I, Jr, J, Li,Ai)
#     cd = Cdecode(R, L, S, B, I, Jr, J, Li,Ai, *bool_signals, *int_signals )

#     @instance
#     def stimulus():
#         # fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:100} |"
#         print("OpCode","RType", "Load", "Store", "Branch", "IType", "Jalr","Jal", "Lui", "oo")
#         for i in opCodes:
#             opCode.next = i #random.choice(opCodes)
#             yield delay(10)
#             print(str(int(opCode)) ,[[str(b) for b in bool_signals],[str(i) for i in int_signals]] )
#         raise StopSimulation
    
#     return itd_1, cd, stimulus

# tb = itdTest()
# tb.run_sim()