from myhdl import *

@block
def NOT(a,b):
    @always_comb
    def not_run():
        if not(a) == True:
             b.next= ~a
        else:
            b.next= ~a
    return not_run
@block 
def gatetest ():
    a,b = [Signal(intbv(0)[32:]) for i in range(2)]
    nott = NOT(a,b)

    @instance
    def test():
        a.next = 6
        yield delay(10)
        print (a,b)
    return nott,test

inst = gatetest()
inst.run_sim()