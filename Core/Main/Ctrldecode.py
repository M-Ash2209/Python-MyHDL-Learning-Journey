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
        # MemWrite.next, Branch.next, MemRead.next, RegWrite.next, MemToReg.next, Operand_b_Sel.next = [False for i in range(6)]
        MemWrite.next = intbv(0)[1:]
        Branch.next = intbv(0)[1:]
        MemRead.next = intbv(0)[1:]
        RegWrite.next = intbv(0)[1:]
        MemToReg.next = intbv(0)[1:]
        Operand_b_Sel.next = intbv(0)[1:]
        AluOp.next = intbv(0)[3:]
        Auimm.next = intbv(0)[1:]
        Uimm.next = intbv(0)[1:]
        jal.next = intbv(0)[1:]
        jalr.next = intbv(0)[1:]
        
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

# opCodes = [51,3,35,99,19,103,111,55,23]
# from Tdecode import Tdecode
# import random
# @block
# def itdTest():

#     R, L, S, B, I, Jr, J, Li,Ai = [Signal(bool(0)) for i in range(9)]
#     opCode = Signal(intbv(0, min=0, max=112))
#     MemWrite = Signal(bool(0))
#     Branch = Signal(bool(0))
#     MemRead = Signal(bool(0))
#     RegWrite = Signal(bool(0))
#     MemToReg = Signal(bool(0))
#     Operand_b_Sel = Signal(bool(0))
#     AluOp = Signal(intbv(0,min=0)[3:])
#     Auimm = Signal(bool(0))
#     Uimm = Signal(bool(0))
#     jal = Signal(bool(0))
#     jalr = Signal(bool(0))

#     itd_1 = Tdecode(opCode, R, L, S, B, I, Jr, J, Li,Ai)
#     cd = Cdecode(R, L, S, B, I, Jr, J, Li,Ai, MemWrite,
#                                     Branch,
#                                     MemRead,
#                                     RegWrite,
#                                     MemToReg,
#                                     Operand_b_Sel,
#                                     AluOp,
#                                     Auimm,
#                                     Uimm,
#                                     jal,
#                                     jalr )

#     @instance
#     def stimulus():
#         # fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:5} "
#         # print(fmt.format("OpCode","RType", "Load", "Store", "Branch", "IType", "Jalr","Jal", "Lui","AuiPC"))
#         # for i in range(10):
#         #     opCode.next = random.choice(opCodes)
#         #     yield delay(10)
#         #     print(fmt.format(str(int(opCode)), str(int(R)), str(int(L)), str(int(S)), str(int(B)), str(int(I)), str(int(Jr)), str(int(J)), str(int(Li)), str(int(Ai))))
#         fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:5} | {10:5} | {11:5}"
#         print(fmt.format("OpCode","MW", "Brn", "MR", "RW", "MTR", "OPB","Aluop", "Auipc", "uimm","jal","jalr"))
#         for i in opCodes:
#             opCode.next = i 
#             yield delay(10)
#             print(fmt.format(str(int(opCode)),str(int(MemWrite)),str(int(Branch)),str(int(MemRead)),str(int(RegWrite)),str(int(MemToReg)),str(int(Operand_b_Sel)),str(int(AluOp)),str(int(Auimm)),str(int(Uimm)),str(int(jal)),str(int(jalr))))
#         raise StopSimulation
    
#     return itd_1, cd, stimulus

# tb = itdTest()
# tb.run_sim()