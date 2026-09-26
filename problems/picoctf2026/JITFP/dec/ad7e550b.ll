source_filename = "test"
target datalayout = "e-m:e-p:64:64-i64:64-f80:128-n8:16:32:64-S128"

%_IO_FILE = type { i32 }

@global_var_3dc8 = local_unnamed_addr global i64 1
@global_var_3fd8 = local_unnamed_addr global i64 0
@global_var_22a0 = constant i64 292057776156
@global_var_3ff8 = local_unnamed_addr global i64 0
@global_var_40e0 = global i64 0
@global_var_2000 = constant [18 x i8] c"Usage: %s <flag>\0A\00"
@global_var_4020 = local_unnamed_addr global i64 94489280542
@global_var_4120 = local_unnamed_addr global i64 0
@global_var_2014 = constant [10 x i8] c"Incorrect\00"
@global_var_201e = constant [11 x i8] c"\0AIncorrect\00"
@global_var_2029 = constant [9 x i8] c"\0ACorrect\00"
@global_var_40c0 = local_unnamed_addr global i8 0
@global_var_3dc0 = local_unnamed_addr global %_IO_FILE* null
@0 = internal constant [2 x i8] c"v\00"
@1 = constant i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i64 0, i64 0)
@global_var_2012 = constant [2 x i8] c"v\00"

define i64 @_init() local_unnamed_addr {
dec_label_pc_1000:
  %0 = alloca i64
  %1 = load i64, i64* %0
  ret i64 %1, !insn.addr !0
}

define i64 @function_1001(i64 %arg1) local_unnamed_addr {
dec_label_pc_1001:
  ret i64 %arg1, !insn.addr !1
}

define i32 @function_1020(i32 %c) local_unnamed_addr {
dec_label_pc_1020:
  %0 = call i32 @putchar(i32 %c), !insn.addr !2
  ret i32 %0, !insn.addr !2
}

define i32 @function_1030(i8* %format, ...) local_unnamed_addr {
dec_label_pc_1030:
  %0 = call i32 (i8*, ...) @printf(i8* %format), !insn.addr !3
  ret i32 %0, !insn.addr !3
}

define i32 @function_1040(i32 %option, i32 %arg2, i32 %arg3, i32 %arg4, i32 %arg5) local_unnamed_addr {
dec_label_pc_1040:
  %0 = call i32 @prctl(i32 %option, i32 %arg2, i32 %arg3, i32 %arg4, i32 %arg5), !insn.addr !4
  ret i32 %0, !insn.addr !4
}

define i32 @function_1050(i8* %s) local_unnamed_addr {
dec_label_pc_1050:
  %0 = call i32 @puts(i8* %s), !insn.addr !5
  ret i32 %0, !insn.addr !5
}

define i32 @function_1060(i32 %seconds) local_unnamed_addr {
dec_label_pc_1060:
  %0 = call i32 @sleep(i32 %seconds), !insn.addr !6
  ret i32 %0, !insn.addr !6
}

define i32 @function_1070(%_IO_FILE* %stream) local_unnamed_addr {
dec_label_pc_1070:
  %0 = call i32 @fflush(%_IO_FILE* %stream), !insn.addr !7
  ret i32 %0, !insn.addr !7
}

define i32 @function_1080(i64 %main, i32 %argc, i8** %ubp_av, void ()* %init, void ()* %fini, void ()* %rtld_fini) local_unnamed_addr {
dec_label_pc_1080:
  %0 = call i32 @__libc_start_main(i64 %main, i32 %argc, i8** %ubp_av, void ()* %init, void ()* %fini, void ()* %rtld_fini), !insn.addr !8
  ret i32 %0, !insn.addr !8
}

define i64 @entry_point(i64 %arg1, i64 %arg2, i64 %arg3, i64 %arg4, i64 %arg5, i64 %arg6, i64 %arg7) local_unnamed_addr {
dec_label_pc_1090:
  %stack_var_8 = alloca i64, align 8
  %0 = trunc i64 %arg7 to i32, !insn.addr !9
  %1 = bitcast i64* %stack_var_8 to i8**, !insn.addr !10
  %2 = call i32 @__libc_start_main(i64 6530, i32 %0, i8** nonnull %1, void ()* inttoptr (i64 4096 to void ()*), void ()* inttoptr (i64 6939 to void ()*), void ()* null), !insn.addr !10
  %3 = sext i32 %2 to i64, !insn.addr !10
  ret i64 %3, !insn.addr !10
}

define i64 @function_10d0() local_unnamed_addr {
dec_label_pc_10d0:
  ret i64 16552, !insn.addr !11
}

define i64 @function_1100() local_unnamed_addr {
dec_label_pc_1100:
  ret i64 0, !insn.addr !12
}

