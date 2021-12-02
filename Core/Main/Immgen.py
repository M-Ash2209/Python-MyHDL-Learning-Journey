from myhdl import *

@block
def ImmGen(inst,pc,s_imm,sb_imm,uj_imm,u_imm,i_imm):
    
    @always_comb
    def run():
        i_imm.next = concat(intbv(inst[31])[20:],inst[32:20])
        s_imm.next = concat(intbv(inst[31])[20:], inst[32:25], inst[12:7])
        u_imm.next = concat(inst[32:12], intbv(0)[11:])
        sb_imm.next = concat(intbv(inst[31])[19:], inst[31], inst[7], inst[31:25], inst[12:8], intbv(0)[1:]) + pc
        uj_imm.next = concat(intbv(inst[31])[12:], inst[20:12], inst[20], inst[31:21], intbv(0)[1:]) + pc
    
    return run

DW = (2**31)-1

inst = Signal(intbv(0, 0, DW)[32:])
pc = Signal(intbv(0, 0, DW))
s_imm = Signal(intbv(0, -DW, DW))
sb_imm = Signal(intbv(0, -DW, DW))
uj_imm = Signal(intbv(0, -DW, DW))
u_imm = Signal(intbv(0, -DW, DW))
i_imm = Signal(intbv(0, -DW, DW))
imm= ImmGen(inst,pc,s_imm,sb_imm,uj_imm,u_imm,i_imm)
imm.convert("Verilog")


# @block
# def Simulate():



#     inst = Signal(intbv(0, 0, DW)[32:])
#     pc = Signal(intbv(0, 0, DW))
#     s_imm = Signal(intbv(0, -DW, DW))
#     sb_imm = Signal(intbv(0, -DW, DW))
#     uj_imm = Signal(intbv(0, -DW, DW))
#     u_imm = Signal(intbv(0, -DW, DW))
#     i_imm = Signal(intbv(0, -DW, DW))
