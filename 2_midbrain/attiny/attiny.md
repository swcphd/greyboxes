## AtTiny Compilation

- write C code
- get familiar with gcc, avr-gcc
- compile this to assembly
- assemble this into hex
- once you get a .hex, .elf., .out file (you can inspect this!)
- (to change .elf to .hex: `objcopy -O ihex input.elf output.hex` )
- avrdude with lots of flags to upload to your uC