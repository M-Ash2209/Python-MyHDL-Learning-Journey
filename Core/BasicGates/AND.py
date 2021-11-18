from myhdl import *

@block
def AND(a,b,c):
    @always_comb
    def and_run():
        c.next = (a & b)
    return and_run
@block 
def gatetest ():
    a,b,c = [Signal(intbv(0)[32:]) for i in range(3)]
    andd = AND(a,b,c)

    @instance
    def test():
        a.next , b.next = 2,7
        yield delay(10)
        print (a,b,c)
    return andd,test

inst = gatetest()
inst.run_sim()
