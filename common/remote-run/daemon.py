import asyncio
import subprocess
import urllib.request

from .protocol import Protocol
from .packets import ExecutionRequest, Packet, ProgramLog, StartedExecution


class DaemonUDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, exe_server: str) -> None:
        super().__init__()
        self.exe_server = exe_server
        self.proto = Protocol.default_protocol()

    def send_packet(self, packet: Packet, addr: tuple[str, int]):
        data = self.proto.pack_packet(packet)
        self.transport.sendto(data, addr)

    def connection_made(self, transport: asyncio.DatagramTransport):
        self.transport = transport

    def datagram_received(self, data: bytes, addr: tuple[str, int]):
        packet = self.proto.parse_packet(data)
        if packet is None:
            print(f"Received unknown packet from {addr}")
            return

        if isinstance(packet, ExecutionRequest):
            url_path = packet.path

            exe_name = url_path.split("/")[-1]

            url = f"http://{self.exe_server}/{url_path}"
            print(f"Downloading {url} --> {exe_name}")
            urllib.request.urlretrieve(url, exe_name)

            print(f"Executing {exe_name}")
            self.send_packet(StartedExecution(exe_name=exe_name), addr)
            try:
                output = subprocess.check_output(
                    f"{exe_name}; echo $?", stderr=subprocess.STDOUT, shell=True
                )
            except subprocess.CalledProcessError as e:
                output = e.output

            # sendto addr with 64byte chunked
            for i in range(0, len(output), 64):
                chunk = output[i : i + 64]
                self.send_packet(ProgramLog(exe_name=exe_name, log_data=chunk), addr)

            print("Execution finished")
            self.send_packet(StartedExecution(exe_name=exe_name), addr)


async def server(listen_on: tuple[str, int], exe_server: str):
    loop = asyncio.get_running_loop()

    print(f"Listening on {listen_on[0]}:{listen_on[1]}")
    transport, _ = await loop.create_datagram_endpoint(
        lambda: DaemonUDPProtocol(exe_server),  # type: ignore
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
