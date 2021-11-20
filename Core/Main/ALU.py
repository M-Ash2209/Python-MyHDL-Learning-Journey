from myhdl import *
import random

@block
def ALU(ina,inb,out,brt,aluop):
    @always_comb
    def alu_run():
        b=bool(0)

        if aluop == 0:
            out.next = ina + inb
        elif aluop == 1:
            out.next = ina << inb[5:0]
        elif aluop == 2 or aluop == 3:
            out.next = ina < inb
        elif aluop == 4:
            out.next = ina ^ inb
        elif aluop == 5:
            out.next = ina >> inb[5:0]
        elif aluop == 6:
            out.next = ina | inb
        elif aluop == 7:
            out.next = ina & inb
        elif aluop == 8:
            out.next = ina - inb
        elif aluop == 13:
            out.next = ina >> inb[5:0]
        elif aluop == 16:
            out.next = ina == inb
            b = ina == inb
        elif aluop == 17:
            out.next = ina != inb
        elif aluop == 20 or aluop == 22:
            out.next = ina < inb
            b = ina < inb
        elif aluop == 21 or aluop == 23:
            out.next = ina >= inb
            b = ina >= inb
        
        if b == 1 and aluop[5:3] == 2:
            brt.next = 1
        else:
            brt.next = 0
                
    return alu_run

DW=(2**32)-1

@block 
def alutest ():
    # ina,inb,out,aluop = [Signal((intbv(0)[32:])) for i in range(4)]
    ina = Signal(intbv(0,-DW,DW))
    inb= Signal(intbv(0,-DW,DW))
    out= Signal(intbv(0,-DW,DW))
    aluop = Signal(intbv(0)[5:])
    brt = Signal(bool())
    alu = ALU(ina,inb,out,brt,aluop)
    alu.convert('Verilog')

    @instance
    def test():
        ina.next,inb.next,aluop.next = random.randrange(-DW, DW),random.randrange(-DW, DW),random.randrange(0, 24)
        
        yield delay(10)
        print (ina,inb,aluop,out,brt)
    return alu,test

inst = alutest()
inst.config_sim(trace=True)
inst.run_sim()