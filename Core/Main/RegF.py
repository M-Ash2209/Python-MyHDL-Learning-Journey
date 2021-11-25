from myhdl import * 

no_of_reg = 32
DW=(2**no_of_reg)-1
Regi= list(intbv(0,-DW,DW) for i in range(no_of_reg))

@block
def RegFile(we,rs1,rs2,rd,WriteBack,Data_A, Data_B):

    @always_comb
    def read():
        Data_A.next = Regi[int(rs1)]
        Data_B.next = Regi[int(rs2)]
    @always_comb
    def write():
        if we and int(rd) != 0 :
            Regi[int(rd)]= WriteBack
    
    return read, write
@block
def Regtest():
    rs_A = Signal(int(0))
    rs_B = Signal(int(0))
    Rd = Signal(int(0))
    WriteBack = Signal(intbv(0,-DW,DW))
    writeEnable = Signal(bool(0))
    Data_A = Signal(intbv(0,-DW,DW))
    Data_B = Signal(intbv(0,-DW,DW))
    regg = RegFile(writeEnable,rs_A,rs_B,Rd,WriteBack,Data_A,Data_B)
    # regg.convert('Verilog')
    @instance
    def test():
        for i in range(2):
            writeEnable.next,rs_A.next,rs_B.next,Rd.next,WriteBack.next = 1,3,4,3,5
            yield delay(10)
            print("rs_a : ",rs_A)
            print("rs_b : ",rs_B)
            print("rd : ",Rd)
            print("writeback : ",WriteBack)
            print("writeEnable : ",writeEnable)
            print("data A : ",Data_A)
            print("data B : ",Data_B)
            print("-------------------------------------")
    return regg, test


tb = Regtest()
tb.config_sim(trace=True)
tb.run_sim()


# from myhdl import *

# ROWS = 32
# DW = 2**(ROWS-1)

# @block
# def RegisterFile(
#                 clock,
#                 regWrite,
#                 wd,
#                 ws,
#                 rs1,
#                 rs2,
#                 rd1,
#                 rd2
#                 ):

#     register = [Signal(intbv(0, -DW, DW)) for i in range(ROWS)]
#     # register[0] = Signal(intbv(0, -DW, DW))
    
#     @always_comb
#     def read():
#         rd1.next = register[int(rs1)]
#         rd2.next = register[int(rs2)]

#     @always(clock.posedge)
#     def write():
#         if regWrite & int(ws) != 0:
#             register[int(ws)].next = wd


#     return read, write
