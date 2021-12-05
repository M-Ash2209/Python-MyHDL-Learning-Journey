from myhdl import *
import random

@block
def Tdecode(opCode, RType, Load, Store, Branch, IType, Jalr, Jal, Lui,Aui):

    @always_comb
    def run():

        RType.next = intbv(0)[1:]
        Load.next = intbv(0)[1:]
        Store.next = intbv(0)[1:]
        Branch.next = intbv(0)[1:]
        IType.next = intbv(0)[1:]
        Jalr.next = intbv(0)[1:]
        Jal.next = intbv(0)[1:]
        Lui.next = intbv(0)[1:]
        Aui.next = intbv(0)[1:]
        
        if opCode == 51:
            RType.next = 1
        elif opCode == 3:
            Load.next = 1
        elif opCode == 35:
            Store.next = 1
        elif opCode == 99:
            Branch.next = 1
        elif opCode == 19:
            IType.next = 1
        elif opCode == 103:
            Jalr.next = 1
        elif opCode == 111:
            Jal.next = 1
        elif opCode == 55:
            Lui.next = 1
        elif opCode == 23:
            Aui.next = 1
        
    return run

opCodes = [51,3,35,99,19,103,111,55,23]
R, L, S, B, I, Jr, J, Li,Ai = [Signal(bool(0)) for i in range(9)]
opCode = Signal(intbv(0, min=0, max=112))

td = Tdecode(opCode,R, L, S, B, I, Jr, J, Li,Ai)
td.convert('Verilog')

# @block
# def Tdtest():

#     R, L, S, B, I, Jr, J, Li,Ai = [Signal(bool(0)) for i in range(9)]
#     opCode = Signal(intbv(0, min=0, max=112))

#     td = Tdecode(opCode,R, L, S, B, I, Jr, J, Li,Ai)
#     td.convert('Verilog')
#     @instance
#     def test():
#         fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:5} "
#         print(fmt.format("OpCode","RType", "Load", "Store", "Branch", "IType", "Jalr","Jal", "Lui","AuiPC"))
#         for i in range(10):
#             opCode.next = random.choice(opCodes)
#             yield delay(10)
#             print(fmt.format(str(int(opCode)), str(int(R)), str(int(L)), str(int(S)), str(int(B)), str(int(I)), str(int(Jr)), str(int(J)), str(int(Li)), str(int(Ai))))
#         # raise StopSimulation
    
#     return td, test

# tb = Tdtest()
# tb.run_sim()