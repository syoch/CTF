import asyncio
import subprocess
import urllib.request

# win-vm:30000
# EXE_SERVER = "100.115.215.47:30000"

# HOST = "100.124.120.123"  # win-vm
# HOST = "100.115.215.47"  # syoch-nix
# PORT = 31000


class DaemonProtocol:
    def __init__(self, exe_server: str) -> None:
        self.exe_server = exe_server

    def connection_made(self, transport: asyncio.DatagramTransport):
        self.transport = transport

    def datagram_received(self, data: bytes, addr: tuple[str, int]):
        opcode = data[0]
        print(f"Received opcode: {opcode} from {addr}")

        if opcode == 0x00:  # Execute peb-inspect
            url_path = data[1:].decode()
            self.transport.sendto(b"\x80", addr)  # Accept

            url = f"http://{self.exe_server}/{url_path}"
            print(f"Downloading {url} --> a.exe")
            urllib.request.urlretrieve(url, "a.exe")

            print("Executing a.exe")
            output = subprocess.check_output("a.exe")

            # sendto addr with 64byte chunked
            for i in range(0, len(output), 64):
                self.transport.sendto(b"\x88" + output[i : i + 64], addr)
            self.transport.sendto(b"\x81", addr)  # End-Program


async def server(listen_on: tuple[str, int], exe_server: str):
    loop = asyncio.get_running_loop()

    print(f"Listening on {listen_on[0]}:{listen_on[1]}")
    transport, _ = await loop.create_datagram_endpoint(
        lambda: DaemonProtocol(exe_server),  # type: ignore
        local_addr=listen_on,
    )

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()


async def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog="daemon",
    )
    parser.add_argument("-b", "--bind", default="0.0.0.0")
    parser.add_argument("-p", "--port", default=31000)
    parser.add_argument("-s", "--server")

    args = parser.parse_args()
    bind, port, exe_server = args.bind, args.port, args.server

    await server((bind, port), exe_server)


if __name__ == "__main__":
    asyncio.run(main())
