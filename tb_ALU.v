module tb_ALU;

reg [32:0] ina;
reg [32:0] inb;
wire [32:0] out;
wire brt;
reg [4:0] aluop;

initial begin
    $from_myhdl(
        ina,
        inb,
        aluop
    );
    $to_myhdl(
        out,
        brt
    );
end

ALU dut(
    ina,
    inb,
    out,
    brt,
    aluop
);

endmodule
