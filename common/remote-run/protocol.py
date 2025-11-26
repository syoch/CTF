from .packets import (
    ExecutionRequest,
    Packet,
    StartedExecution,
    StoppedExecution,
    ProgramLog,
)


class Protocol:
    def __init__(self):
        self.packets: list[tuple[int, Packet]] = []

    @classmethod
    def default_protocol(cls) -> "Protocol":
        protocol = cls()
        protocol.add_packet_type(0x00, ExecutionRequest)
        protocol.add_packet_type(0x01, ProgramLog)
        protocol.add_packet_type(0x02, StartedExecution)
        protocol.add_packet_type(0x03, StoppedExecution)
        return protocol

    def add_packet_type(self, opcode: int, packet_class: type):
        self.packets.append((opcode, packet_class()))

    def parse_packet(self, data: bytes) -> Packet | None:
        if not data:
            return None

        opcode = data[0]
        payload = data[1:]

        for code, packet in self.packets:
            if code == opcode:
                return packet.unpack(payload)

        return None

    def pack_packet(self, packet: Packet) -> bytes:
        for code, pkt in self.packets:
            if isinstance(packet, type(pkt)):
                return bytes([code]) + packet.pack()
        raise ValueError("Unknown packet type")
