; Your second assembly program (for an AVR microcontroller)
; This code is for the Atmel Mega 328P (used in Arduinos)

; How to read input from digitial IO pins

; First, we include ALL useful definitions for our hardware (names of pins, ports, etc.)
.nolist
.include "..\tools\m328pdef.inc"
.list

; When the Reset button is pressed, the program counter is set to 0x0000, put an instruction there to jump to our code.
.ORG	0x0000					; The next instruction is written at 0x0000
RJMP	main					; Write the instruction to jump to "main" label

main:							; Sets 4 pins to "Output" mode and 4 pins to "Input" mode
	LDI		r16, 0xF0			; Load the immedate value 0xF0 (1111000) into register 16
	OUT		DDRB, r16			; Set Data Direction Register B (0x04)

loop:
	IN		r16, PINB			; Read input from PINB (only valid for 4 pins set to input)
	BST		r16, 3				; Check status of the third bit (pin 11)
	BRTS	flash				; If the T-flag is set, then jump to flash
	CBI		PORTB, 5			; Clear fifth bit (pin 13)
	RJMP	loop				; Jump to "loop" label (again)

flash:
	SBI PORTB, 5				; Set fifth bit (pin 13)
	RJMP loop					; Jump to "loop" label
	
; FIN