define i64 @function_1140() local_unnamed_addr {
dec_label_pc_1140:
  %0 = alloca i64
  %rax.0.reg2mem = alloca i64, !insn.addr !13
  %1 = load i64, i64* %0
  %2 = load i8, i8* @global_var_40c0, align 1, !insn.addr !13
  %3 = icmp eq i8 %2, 0, !insn.addr !13
  %4 = icmp eq i1 %3, false, !insn.addr !14
  br i1 %4, label %dec_label_pc_1190, label %dec_label_pc_1149, !insn.addr !14

dec_label_pc_1149:                                ; preds = %dec_label_pc_1140
  %5 = load i64, i64* @global_var_3fd8, align 8, !insn.addr !15
  %6 = icmp eq i64 %5, 0, !insn.addr !15
  br i1 %6, label %dec_label_pc_1164, label %dec_label_pc_1157, !insn.addr !16

dec_label_pc_1157:                                ; preds = %dec_label_pc_1149
  %7 = load i64, i64* inttoptr (i64 16384 to i64*), align 16384, !insn.addr !17
  %8 = inttoptr i64 %7 to i64*, !insn.addr !18
  call void @__cxa_finalize(i64* %8), !insn.addr !18
  br label %dec_label_pc_1164, !insn.addr !18

dec_label_pc_1164:                                ; preds = %dec_label_pc_1157, %dec_label_pc_1149
  %9 = call i64 @function_10d0(), !insn.addr !19
  %10 = load i64, i64* inttoptr (i64 16352 to i64*), align 32, !insn.addr !20
  %11 = icmp eq i64 %10, 0, !insn.addr !20
  store i64 %9, i64* %rax.0.reg2mem, !insn.addr !21
  br i1 %11, label %dec_label_pc_1180, label %dec_label_pc_1173, !insn.addr !21

dec_label_pc_1173:                                ; preds = %dec_label_pc_1164
  %12 = call i64 @__deregister_frame_info(i64* nonnull @global_var_22a0), !insn.addr !22
  store i64 %12, i64* %rax.0.reg2mem, !insn.addr !22
  br label %dec_label_pc_1180, !insn.addr !22

dec_label_pc_1180:                                ; preds = %dec_label_pc_1173, %dec_label_pc_1164
  %rax.0.reload = load i64, i64* %rax.0.reg2mem
  store i8 1, i8* @global_var_40c0, align 1, !insn.addr !23
  ret i64 %rax.0.reload, !insn.addr !24

dec_label_pc_1190:                                ; preds = %dec_label_pc_1140
  ret i64 %1, !insn.addr !25

; uselistorder directives
  uselistorder i8* @global_var_40c0, { 1, 0 }
}

define i64 @function_11a0() local_unnamed_addr {
dec_label_pc_11a0:
  %0 = load i64, i64* @global_var_3ff8, align 8, !insn.addr !26
  %1 = icmp eq i64 %0, 0, !insn.addr !26
  br i1 %1, label %dec_label_pc_11d0, label %dec_label_pc_11aa, !insn.addr !27

dec_label_pc_11aa:                                ; preds = %dec_label_pc_11a0
  %2 = call i64 @__register_frame_info(i64* nonnull @global_var_22a0, i64* nonnull @global_var_40e0), !insn.addr !28
  %3 = call i64 @function_1100(), !insn.addr !29
  ret i64 %3, !insn.addr !29

dec_label_pc_11d0:                                ; preds = %dec_label_pc_11a0
  %4 = call i64 @function_1100(), !insn.addr !30
  ret i64 %4, !insn.addr !30

; uselistorder directives
  uselistorder i64 ()* @function_1100, { 1, 0 }
}

define i64 @function_11d5(i64 %arg1) local_unnamed_addr {
dec_label_pc_11d5:
  %0 = trunc i64 %arg1 to i8, !insn.addr !31
  %1 = icmp eq i8 %0, 97, !insn.addr !32
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !33
}

define i64 @function_11f2(i64 %arg1) local_unnamed_addr {
dec_label_pc_11f2:
  %0 = trunc i64 %arg1 to i8, !insn.addr !34
  %1 = icmp eq i8 %0, 98, !insn.addr !35
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !36
}

define i64 @function_120f(i64 %arg1) local_unnamed_addr {
dec_label_pc_120f:
  %0 = trunc i64 %arg1 to i8, !insn.addr !37
  %1 = icmp eq i8 %0, 99, !insn.addr !38
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !39
}

define i64 @function_122c(i64 %arg1) local_unnamed_addr {
dec_label_pc_122c:
  %0 = trunc i64 %arg1 to i8, !insn.addr !40
  %1 = icmp eq i8 %0, 100, !insn.addr !41
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !42
}

define i64 @function_1249(i64 %arg1) local_unnamed_addr {
dec_label_pc_1249:
  %0 = trunc i64 %arg1 to i8, !insn.addr !43
  %1 = icmp eq i8 %0, 101, !insn.addr !44
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !45
}

define i64 @function_1266(i64 %arg1) local_unnamed_addr {
dec_label_pc_1266:
  %0 = trunc i64 %arg1 to i8, !insn.addr !46
  %1 = icmp eq i8 %0, 102, !insn.addr !47
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !48
}

define i64 @function_1283(i64 %arg1) local_unnamed_addr {
dec_label_pc_1283:
  %0 = trunc i64 %arg1 to i8, !insn.addr !49
  %1 = icmp eq i8 %0, 103, !insn.addr !50
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !51
}

define i64 @function_12a0(i64 %arg1) local_unnamed_addr {
dec_label_pc_12a0:
  %0 = trunc i64 %arg1 to i8, !insn.addr !52
  %1 = icmp eq i8 %0, 104, !insn.addr !53
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !54
}

define i64 @function_12bd(i64 %arg1) local_unnamed_addr {
dec_label_pc_12bd:
  %0 = trunc i64 %arg1 to i8, !insn.addr !55
  %1 = icmp eq i8 %0, 105, !insn.addr !56
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !57
}

define i64 @function_12da(i64 %arg1) local_unnamed_addr {
dec_label_pc_12da:
  %0 = trunc i64 %arg1 to i8, !insn.addr !58
  %1 = icmp eq i8 %0, 106, !insn.addr !59
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !60
}

define i64 @function_12f7(i64 %arg1) local_unnamed_addr {
dec_label_pc_12f7:
  %0 = trunc i64 %arg1 to i8, !insn.addr !61
  %1 = icmp eq i8 %0, 107, !insn.addr !62
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !63
}

