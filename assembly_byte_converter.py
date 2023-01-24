import sys
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--name", help="name for file")

args = argParser.parse_args()

f = open(args.name+(".py"),"w")




f.write(
        """
import pwn

import sys

pwn.context.update(arch="x86-64")

#write assembly code here
asm = pwn.asm(
    '''

    mov rdi, 0x1337

    '''
    )
with pwn.process("/challenge/embryoasm") as process:
        process.write(asm)
        print(process.readallS())

        """

        )

f.close()