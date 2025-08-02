# Snippet

```
fn:
 mov    rax,QWORD PTR [rsp]
 sub    rax,0x1109
 call   rax
 jmp    0
```

# Control
- a: left
- s: right
- r: soft drop
- w: hard drop
- q: ccw
- f: cw

# Relocation @gdb
```
.text: 0x0000555555555000
win: 0x0000555555555a00

.board: 0x00007ffff7fbf000
```

# Board
```
|####    # #     |
|################|
|    ## ### ###  |
|### #### ### ###|
|  # # # ##### # |
|################|
|   # ## ##  # # |
|#### #  ##  ### |
| ### ## #### #  |
| #   ## #  # ## |
|## ### ##### #  |
|################|
| ## # #    #  # |
|################|
|#   ##   ## ####|
```


e8 b2 07 00 00