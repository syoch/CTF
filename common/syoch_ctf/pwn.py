import argparse
from typing import Callable, Literal

import pwn

pwn.context.terminal = ["tmux", "splitw", "-h"]
pwn.context.log_level = "debug"


type SolverResult = (
    Literal["SolverFailure"] | Literal["SolverSuccess"] | Literal["RequestRestart"]
)
type Solver = Callable[[pwn.tube], SolverResult]
type TubeFactory = Callable[[], pwn.tube]


def execute_solver(solver: Solver, factory: TubeFactory):
    while True:
        tube = factory()

        result = solver(tube)
        match result:
            case "SolverFailure":
                tube.close()
                return
            case "SolverSuccess":
                tube.close()
                return
            case "RequestRestart":
                tube.close()


def local_process_factory(executable: str, with_gdb: bool) -> TubeFactory:
    def factory():
        p = pwn.process([executable])
        if with_gdb:
            pwn.gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
        return p

    return factory


def remote_process_factory(host: str, port: int) -> TubeFactory:
    def factory():
        return pwn.remote(host, port)

    return factory


def auto_solver(local_executable: str, remote_host: str, remote_port: int):
    def deco(solver: Solver):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--target",
            choices=["local", "local-gdb", "remote"],
            help="Target to run the solver",
        )
        args = parser.parse_args()

        if args.target == "local":
            factory = local_process_factory(local_executable, False)
        elif args.target == "local-gdb":
            factory = local_process_factory(local_executable, True)
        else:
            factory = remote_process_factory(remote_host, remote_port)

        execute_solver(solver, factory)

    return deco
