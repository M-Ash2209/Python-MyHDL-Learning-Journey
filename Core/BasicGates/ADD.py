from myhdl import *

@block
def ADD(a,b,c):
    @always_comb
    def add_run():
        c.next = a + b
    return add_run
@block 
def optest ():
    a,b,c = [Signal((intbv(0)[32:])) for i in range(3)]
    add = ADD(a,b,c)

    @instance
    def test():
        a.next , b.next = 4,166
        yield delay(10)
        print (a,b,c)
    return add,test

inst = optest()
inst.run_sim()