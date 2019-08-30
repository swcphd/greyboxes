# Digital Logic

Created: Jul 24, 2019 4:56 PM

# (Very Basic) Intro to Digital Logic

Today we're working towards the engine of a processor This is working towards an ALU — there is much more to a CPU!

[Photo of CPU architecture]

What is "digital"?

Why do we need logic?

How do we implement logic in circuits?

What can we make with hardware logic?

- any instruction set can be represented as binary
- boolean algebra applied to such instructions / data can generate arbitrary computations with enough time and memory (see later discussions of interpretation/compilation)

Choices are made by people:

[https://en.wikipedia.org/wiki/Von_Neumann_architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)

[https://en.wikipedia.org/wiki/Universal_Turing_machine](https://en.wikipedia.org/wiki/Universal_Turing_machine)

- Make an OR and AND gate
    - Explain how to get to XOR, NAND, etc
- Make a full adder out of XOR ICs
- Hook full adders together to get multiple bit adder?
- Explain negative numbers, subtraction, bit-shifting
- Link to reference of how to implement every single basic gate with NAND
-

Many ways to make XOR gate:

- [https://hackaday.io/project/8449-hackaday-ttlers/log/150147-bipolar-xor-gate-with-only-2-transistors/](https://hackaday.io/project/8449-hackaday-ttlers/log/150147-bipolar-xor-gate-with-only-2-transistors/)

IMPORTANT: make sure to pull up/down unused gates otherwise nondeterministic behavior may ensue.

NOTE: with BJTs you might see different currents on the outputs because the currents will add as you saturate transistors. Thus LEDs will glow differently depending on the circuit's state.

OR Gate

![](images/Untitled-1425ddf3-2a5f-4d93-819d-d496101f1a87.png)

AND Gate

Great example: [http://www.technologystudent.com/elec1/dig8.htm](http://www.technologystudent.com/elec1/dig8.htm)

![](images/Untitled-c9b50a7b-b105-4d02-9076-e82a15cc6148.png)

XOR Gate (using diode bridge + PNP)

I wasn't able to get this circuit working, but I didn't try very hard! PNPs flip my brain inside out... I think the issue was getting the incoming logic level to be reversed.

![](images/Untitled-825442e4-7951-450f-8e10-9dec8556a108.png)

![](images/Untitled-c64085f7-0edc-4b42-a1cc-5abe9fa621b3.png)

Gate Abstractions

![](images/Untitled-6c814281-f78d-4b8c-b474-133df32c7a46.png)

Half Adder

Parts

(XOR)[[https://www.ti.com/lit/ds/symlink/cd4030b-mil.pdf](https://www.ti.com/lit/ds/symlink/cd4030b-mil.pdf)]

(AND)[[https://www.ti.com/lit/ds/symlink/cd4081b.pdf](https://www.ti.com/lit/ds/symlink/cd4081b.pdf)]

(OR)[[http://www.ti.com/lit/ds/symlink/cd4071b.pdf](http://www.ti.com/lit/ds/symlink/cd4071b.pdf)]

Tutorial — can you spot the error?

[http://www.learningaboutelectronics.com/Articles/Half-adder-circuit.php](http://www.learningaboutelectronics.com/Articles/Half-adder-circuit.php)

![](images/Untitled-15dc1d1c-ae8d-4f1f-9de6-8ace11ec0102.png)

Full Adder

![](images/Untitled-ffdf0f39-5a96-4e09-82a3-97ac97632af7.png)

2-bit adder (without carry in)

![](images/Untitled-1f3de71c-9511-423e-8d3f-6279cdc74fb9.png)

3 bit adder

![](images/Untitled-0a55f581-5781-4604-a3c6-368bfc1b6b0b.png)

![](images/Untitled-3702979f-fc4e-4943-930a-c7a3d33d4887.png)

![](images/Untitled-fd2ff237-b9e8-4360-bd6f-e16c7945d05a.png)