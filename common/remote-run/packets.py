from typing import Self


class Packet:
    def __init__(self):
        pass

    def pack(self) -> bytes:
        raise NotImplementedError

    def unpack(self, _payload: bytes) -> Self | None:
        raise NotImplementedError


class ExecutionRequest(Packet):
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def pack(self) -> bytes:
        return self.path.encode()

    def unpack(self, payload: bytes):
        return ExecutionRequest(payload.decode())


class StartedExecution(Packet):
    def __init__(self, exe_name: str):
        super().__init__()
        self.exe_name = exe_name

    def pack(self) -> bytes:
        return self.exe_name.encode()

    def unpack(self, payload: bytes):
        return StartedExecution(payload.decode())


class StoppedExecution(Packet):
    def __init__(self, exe_name: str):
        super().__init__()
        self.exe_name = exe_name

    def pack(self) -> bytes:
        return self.exe_name.encode()

    def unpack(self, payload: bytes):
        return StoppedExecution(payload.decode())


class ProgramLog(Packet):
    def __init__(self, exe_name: str, log_data: bytes):
        super().__init__()
        self.exe_name = exe_name
        self.data = log_data

    def pack(self) -> bytes:
        return self.exe_name.encode() + bytes([0]) + self.data

    def unpack(self, payload: bytes):
        exe_name_length = payload.find(b"\0")
        exe_name = payload[0:exe_name_length].decode()

        data = payload[exe_name_length + 1 :]

        return ProgramLog(exe_name=exe_name, log_data=data)
