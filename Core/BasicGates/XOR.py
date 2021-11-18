from myhdl import *

@block
def XOR(a,b,c):
    @always_comb
    def xor_run():
        c.next = (a ^ b)
    return xor_run
@block 
def gatetest ():
    a,b,c = [Signal((intbv(0)[3:])) for i in range(3)]
    xor = XOR(a,b,c)

    @instance
    def test():
        a.next , b.next = 2,5
        yield delay(10)
        print (a,b,c)
    return xor,test

inst = gatetest()
inst.run_sim()
