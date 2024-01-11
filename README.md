# Iodine Processor Havia v1
### This is a processor project where I attempt to emulate how a processor works.


# Instructions
The instruction's for how the processor uses the values of hex from 0x00 to 0xff are listed in the `instruction.md` file where they can be viewed by clicking on the hex value of the operation you are looking for, or by scrolling down to see which it is. the values listed are most likely not based on any known processor configurations for the functions.

Here is some example code:
```
( HEX PROMPT )
0xea
0x9a 0x01 0x01
0x9a 0x02 0x01
0x2d 0x01 0x02 0x01
0x21 0x01
0x00

( INTO PYTHON PROGRAM )
program = [
  0xea,
  0x9a, 0x01, 0x01,
  0x9a, 0x02, 0x01,
  0x2d, 0x01, 0x02, 0x01,
  0x21, 0x01,
  0x00,
]

The Code ^^^ will continue on until it hits 255 where it will then error out as the processor will have gone above its allowed hex integer value.
```

## Future Updates
### The plan for the future
I will attempt by best to add more and more functionality to this processor and at somepoint add a display and keyboard input, tho currently I want to implement a better error detection system that would allow the processor to just write to the next address in memory and keep going until it runs out of memory, and I also want to add external file support which would allow others to write code for the processor to read from without needing to write in hex (yes an assembly language. called voidscript (vs)).