define i64 @function_1314(i64 %arg1) local_unnamed_addr {
dec_label_pc_1314:
  %0 = trunc i64 %arg1 to i8, !insn.addr !64
  %1 = icmp eq i8 %0, 108, !insn.addr !65
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !66
}

define i64 @function_1331(i64 %arg1) local_unnamed_addr {
dec_label_pc_1331:
  %0 = trunc i64 %arg1 to i8, !insn.addr !67
  %1 = icmp eq i8 %0, 109, !insn.addr !68
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !69
}

define i64 @function_134e(i64 %arg1) local_unnamed_addr {
dec_label_pc_134e:
  %0 = trunc i64 %arg1 to i8, !insn.addr !70
  %1 = icmp eq i8 %0, 110, !insn.addr !71
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !72
}

define i64 @function_136b(i64 %arg1) local_unnamed_addr {
dec_label_pc_136b:
  %0 = trunc i64 %arg1 to i8, !insn.addr !73
  %1 = icmp eq i8 %0, 111, !insn.addr !74
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !75
}

define i64 @function_1388(i64 %arg1) local_unnamed_addr {
dec_label_pc_1388:
  %0 = trunc i64 %arg1 to i8, !insn.addr !76
  %1 = icmp eq i8 %0, 112, !insn.addr !77
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !78
}

define i64 @function_13a5(i64 %arg1) local_unnamed_addr {
dec_label_pc_13a5:
  %0 = trunc i64 %arg1 to i8, !insn.addr !79
  %1 = icmp eq i8 %0, 113, !insn.addr !80
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !81
}

define i64 @function_13c2(i64 %arg1) local_unnamed_addr {
dec_label_pc_13c2:
  %0 = trunc i64 %arg1 to i8, !insn.addr !82
  %1 = icmp eq i8 %0, 114, !insn.addr !83
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !84
}

define i64 @function_13df(i64 %arg1) local_unnamed_addr {
dec_label_pc_13df:
  %0 = trunc i64 %arg1 to i8, !insn.addr !85
  %1 = icmp eq i8 %0, 115, !insn.addr !86
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !87
}

define i64 @function_13fc(i64 %arg1) local_unnamed_addr {
dec_label_pc_13fc:
  %0 = trunc i64 %arg1 to i8, !insn.addr !88
  %1 = icmp eq i8 %0, 116, !insn.addr !89
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !90
}

define i64 @function_1419(i64 %arg1) local_unnamed_addr {
dec_label_pc_1419:
  %0 = trunc i64 %arg1 to i8, !insn.addr !91
  %1 = icmp eq i8 %0, 117, !insn.addr !92
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !93
}

define i64 @function_1436(i64 %arg1) local_unnamed_addr {
dec_label_pc_1436:
  %0 = trunc i64 %arg1 to i8, !insn.addr !94
  %1 = icmp eq i8 %0, 118, !insn.addr !95
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !96
}

define i64 @function_1453(i64 %arg1) local_unnamed_addr {
dec_label_pc_1453:
  %0 = trunc i64 %arg1 to i8, !insn.addr !97
  %1 = icmp eq i8 %0, 119, !insn.addr !98
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !99
}

define i64 @function_1470(i64 %arg1) local_unnamed_addr {
dec_label_pc_1470:
  %0 = trunc i64 %arg1 to i8, !insn.addr !100
  %1 = icmp eq i8 %0, 120, !insn.addr !101
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !102
}

define i64 @function_148d(i64 %arg1) local_unnamed_addr {
dec_label_pc_148d:
  %0 = trunc i64 %arg1 to i8, !insn.addr !103
  %1 = icmp eq i8 %0, 121, !insn.addr !104
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !105
}

define i64 @function_14aa(i64 %arg1) local_unnamed_addr {
dec_label_pc_14aa:
  %0 = trunc i64 %arg1 to i8, !insn.addr !106
  %1 = icmp eq i8 %0, 122, !insn.addr !107
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !108
}

define i64 @function_14c7(i64 %arg1) local_unnamed_addr {
dec_label_pc_14c7:
  %0 = trunc i64 %arg1 to i8, !insn.addr !109
  %1 = icmp eq i8 %0, 65, !insn.addr !110
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !111
}

define i64 @function_14e4(i64 %arg1) local_unnamed_addr {
dec_label_pc_14e4:
  %0 = trunc i64 %arg1 to i8, !insn.addr !112
  %1 = icmp eq i8 %0, 66, !insn.addr !113
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !114
}

define i64 @function_1501(i64 %arg1) local_unnamed_addr {
dec_label_pc_1501:
  %0 = trunc i64 %arg1 to i8, !insn.addr !115
  %1 = icmp eq i8 %0, 67, !insn.addr !116
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !117
}

define i64 @function_151e(i64 %arg1) local_unnamed_addr {
dec_label_pc_151e:
  %0 = trunc i64 %arg1 to i8, !insn.addr !118
  %1 = icmp eq i8 %0, 68, !insn.addr !119
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !120
}

define i64 @function_153b(i64 %arg1) local_unnamed_addr {
dec_label_pc_153b:
  %0 = trunc i64 %arg1 to i8, !insn.addr !121
  %1 = icmp eq i8 %0, 69, !insn.addr !122
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !123
}

define i64 @function_1558(i64 %arg1) local_unnamed_addr {
dec_label_pc_1558:
  %0 = trunc i64 %arg1 to i8, !insn.addr !124
  %1 = icmp eq i8 %0, 70, !insn.addr !125
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !126
}

define i64 @function_1575(i64 %arg1) local_unnamed_addr {
dec_label_pc_1575:
  %0 = trunc i64 %arg1 to i8, !insn.addr !127
  %1 = icmp eq i8 %0, 71, !insn.addr !128
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !129
}

