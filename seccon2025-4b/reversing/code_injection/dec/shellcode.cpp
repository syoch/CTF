#include <stdint.h>

using WCHAR = uint16_t;

struct UserProcParam_Env {
  WCHAR *k;
  WCHAR *v;
}

void fn(uint64_t param_1, uint64_t param_2, uint32_t param_3) {
  uint8_t auVar1[16];
  long i;
  int *strings2;
  WCHAR *strings;
  UserProcParam_Env *env;
  long lVar2;
  GS *gs;
  uint32_t buf[6];
  _LIST_ENTRY *mod_entry_1;
  _LIST_ENTRY *mod_entry_2;
  uint offset;

  mod_entry_1 = ((gs->peb->LoaderData->InMemoryOrderModuleList).Flink)->Flink;
  mod_entry_2 = mod_entry_1->Flink;
  buf[4] =
      (uint32_t)((mod_entry_2[5].Flink)->Flink +
                 (((uint32_t)(mod_entry_1[5].Flink)->Flink | 0x20002000200020) ^
                  (uint32_t)env->k) *
                     0x10) |
      0x20002000200020;
  mod_entry_1 = mod_entry_2[2].Flink;
  lVar2 =
      (long)&mod_entry_1->Flink +
      (uint32_t)*(uint *)((long)&mod_entry_1[8].Blink +
                          (uint32_t)*(uint *)((long)&mod_entry_1[3].Blink + 4));
  buf[2] = 0x2a087d454e564005;
  i = 0;
  while (((strings2 =
               (int *)((long)&mod_entry_1->Flink +
                       (uint32_t)*(uint *)((long)&mod_entry_1->Flink + i * 4 +
                                           (uint32_t)*(uint *)(lVar2 + 0x20))),
           *strings2 != 0x53746547 || (strings2[1] != 0x61486474)) ||
          (strings2[2] != 0x656c646e))) {
    i = i + 1;
  }
  buf[3] = 0x52134041503a405b;
  (*(void (*)())(
      (long)&mod_entry_1->Flink +
      (uint32_t)*(
          uint32_t *)((long)&mod_entry_1->Flink +
                      CONCAT62(
                          (int6)((uint32_t)i >> 0x10),
                          *(undefined2 *)((long)&mod_entry_1->Flink + i * 2 +
                                          (uint32_t)*(uint *)(lVar2 + 0x24))) *
                          4 +
                      (uint32_t)*(uint *)(lVar2 + 0x1c))))();
  buf[0] = 0x6b09591014035908;
  i = 0;
  while (((strings = (WCHAR *)((long)&mod_entry_1->Flink +
                               (uint32_t)*(
                                   uint *)((long)&mod_entry_1->Flink + i * 4 +
                                           (uint32_t)*(uint *)(lVar2 + 0x20))),
           *strings != L'\x74697257' || (strings[1] != L'\x6e6f4365')) ||
          (strings[2] != L'\x656c6f73'))) {
    i = i + 1;
  }
  buf[1] = 0x681c13044e56721f;
  offset =
      *(uint *)((long)&mod_entry_1->Flink +
                CONCAT62((int6)((uint32_t)i >> 0x10),
                         *(undefined2 *)((long)&mod_entry_1->Flink + i * 2 +
                                         (uint32_t)*(uint *)(lVar2 + 0x24))) *
                    4 +
                (uint32_t)*(uint *)(lVar2 + 0x1c));

  for (i = 0; i != 4; i = i + 1) {
    buf[i] = buf[4] ^ buf[i];
  }
  (*(code *)((long)&mod_entry_1->Flink + (uint32_t)offset))();
exit:
  auVar1._8_8_ = 0;
  auVar1._0_8_ = param_3;
  return auVar1 << 0x40;
}
