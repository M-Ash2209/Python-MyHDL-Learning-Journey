from myhdl import *

from PCC import PCC
from IMEM import IMEM
from CU import ControlUnit
from RegF import RegFile
from Immgen import ImmGen
from AluCtrl import AluCtrl
from ALU import ALU
from DMEM import DataMemory



# def loadmemoryfromfile(pathToFile):
#     file = open(pathToFile, "r")
#     return [int("0x"+ inst,16) for inst in file.read().split("\n")]

@block
def Core(clk,reset_n):

    @always_seq(clk.posedge,reset=reset_n)
    def top():

        pc_in, pc_out, pc4_out = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(3)]
        pc = PCC(clk, pc_in, pc_out, pc4_out)

        # instructions = loadmemoryfromfile("/home/ash/inst.txt")
        insinstructionsst = [0x00300293,0xffd00293]
        inst_out = Signal(intbv(0, min=0 ,max=(2**32)-1))
        instr_memory = IMEM(pc_out, inst_out, instructions)

        MemWrite = Signal(bool(0))
        Branch = Signal(bool(0))
        MemRead = Signal(bool(0))
        RegWrite = Signal(bool(0))
        MemToReg = Signal(bool(0))
        Operand_b_Sel = Signal(bool(0))
        AluOp = Signal(intbv(0,min=0)[3:])
        Auimm = Signal(bool(0))
        Uimm = Signal(bool(0))
        jal = Signal(bool(0))
        jalr = Signal(bool(0))
        control = ControlUnit(inst_out[6:],MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Auimm,Uimm,jal,jalr)

        reg_write_data, reg_read_data1, reg_read_data2 = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(3)]
        reg_file = RegFile(clk, RegWrite,reg_write_data, inst_out[11,7], inst_out[19:15], inst_out[24:20], reg_read_data1, reg_read_data2)

        s_imm , sb_imm , uj_imm , u_imm,au_imm, i_imm = [Signal(intbv(0)[32:]) for i in range(6)]
        imm_gen = ImmGen(inst_out, pc_out,s_imm , sb_imm , uj_imm , u_imm, au_imm,i_imm)

        alu_ctrl_pin = Signal(intbv(0, min=0, max=(2**5)-1))
        AluCtrl(AluOp, inst_out[14:12], inst_out[30], alu_ctrl_pin)

        alu_a, alu_b = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(2)]
        alu_out = Signal(intbv(0, min=0, max=(2**32)-1))
        brnc_out = Signal(bool())
        alu = ALU(alu_a, alu_b, alu_out,brnc_out, alu_ctrl_pin)
       
        alu_a.next = reg_read_data1

        @always_comb
        def opb():
            if MemWrite == False and Operand_b_Sel == True:
                alu_b.next = i_imm
            elif MemWrite == True and Operand_b_Sel == True:
                alu_b.next = s_imm
            else:
                alu_b.next = reg_read_data2

        

        @always_comb
        def pc_next():
            
            if (Branch and brnc_out) == True  and jal== False and jalr== False:
                pc_in.next = sb_imm
            elif (Branch and brnc_out) == False  and jal== True and jalr== False:

                pc_in.next = uj_imm
            elif (Branch and brnc_out) == False  and jal== False and jalr== True: 
                pc_in.next = alu_out
            else:
                pc_in.next = pc4_out

        
        data_mem_out = Signal(intbv(0, min=0, max=(2**32)-1))
        d_mem = DataMemory(clk, alu_out[9:2], reg_read_data2, data_mem_out, MemWrite, MemRead)

        @always_comb
        def Wrbackk():
            if MemToReg == True  and Auimm== False and Uimm== False and (jalr or jal)== False:
                reg_write_data.next = data_mem_out
            elif MemToReg == False  and Auimm== False and Uimm== True and (jalr or jal)== False:
                reg_write_data.next = u_imm
            elif MemToReg == False  and Auimm== True and Uimm== False and (jalr or jal)== False:
                reg_write_data.next = au_imm
            elif MemToReg == False  and Auimm== False and Uimm== False and (jalr or jal)== True:
                reg_write_data.next = pc4_out
            else:
                reg_write_data.next = alu_out
        return Wrbackk,opb,pc_next,d_mem,alu,imm_gen,control,instr_memory,pc,reg_file
    return top

@block
def Simulate():
    clk = Signal(bool(0))
    # reset_n = Signal(bool(1))
    reset_n = ResetSignal(0, active=0, isasync=False)
    core = Core(clk, reset_n)
    # core.convert("Verilog")
    
    @instance
    def clockGen():
        c = 0
        while c <= 100:
            clk.next = not clk
            c+=1
            yield delay(10)

    @instance
    def stimulus():
        yield delay(10)
        reset_n.next = 1

    return stimulus, clockGen, core

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

tb = Simulate()
# tb.config_sim(trace=True)
tb.run_sim()