define i64 @function_1592(i64 %arg1) local_unnamed_addr {
dec_label_pc_1592:
  %0 = trunc i64 %arg1 to i8, !insn.addr !130
  %1 = icmp eq i8 %0, 72, !insn.addr !131
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !132
}

define i64 @function_15af(i64 %arg1) local_unnamed_addr {
dec_label_pc_15af:
  %0 = trunc i64 %arg1 to i8, !insn.addr !133
  %1 = icmp eq i8 %0, 73, !insn.addr !134
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !135
}

define i64 @function_15cc(i64 %arg1) local_unnamed_addr {
dec_label_pc_15cc:
  %0 = trunc i64 %arg1 to i8, !insn.addr !136
  %1 = icmp eq i8 %0, 74, !insn.addr !137
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !138
}

define i64 @function_15e9(i64 %arg1) local_unnamed_addr {
dec_label_pc_15e9:
  %0 = trunc i64 %arg1 to i8, !insn.addr !139
  %1 = icmp eq i8 %0, 75, !insn.addr !140
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !141
}

define i64 @function_1606(i64 %arg1) local_unnamed_addr {
dec_label_pc_1606:
  %0 = trunc i64 %arg1 to i8, !insn.addr !142
  %1 = icmp eq i8 %0, 76, !insn.addr !143
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !144
}

define i64 @function_1623(i64 %arg1) local_unnamed_addr {
dec_label_pc_1623:
  %0 = trunc i64 %arg1 to i8, !insn.addr !145
  %1 = icmp eq i8 %0, 77, !insn.addr !146
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !147
}

define i64 @function_1640(i64 %arg1) local_unnamed_addr {
dec_label_pc_1640:
  %0 = trunc i64 %arg1 to i8, !insn.addr !148
  %1 = icmp eq i8 %0, 78, !insn.addr !149
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !150
}

define i64 @function_165d(i64 %arg1) local_unnamed_addr {
dec_label_pc_165d:
  %0 = trunc i64 %arg1 to i8, !insn.addr !151
  %1 = icmp eq i8 %0, 79, !insn.addr !152
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !153
}

define i64 @function_167a(i64 %arg1) local_unnamed_addr {
dec_label_pc_167a:
  %0 = trunc i64 %arg1 to i8, !insn.addr !154
  %1 = icmp eq i8 %0, 80, !insn.addr !155
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !156
}

define i64 @function_1697(i64 %arg1) local_unnamed_addr {
dec_label_pc_1697:
  %0 = trunc i64 %arg1 to i8, !insn.addr !157
  %1 = icmp eq i8 %0, 81, !insn.addr !158
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !159
}

define i64 @function_16b4(i64 %arg1) local_unnamed_addr {
dec_label_pc_16b4:
  %0 = trunc i64 %arg1 to i8, !insn.addr !160
  %1 = icmp eq i8 %0, 82, !insn.addr !161
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !162
}

define i64 @function_16d1(i64 %arg1) local_unnamed_addr {
dec_label_pc_16d1:
  %0 = trunc i64 %arg1 to i8, !insn.addr !163
  %1 = icmp eq i8 %0, 83, !insn.addr !164
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !165
}

define i64 @function_16ee(i64 %arg1) local_unnamed_addr {
dec_label_pc_16ee:
  %0 = trunc i64 %arg1 to i8, !insn.addr !166
  %1 = icmp eq i8 %0, 84, !insn.addr !167
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !168
}

define i64 @function_170b(i64 %arg1) local_unnamed_addr {
dec_label_pc_170b:
  %0 = trunc i64 %arg1 to i8, !insn.addr !169
  %1 = icmp eq i8 %0, 85, !insn.addr !170
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !171
}

define i64 @function_1728(i64 %arg1) local_unnamed_addr {
dec_label_pc_1728:
  %0 = trunc i64 %arg1 to i8, !insn.addr !172
  %1 = icmp eq i8 %0, 86, !insn.addr !173
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !174
}

define i64 @function_1745(i64 %arg1) local_unnamed_addr {
dec_label_pc_1745:
  %0 = trunc i64 %arg1 to i8, !insn.addr !175
  %1 = icmp eq i8 %0, 87, !insn.addr !176
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !177
}

define i64 @function_1762(i64 %arg1) local_unnamed_addr {
dec_label_pc_1762:
  %0 = trunc i64 %arg1 to i8, !insn.addr !178
  %1 = icmp eq i8 %0, 88, !insn.addr !179
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !180
}

define i64 @function_177f(i64 %arg1) local_unnamed_addr {
dec_label_pc_177f:
  %0 = trunc i64 %arg1 to i8, !insn.addr !181
  %1 = icmp eq i8 %0, 89, !insn.addr !182
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !183
}

define i64 @function_179c(i64 %arg1) local_unnamed_addr {
dec_label_pc_179c:
  %0 = trunc i64 %arg1 to i8, !insn.addr !184
  %1 = icmp eq i8 %0, 90, !insn.addr !185
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !186
}

define i64 @function_17b9(i64 %arg1) local_unnamed_addr {
dec_label_pc_17b9:
  %0 = trunc i64 %arg1 to i8, !insn.addr !187
  %1 = icmp eq i8 %0, 48, !insn.addr !188
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !189
}

define i64 @function_17d6(i64 %arg1) local_unnamed_addr {
dec_label_pc_17d6:
  %0 = trunc i64 %arg1 to i8, !insn.addr !190
  %1 = icmp eq i8 %0, 49, !insn.addr !191
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !192
}

define i64 @function_17f3(i64 %arg1) local_unnamed_addr {
dec_label_pc_17f3:
  %0 = trunc i64 %arg1 to i8, !insn.addr !193
  %1 = icmp eq i8 %0, 50, !insn.addr !194
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !195
}

