module tb_SysTop;

wire txd_line;
reg rxd_line;
wire txd_line2;
reg rxd_line2;
wire [7:0] leds;
reg reset;
reg clock;

initial begin
    $from_myhdl(
        rxd_line,
        rxd_line2,
        reset,
        clock
    );
    $to_myhdl(
        txd_line,
        txd_line2,
        leds
    );
end

SysTop dut(
    txd_line,
    rxd_line,
    txd_line2,
    rxd_line2,
    leds,
    reset,
    clock
);

endmodule
