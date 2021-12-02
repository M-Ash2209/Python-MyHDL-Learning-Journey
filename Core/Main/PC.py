from myhdl import *

DW = 32

@block
def PC(clock, input, pc, pc4):

    reg = Signal(modbv(0,0,2**DW))
    @always_comb
    def read():
        pc.next = reg
        pc4.next = reg + 4
    
    @always(clock.posedge)
    def write():
        reg.next = input

    return read, write

@block
def PCtest():
    pc_input, pc, pc4 = [Signal(intbv(0,0,2**DW)) for i in range(3)]
    clk = Signal(bool(0))
    pCounter = PC(clk, pc_input, pc, pc4)
    pCounter.convert("Verilog")
    @instance
    def run():
        for i in range(0,10):
            pc_input.next = i
            yield clk.posedge
            print(f"{pc} {pc4}")
            # yield clk
            
        raise StopSimulation

    @always(delay(10))
    def clkgen():
        clk.next = not clk
    
    return pCounter, run, clkgen

tb = PCtest()
# tb.config_sim(trace=True)
tb.run_sim()