define i64 @function_1810(i64 %arg1) local_unnamed_addr {
dec_label_pc_1810:
  %0 = trunc i64 %arg1 to i8, !insn.addr !196
  %1 = icmp eq i8 %0, 51, !insn.addr !197
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !198
}

define i64 @function_182d(i64 %arg1) local_unnamed_addr {
dec_label_pc_182d:
  %0 = trunc i64 %arg1 to i8, !insn.addr !199
  %1 = icmp eq i8 %0, 52, !insn.addr !200
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !201
}

define i64 @function_184a(i64 %arg1) local_unnamed_addr {
dec_label_pc_184a:
  %0 = trunc i64 %arg1 to i8, !insn.addr !202
  %1 = icmp eq i8 %0, 53, !insn.addr !203
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !204
}

define i64 @function_1867(i64 %arg1) local_unnamed_addr {
dec_label_pc_1867:
  %0 = trunc i64 %arg1 to i8, !insn.addr !205
  %1 = icmp eq i8 %0, 54, !insn.addr !206
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !207
}

define i64 @function_1884(i64 %arg1) local_unnamed_addr {
dec_label_pc_1884:
  %0 = trunc i64 %arg1 to i8, !insn.addr !208
  %1 = icmp eq i8 %0, 55, !insn.addr !209
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !210
}

define i64 @function_18a1(i64 %arg1) local_unnamed_addr {
dec_label_pc_18a1:
  %0 = trunc i64 %arg1 to i8, !insn.addr !211
  %1 = icmp eq i8 %0, 56, !insn.addr !212
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !213
}

define i64 @function_18be(i64 %arg1) local_unnamed_addr {
dec_label_pc_18be:
  %0 = trunc i64 %arg1 to i8, !insn.addr !214
  %1 = icmp eq i8 %0, 57, !insn.addr !215
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !216
}

define i64 @function_18db(i64 %arg1) local_unnamed_addr {
dec_label_pc_18db:
  %0 = trunc i64 %arg1 to i8, !insn.addr !217
  %1 = icmp eq i8 %0, 95, !insn.addr !218
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !219
}

define i64 @function_18f8(i64 %arg1) local_unnamed_addr {
dec_label_pc_18f8:
  %0 = trunc i64 %arg1 to i8, !insn.addr !220
  %1 = icmp eq i8 %0, 123, !insn.addr !221
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !222
}

define i64 @function_1915(i64 %arg1) local_unnamed_addr {
dec_label_pc_1915:
  %0 = trunc i64 %arg1 to i8, !insn.addr !223
  %1 = icmp eq i8 %0, 125, !insn.addr !224
  %. = zext i1 %1 to i64
  ret i64 %., !insn.addr !225
}

define i64 @function_1932(i64 %arg1) local_unnamed_addr {
dec_label_pc_1932:
  %storemerge2.reg2mem = alloca i32, !insn.addr !226
  %0 = trunc i64 %arg1 to i32, !insn.addr !227
  %1 = icmp sgt i32 %0, 0, !insn.addr !228
  store i32 0, i32* %storemerge2.reg2mem, !insn.addr !228
  br i1 %1, label %dec_label_pc_1946, label %dec_label_pc_1975, !insn.addr !228

dec_label_pc_1946:                                ; preds = %dec_label_pc_1932, %dec_label_pc_1946
  %storemerge2.reload = load i32, i32* %storemerge2.reg2mem
  %2 = call i32 @putchar(i32 42), !insn.addr !229
  %3 = load %_IO_FILE*, %_IO_FILE** @global_var_3dc0, align 8, !insn.addr !230
  %4 = call i32 @fflush(%_IO_FILE* %3), !insn.addr !231
  %5 = call i32 @sleep(i32 1), !insn.addr !232
  %6 = add nuw nsw i32 %storemerge2.reload, 1, !insn.addr !233
  %exitcond = icmp eq i32 %6, %0
  store i32 %6, i32* %storemerge2.reg2mem, !insn.addr !228
  br i1 %exitcond, label %dec_label_pc_1975, label %dec_label_pc_1946, !insn.addr !228

dec_label_pc_1975:                                ; preds = %dec_label_pc_1946, %dec_label_pc_1932
  %7 = call i32 @putchar(i32 10), !insn.addr !234
  %8 = sext i32 %7 to i64, !insn.addr !234
  ret i64 %8, !insn.addr !235

; uselistorder directives
  uselistorder i32* %storemerge2.reg2mem, { 2, 0, 1 }
  uselistorder label %dec_label_pc_1946, { 1, 0 }
}

define i64 @function_1982(i64 %arg1, i64 %arg2) local_unnamed_addr {
dec_label_pc_1982:
  %rax.0.reg2mem = alloca i64, !insn.addr !236
  %storemerge4.reg2mem = alloca i32, !insn.addr !236
  %.reg2mem = alloca i64, !insn.addr !236
  %storemerge15.reg2mem = alloca i32, !insn.addr !236
  %0 = trunc i64 %arg1 to i32, !insn.addr !237
  %1 = call i32 @prctl(i32 1499557217, i32 -1, i32 0, i32 0, i32 0), !insn.addr !238
  %2 = icmp eq i32 %0, 2, !insn.addr !239
  store i32 0, i32* %storemerge15.reg2mem, !insn.addr !240
  br i1 %2, label %dec_label_pc_19ee, label %dec_label_pc_19bd, !insn.addr !240

dec_label_pc_19bd:                                ; preds = %dec_label_pc_1982
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @global_var_2000, i64 0, i64 0), i8* inttoptr (i64 -1 to i8*)), !insn.addr !241
  store i64 1, i64* %rax.0.reg2mem, !insn.addr !242
  br label %dec_label_pc_1b19, !insn.addr !242

