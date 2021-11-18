from myhdl import *

@block
def NAND(a,b,c):
    @always_comb
    def nand_run():
        c.next = not(a & b)
    return nand_run
@block 
def gatetest ():
    a,b,c = [Signal(intbv(0)[32:]) for i in range(3)]
    nand = NAND(a,b,c)

    @instance
    def test():
        a.next , b.next = 4,3
        yield delay(10)
        print (a,b,c)
    return nand,test

inst = gatetest()
inst.run_sim()