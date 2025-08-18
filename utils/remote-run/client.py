import socket

HOST = "100.124.120.123"  # win-vm
# HOST = "100.115.215.47"  # syoch-nix
PORT = 31000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"\x00utils/peb-inspect/build/peb-inspect.exe", (HOST, PORT))
        reply, a = s.recvfrom(1)
        print(f"Reply: {reply} from {a}")

        while True:
            msg, _ = s.recvfrom(1024)
            op = msg[0]

            if op == 0x88:
                for b in msg[1:]:
                    if 32 <= b <= 126 or b == 10:
                        print(chr(b), end="")
                    elif b == 0x0D:
                        pass
                    else:
                        print("\\x{:02X}".format(b), end="")
            elif op == 0x81:  # End
                print("")
                break


main()
