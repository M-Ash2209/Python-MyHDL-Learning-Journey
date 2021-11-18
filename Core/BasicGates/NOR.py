from myhdl import *

@block
def NOR(a,b,c):
    @always_comb
    def nor_run():
        c.next = not(a | b)
    return nor_run
@block 
def gatetest ():
    a,b,c = [Signal(intbv(0)[32:]) for i in range(3)]
    nor = NOR(a,b,c)

    @instance
    def test():
        a.next , b.next = 4,5
        yield delay(10)
        print (a,b,c)
    return nor,test

inst = gatetest()
inst.run_sim()