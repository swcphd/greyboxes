# Arduino Assembly Language

Detailed explanation and examples of how to program the Arduino UNO's microcontroller (Atmega328P) using AVR assembly language.

## Getting Started

Go through the tutorial.

### Prerequisites

You need an Arduino UNO (or micro/nano...any Arduino with the Atmega328P microcontroller) connected to a PC running windows via a USB cable.
This repository includes the main tools required: the AVR assembler (avr2asm.exe) and code upload utility (avrdude.exe) in the "Tools" sub-folder.
If you want to download these tools, then you can find them here:
[Atmel Studio] (http://www.microchip.com/development-tools/atmel-studio-7)
They will be installed here: C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain

You also need a text editor. We recommend Notepad++.


### Using example code

Assemble a *.asm file:
Go to the "Tools" folder. Open a window command prompt at this location. 
```
avrasm2.exe -fI *.asm
```
This will create a binary file (*.hex). If you do not include the -fI flag (which specifies intel hex file formats), then you will get a *.obj file.

Upload the binary file to the Atmega via USB.
```
avrdude -v -p atmega328p -c arduino -P com3 -b 115200 -D -U flash:w:*.hex:i
```


## Authors

* **Adam Kampff** - [kampff](https://github.com/kampff)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

