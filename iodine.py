from havia.processor import Processor

program = [
    0x9a, 0xff, 0xff,
    0x00
]

processor = Processor(program, [0xea] * 256)

while (processor.pc != -1):
    print(processor.pc)
    processor.execute_instruction()
    if processor.pc != -1:
        processor.INC()


print("The Ram Results Caught by The Processor: -->")
print(processor.get_ram())
print("<-- :End of Ram Contents")