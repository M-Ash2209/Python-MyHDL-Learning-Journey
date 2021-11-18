module tb_ALU;

reg [32:0] ina;
reg [32:0] inb;
wire [32:0] out;
reg brt;
reg [4:0] aluop;

initial begin
    $from_myhdl(
        ina,
        inb,
        brt,
        aluop
    );
    $to_myhdl(
        out
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
