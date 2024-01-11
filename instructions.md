## All OpCodes
- [0x00](#halt)
- [0x21](#jmp)
- [0x22](#jsr)
- [0x23](#rts)
- [0x2A](#mul)
- [0x2B](#div)
- [0x2C](#floordiv)
- [0x2D](#add)
- [0x2E](#sub)
- [0x9A](#ldi)
- [0xAA](#lda)
- [0xBB](#ldb)
- [0xCC](#ldc)
- [0xEA](#ea)
- [0xEE](#interrupt)



## Program Functions
#### HALT
##### 0x00
Halts the processor

#### LDA
##### 0xAA
Loads a value into register A

#### LDB
##### 0xBB
Loads a value into register B

#### LDC
##### 0xCC
Loads a value into register C

#### MUL
##### 0x2A
The Multiply Function allows the processor to multiply two addresses together.

#### DIV
##### 0x2B
The Divide Function allows the processor to divide two addresses together.

#### FLOORDIV
##### 0x2C
This Function allows the processor to only divide into whole numbers.

#### INTERRUPT
##### 0xEE
This function halts the processor for a specified amount of time.

#### EA
##### 0xEA
This function is just an ignore operation.

#### RTS
##### 0x23
This operation can be used after a `JSR` operation to return to when that function was called.

#### JSR
##### 0x22
This operation is like a `JMP` but it stores the address of where it jumped from.

#### JMP
##### 0x21
Changes the program counter to the location listed on the function.

#### ADD
##### 0x2D
This function adds two addresses together then places the result in another address.

#### SUB
##### 0x2E
This function subtracts two addresses together then places the result in another address.

#### LDI
##### 0x9A
This function allows a value to be placed into a specified address in ram.

#### INC
##### None
This function increments the program counter by 1.

#### Fetch
##### None
This function gets the next instruction from rom at the location of the program counter.



## Outside program functions
#### get_ram
Gets the whole current contents of ram.

#### get_program
Retrieves the current written program if needed.

#### get_program_counter
Retrieves the current position of the program counter.
