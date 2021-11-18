from myhdl import *

@block
def OR(a,b,c):
    @always_comb
    def or_run():
        c.next = (a | b)
    return or_run
@block 
def gatetest ():
    a,b,c = [Signal((intbv(0)[3:])) for i in range(3)]
    orr = OR(a,b,c)

    @instance
    def test():
        a.next , b.next = 2,5
        yield delay(10)
        print (a,b,c)
    return orr,test

inst = gatetest()
inst.run_sim()
