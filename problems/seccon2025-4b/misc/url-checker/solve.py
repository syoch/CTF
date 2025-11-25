from pwn import *

# p: tube = process("docker run -i s4b25-petname:latest /home/pwn/chall", shell=True)
p: tube = remote("url-checker.challenges.beginners.seccon.jp", 33457)

p.sendline(b"https://example.coma")
p.interactive()