dec_label_pc_19ee:                                ; preds = %dec_label_pc_1982, %dec_label_pc_19ee
  %storemerge15.reload = load i32, i32* %storemerge15.reg2mem
  %4 = call i32 @putchar(i32 61), !insn.addr !243
  %5 = load %_IO_FILE*, %_IO_FILE** @global_var_3dc0, align 8, !insn.addr !244
  %6 = call i32 @fflush(%_IO_FILE* %5), !insn.addr !245
  %7 = add nuw nsw i32 %storemerge15.reload, 1, !insn.addr !246
  %exitcond = icmp eq i32 %7, 32
  store i32 %7, i32* %storemerge15.reg2mem, !insn.addr !247
  br i1 %exitcond, label %dec_label_pc_1a11, label %dec_label_pc_19ee, !insn.addr !247

dec_label_pc_1a11:                                ; preds = %dec_label_pc_19ee
  %8 = call i32 @puts(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @global_var_2012, i64 0, i64 0)), !insn.addr !248
  %9 = call i32 @sleep(i32 1)
  %10 = add i64 %arg2, 8
  %11 = inttoptr i64 %10 to i64*
  %12 = load i64, i64* %11, align 8
  store i64 %12, i64* %.reg2mem
  store i32 0, i32* %storemerge4.reg2mem
  br label %dec_label_pc_1a2c

dec_label_pc_1a2c:                                ; preds = %dec_label_pc_1a11, %dec_label_pc_1aa8
  %storemerge4.reload = load i32, i32* %storemerge4.reg2mem
  %.reload = load i64, i64* %.reg2mem
  %13 = sext i32 %storemerge4.reload to i64, !insn.addr !249
  %14 = add i64 %.reload, %13, !insn.addr !250
  %15 = inttoptr i64 %14 to i8*, !insn.addr !251
  %16 = load i8, i8* %15, align 1, !insn.addr !251
  %17 = icmp eq i8 %16, 0, !insn.addr !252
  %18 = icmp eq i1 %17, false, !insn.addr !253
  br i1 %18, label %dec_label_pc_1aa8, label %dec_label_pc_1a83, !insn.addr !253

dec_label_pc_1a83:                                ; preds = %dec_label_pc_1a2c
  %19 = sub i32 33, %storemerge4.reload, !insn.addr !254
  %20 = zext i32 %19 to i64, !insn.addr !255
  %21 = call i64 @function_1932(i64 %20), !insn.addr !256
  %22 = call i32 @puts(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @global_var_2014, i64 0, i64 0)), !insn.addr !257
  store i64 1, i64* %rax.0.reg2mem, !insn.addr !258
  br label %dec_label_pc_1b19, !insn.addr !258

dec_label_pc_1aa8:                                ; preds = %dec_label_pc_1a2c
  %23 = call i32 @putchar(i32 42), !insn.addr !259
  %24 = load %_IO_FILE*, %_IO_FILE** @global_var_3dc0, align 8, !insn.addr !260
  %25 = call i32 @fflush(%_IO_FILE* %24), !insn.addr !261
  %26 = add nuw i32 %storemerge4.reload, 1, !insn.addr !262
  %27 = icmp ult i32 %26, 33, !insn.addr !263
  %28 = call i32 @sleep(i32 1)
  %29 = load i64, i64* %11, align 8
  store i64 %29, i64* %.reg2mem, !insn.addr !263
  store i32 %26, i32* %storemerge4.reg2mem, !insn.addr !263
  br i1 %27, label %dec_label_pc_1a2c, label %dec_label_pc_1acf, !insn.addr !263

dec_label_pc_1acf:                                ; preds = %dec_label_pc_1aa8
  %30 = add i64 %29, 33, !insn.addr !264
  %31 = inttoptr i64 %30 to i8*, !insn.addr !265
  %32 = load i8, i8* %31, align 1, !insn.addr !265
  %33 = icmp eq i8 %32, 0, !insn.addr !266
  br i1 %33, label %dec_label_pc_1b05, label %dec_label_pc_1aef, !insn.addr !267

dec_label_pc_1aef:                                ; preds = %dec_label_pc_1acf
  %34 = call i32 @puts(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @global_var_201e, i64 0, i64 0)), !insn.addr !268
  store i64 1, i64* %rax.0.reg2mem, !insn.addr !269
  br label %dec_label_pc_1b19, !insn.addr !269

dec_label_pc_1b05:                                ; preds = %dec_label_pc_1acf
  %35 = call i32 @puts(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @global_var_2029, i64 0, i64 0)), !insn.addr !270
  store i64 0, i64* %rax.0.reg2mem, !insn.addr !271
  br label %dec_label_pc_1b19, !insn.addr !271

dec_label_pc_1b19:                                ; preds = %dec_label_pc_1b05, %dec_label_pc_1a83, %dec_label_pc_1aef, %dec_label_pc_19bd
  %rax.0.reload = load i64, i64* %rax.0.reg2mem
  ret i64 %rax.0.reload, !insn.addr !272

