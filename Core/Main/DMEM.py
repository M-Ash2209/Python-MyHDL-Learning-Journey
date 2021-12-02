from myhdl import *

ROWS = 1024
DW = (2**32)-1

@block
def DataMemory(clk, addr, data_in, data_out, we, rd):

    mem = [Signal(intbv(0, -DW, DW)) for i in range(ROWS)]

    @always_comb
    def read():
        if rd:
            data_out.next = mem[int(addr)]  
        

    @always(clk.posedge)
    def write():
        if we:
            mem[addr].next = data_in

    return read, write

# def toGenerateVerilog():
#     clk = Signal(bool(0))mm,
                # jal,
                # jalr
                # )
#     addr = Signal(intbv(0)[10:])
#     data_in = Signal(intbv(0, -DW, DW))
#     data_out = Signal(intbv(0, -DW, DW))
#     we = Signal(bool(0))
#     rd = Signal(bool(0))
#     # mem_data = Signal(intbv(0)[32:])

#     dmem = DataMemory(clk, addr, data_in, data_out, we, rd)

#     dmem.convert('Verilog')

# toGenerateVerilog()