import asyncio

from .protocol import Protocol
from .packets import (
    ExecutionRequest,
    Packet,
    StartedExecution,
    StoppedExecution,
    ProgramLog,
)


class ClientUDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, program: str) -> None:
        super().__init__()
        self.program = program
        self.proto = Protocol.default_protocol()
        self.program_stopped = False

    def send_packet(self, packet: Packet):
        data = self.proto.pack_packet(packet)
        self.transport.sendto(data)

    def connection_made(self, transport: asyncio.DatagramTransport):
        self.transport = transport
        print(f"Requesting execution of {self.program}")
        self.send_packet(ExecutionRequest(path=self.program))

    def datagram_received(self, data: bytes, addr: tuple[str, int]):
        packet = self.proto.parse_packet(data)
        if packet is None:
            print(f"Received unknown packet from {addr}")
            return

        if isinstance(packet, StartedExecution):
            print(f"Execution started: {packet.exe_name}")
        elif isinstance(packet, StoppedExecution):
            print(f"Execution stopped: {packet.exe_name}")
            self.program_stopped = True
        elif isinstance(packet, ProgramLog):
            print(f"[{packet.exe_name}] {packet.data.decode(errors='ignore')}", end="")

    async def wait_until_stopped(self):
        while not self.program_stopped:
            await asyncio.sleep(1)


async def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog="client",
    )
    parser.add_argument("-s", "--server")
    parser.add_argument("-p", "--program")

    args = parser.parse_args()
    server, program = args.server, args.program

    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientUDPProtocol(program),
        remote_addr=(server, 31000),
    )

    try:
        await protocol.wait_until_stopped()
    finally:
        transport.close()


if __name__ == "__main__":
    asyncio.run(main())