; uselistorder directives
  uselistorder i64 %29, { 1, 0 }
  uselistorder i32 %storemerge4.reload, { 0, 2, 1 }
  uselistorder i64* %11, { 1, 0 }
  uselistorder i32* %storemerge15.reg2mem, { 2, 0, 1 }
  uselistorder i64* %.reg2mem, { 1, 0, 2 }
  uselistorder i32* %storemerge4.reg2mem, { 1, 0, 2 }
  uselistorder i64* %rax.0.reg2mem, { 0, 3, 2, 4, 1 }
  uselistorder i8 0, { 2, 0, 3, 1 }
  uselistorder i32 (i32)* @sleep, { 2, 0, 1, 3 }
  uselistorder i32 (i8*)* @puts, { 3, 1, 2, 0, 4 }
  uselistorder i32 (%_IO_FILE*)* @fflush, { 2, 1, 0, 3 }
  uselistorder %_IO_FILE** @global_var_3dc0, { 2, 1, 0 }
  uselistorder i32 (i32)* @putchar, { 3, 2, 0, 1, 4 }
  uselistorder i64 1, { 1, 2, 0, 3 }
  uselistorder i64 0, { 0, 8, 9, 10, 11, 6, 7, 1, 2, 12, 13, 18, 19, 20, 3, 4, 5, 14, 15, 16, 17 }
  uselistorder i32 0, { 0, 1, 4, 5, 6, 2, 3 }
  uselistorder label %dec_label_pc_1b19, { 0, 2, 1, 3 }
  uselistorder label %dec_label_pc_1a2c, { 1, 0 }
  uselistorder label %dec_label_pc_19ee, { 1, 0 }
}

define i64 @_fini() local_unnamed_addr {
dec_label_pc_1b1b:
  %0 = alloca i64
  %1 = load i64, i64* %0
  ret i64 %1, !insn.addr !273

; uselistorder directives
  uselistorder i32 1, { 2, 10, 13, 9, 14, 6, 5, 4, 3, 15, 11, 7, 8, 1, 12, 0 }
}

define i64 @function_1b1c(i64 %arg1) local_unnamed_addr {
dec_label_pc_1b1c:
  ret i64 %arg1, !insn.addr !274
}

declare i32 @putchar(i32) local_unnamed_addr

declare i32 @printf(i8*, ...) local_unnamed_addr

declare i32 @prctl(i32, i32, i32, i32, i32) local_unnamed_addr

declare i32 @puts(i8*) local_unnamed_addr

declare i32 @sleep(i32) local_unnamed_addr

declare i32 @fflush(%_IO_FILE*) local_unnamed_addr

declare i32 @__libc_start_main(i64, i32, i8**, void ()*, void ()*, void ()*) local_unnamed_addr

declare void @__cxa_finalize(i64*) local_unnamed_addr

declare i64 @__deregister_frame_info(i64*) local_unnamed_addr

declare i64 @__register_frame_info(i64*, i64*) local_unnamed_addr

