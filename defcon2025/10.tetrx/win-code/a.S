
        .section .text
        .global _start
        _start:
            # mov 0(%rsp), %rax
            movabs $0x0000555555555a04, %rax
            call *%rax

        a:  jmp a
        