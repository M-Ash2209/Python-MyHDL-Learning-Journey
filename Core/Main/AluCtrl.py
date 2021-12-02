from myhdl import *


@block
def AluCtrl(AluOp, Func3, Func730, AluCntrl):


    @always_comb
    def run():
        AluCntrl.next = 0

        if AluOp == 0:
            AluCntrl.next = concat(intbv(0, min=0, max=1),Func730, Func3)      # R/I


        elif AluOp == 1:
            AluCntrl.next = concat(intbv(2, min=0, max=(2**2)-1), Func3)     # SB
        

        elif AluOp  == 2 and AluOp  == 3:
            AluCntrl.next = intbv(0, min=0, max= (2**5)-1)                   # Load / Store 

    return run
        
# AluOp = Signal(intbv(0, min=0, max=3))
# Func3 = Signal(intbv(0, min=0, max=3))
# Func730 = Signal(bool(0))
# AluCntrl = Signal(intbv(0, min=0, max=(2**5)-1))

# aluctrl = AluCtrl(AluOp, Func3, Func730, AluCntrl)
# aluctrl.convert(hdl='Verilog')
@block
def actest():
    AluOp = Signal(intbv(0, min=0)[3:])
    Func3 = Signal(intbv(0, min=0)[3:])
    Func730 = Signal(bool(0))
    AluCntrl = Signal(intbv(0, min=0)[5:])

    aluctrl = AluCtrl(AluOp, Func3, Func730, AluCntrl)
    aluctrl.convert('Verilog')

    @instance
    def test():
        AluOp.next,Func3.next,Func730.next = 0, 0 ,0
        yield delay(10)
        print(bin(AluCntrl))

    return aluctrl, test


tb = actest()
# tb.config_sim(trace=True)
tb.run_sim()