!0 = !{i64 4096}
!1 = !{i64 4098}
!2 = !{i64 4128}
!3 = !{i64 4144}
!4 = !{i64 4160}
!5 = !{i64 4176}
!6 = !{i64 4192}
!7 = !{i64 4208}
!8 = !{i64 4224}
!9 = !{i64 4262}
!10 = !{i64 4292}
!11 = !{i64 4344}
!12 = !{i64 4408}
!13 = !{i64 4416}
!14 = !{i64 4423}
!15 = !{i64 4426}
!16 = !{i64 4437}
!17 = !{i64 4439}
!18 = !{i64 4446}
!19 = !{i64 4452}
!20 = !{i64 4457}
!21 = !{i64 4465}
!22 = !{i64 4474}
!23 = !{i64 4480}
!24 = !{i64 4488}
!25 = !{i64 4496}
!26 = !{i64 4512}
!27 = !{i64 4520}
!28 = !{i64 4540}
!29 = !{i64 4547}
!30 = !{i64 4560}
!31 = !{i64 4571}
!32 = !{i64 4574}
!33 = !{i64 4593}
!34 = !{i64 4600}
!35 = !{i64 4603}
!36 = !{i64 4622}
!37 = !{i64 4629}
!38 = !{i64 4632}
!39 = !{i64 4651}
!40 = !{i64 4658}
!41 = !{i64 4661}
!42 = !{i64 4680}
!43 = !{i64 4687}
!44 = !{i64 4690}
!45 = !{i64 4709}
!46 = !{i64 4716}
!47 = !{i64 4719}
!48 = !{i64 4738}
!49 = !{i64 4745}
!50 = !{i64 4748}
!51 = !{i64 4767}
!52 = !{i64 4774}
!53 = !{i64 4777}
!54 = !{i64 4796}
!55 = !{i64 4803}
!56 = !{i64 4806}
!57 = !{i64 4825}
!58 = !{i64 4832}
!59 = !{i64 4835}
!60 = !{i64 4854}
!61 = !{i64 4861}
!62 = !{i64 4864}
!63 = !{i64 4883}
!64 = !{i64 4890}
!65 = !{i64 4893}
!66 = !{i64 4912}
!67 = !{i64 4919}
!68 = !{i64 4922}
!69 = !{i64 4941}
!70 = !{i64 4948}
!71 = !{i64 4951}
!72 = !{i64 4970}
!73 = !{i64 4977}
!74 = !{i64 4980}
!75 = !{i64 4999}
!76 = !{i64 5006}
!77 = !{i64 5009}
!78 = !{i64 5028}
!79 = !{i64 5035}
!80 = !{i64 5038}
!81 = !{i64 5057}
!82 = !{i64 5064}
!83 = !{i64 5067}
!84 = !{i64 5086}
!85 = !{i64 5093}
!86 = !{i64 5096}
!87 = !{i64 5115}
!88 = !{i64 5122}
!89 = !{i64 5125}
!90 = !{i64 5144}
!91 = !{i64 5151}
!92 = !{i64 5154}
!93 = !{i64 5173}
!94 = !{i64 5180}
!95 = !{i64 5183}
!96 = !{i64 5202}
!97 = !{i64 5209}
!98 = !{i64 5212}
!99 = !{i64 5231}
!100 = !{i64 5238}
!101 = !{i64 5241}
!102 = !{i64 5260}
!103 = !{i64 5267}
!104 = !{i64 5270}
!105 = !{i64 5289}
!106 = !{i64 5296}
!107 = !{i64 5299}
!108 = !{i64 5318}
!109 = !{i64 5325}
!110 = !{i64 5328}
!111 = !{i64 5347}
!112 = !{i64 5354}
!113 = !{i64 5357}
!114 = !{i64 5376}
!115 = !{i64 5383}
!116 = !{i64 5386}
!117 = !{i64 5405}
!118 = !{i64 5412}
!119 = !{i64 5415}
!120 = !{i64 5434}
!121 = !{i64 5441}
!122 = !{i64 5444}
!123 = !{i64 5463}
!124 = !{i64 5470}
!125 = !{i64 5473}
!126 = !{i64 5492}
!127 = !{i64 5499}
!128 = !{i64 5502}
!129 = !{i64 5521}
!130 = !{i64 5528}
!131 = !{i64 5531}
!132 = !{i64 5550}
!133 = !{i64 5557}
!134 = !{i64 5560}
!135 = !{i64 5579}
!136 = !{i64 5586}
!137 = !{i64 5589}
!138 = !{i64 5608}
!139 = !{i64 5615}
!140 = !{i64 5618}
!141 = !{i64 5637}
!142 = !{i64 5644}
!143 = !{i64 5647}
!144 = !{i64 5666}
!145 = !{i64 5673}
!146 = !{i64 5676}
!147 = !{i64 5695}
!148 = !{i64 5702}
!149 = !{i64 5705}
!150 = !{i64 5724}
!151 = !{i64 5731}
!152 = !{i64 5734}
!153 = !{i64 5753}
!154 = !{i64 5760}
!155 = !{i64 5763}
!156 = !{i64 5782}
!157 = !{i64 5789}
!158 = !{i64 5792}
!159 = !{i64 5811}
!160 = !{i64 5818}
!161 = !{i64 5821}
!162 = !{i64 5840}
!163 = !{i64 5847}
!164 = !{i64 5850}
!165 = !{i64 5869}
!166 = !{i64 5876}
!167 = !{i64 5879}
!168 = !{i64 5898}
!169 = !{i64 5905}
!170 = !{i64 5908}
!171 = !{i64 5927}
!172 = !{i64 5934}
!173 = !{i64 5937}
!174 = !{i64 5956}
!175 = !{i64 5963}
!176 = !{i64 5966}
!177 = !{i64 5985}
!178 = !{i64 5992}
!179 = !{i64 5995}
!180 = !{i64 6014}
!181 = !{i64 6021}
!182 = !{i64 6024}
!183 = !{i64 6043}
!184 = !{i64 6050}
!185 = !{i64 6053}
!186 = !{i64 6072}
!187 = !{i64 6079}
!188 = !{i64 6082}
!189 = !{i64 6101}
!190 = !{i64 6108}
!191 = !{i64 6111}
!192 = !{i64 6130}
!193 = !{i64 6137}
!194 = !{i64 6140}
!195 = !{i64 6159}
!196 = !{i64 6166}
!197 = !{i64 6169}
!198 = !{i64 6188}
!199 = !{i64 6195}
!200 = !{i64 6198}
!201 = !{i64 6217}
!202 = !{i64 6224}
!203 = !{i64 6227}
!204 = !{i64 6246}
!205 = !{i64 6253}
!206 = !{i64 6256}
!207 = !{i64 6275}
!208 = !{i64 6282}
!209 = !{i64 6285}
!210 = !{i64 6304}
!211 = !{i64 6311}
!212 = !{i64 6314}
!213 = !{i64 6333}
!214 = !{i64 6340}
!215 = !{i64 6343}
!216 = !{i64 6362}
!217 = !{i64 6369}
!218 = !{i64 6372}
!219 = !{i64 6391}
!220 = !{i64 6398}
!221 = !{i64 6401}
!222 = !{i64 6420}
!223 = !{i64 6427}
!224 = !{i64 6430}
!225 = !{i64 6449}
!226 = !{i64 6450}
!227 = !{i64 6512}
!228 = !{i64 6515}
!229 = !{i64 6475}
!230 = !{i64 6480}
!231 = !{i64 6490}
!232 = !{i64 6500}
!233 = !{i64 6505}
!234 = !{i64 6522}
!235 = !{i64 6529}
!236 = !{i64 6530}
!237 = !{i64 6538}
!238 = !{i64 6578}
!239 = !{i64 6583}
!240 = !{i64 6587}
!241 = !{i64 6614}
!242 = !{i64 6624}
!243 = !{i64 6643}
!244 = !{i64 6648}
!245 = !{i64 6658}
!246 = !{i64 6663}
!247 = !{i64 6671}
!248 = !{i64 6683}
!249 = !{i64 6768}
!250 = !{i64 6770}
!251 = !{i64 6773}
!252 = !{i64 6783}
!253 = !{i64 6785}
!254 = !{i64 6792}
!255 = !{i64 6795}
!256 = !{i64 6797}
!257 = !{i64 6812}
!258 = !{i64 6822}
!259 = !{i64 6829}
!260 = !{i64 6834}
!261 = !{i64 6844}
!262 = !{i64 6849}
!263 = !{i64 6857}
!264 = !{i64 6884}
!265 = !{i64 6888}
!266 = !{i64 6891}
!267 = !{i64 6893}
!268 = !{i64 6905}
!269 = !{i64 6915}
!270 = !{i64 6927}
!271 = !{i64 6932}
!272 = !{i64 6938}
!273 = !{i64 6939}
!274 = !{i64 6941}
