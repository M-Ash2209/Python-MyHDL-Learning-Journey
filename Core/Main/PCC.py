from myhdl import *

@block
def PCC(clk,inpp,pc,pc4):
    regg = Signal(intbv(0,min=0)[32:])

    @always_comb
    def read ():
        pc.next = regg
        pc4.next = regg+4

    @always(clk.posedge)
    def wrt ():
        regg.next = inpp
    return wrt,read

# clk = Signal(bool())
# inpp = Signal(intbv(0,min=0)[32:])
# pc = Signal(intbv(0,min=0)[32:])
# pc4 = Signal(intbv(0,min=0)[32:])
# pcc = PCC(clk,inpp,pc,pc4)
# pcc.convert("Verilog")
@block
def testing():
    
    clk = Signal(bool())
    inpp = Signal(intbv(0,min=0)[32:])
    pc = Signal(intbv(0,min=0)[32:])
    pc4 = Signal(intbv(0,min=0)[32:])
    pcc = PCC(clk,inpp,pc,pc4)
    pcc.convert("Verilog")

    @instance
    def run():
        for i in range(10):
            inpp.next = pc4
            yield clk.posedge
            print(f"{pc} {pc4}")
            # yield clk
        raise StopSimulation

    @always(delay(10))
    def clkgen():
        clk.next = not clk
    
    return pcc, run, clkgen

tb = testing()
tb.config_sim(trace=True)
tb.run_sim()

