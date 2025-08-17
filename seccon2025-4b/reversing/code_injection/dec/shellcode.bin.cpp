#define "SteG" 0x53746547
#define "aHdt" 0x61486474
#define "eldn" 0x656c646e

typedef unsigned char undefined;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned char undefined1;
typedef unsigned int undefined4;
typedef unsigned long undefined8;
typedef unsigned short ushort;
typedef unsigned short wchar16;
typedef unsigned int wchar32;
typedef struct LDR_MODULE LDR_MODULE, *PLDR_MODULE;
typedef struct PEB PEB, *PPEB;
typedef uchar uint8_t;
typedef struct _LIST_ENTRY _LIST_ENTRY, *P_LIST_ENTRY;
typedef struct _LIST_ENTRY LIST_ENTRY;
typedef struct _LSA_UNICODE_STRING _LSA_UNICODE_STRING, *P_LSA_UNICODE_STRING;
typedef struct _LSA_UNICODE_STRING LSA_UNICODE_STRING;
typedef LSA_UNICODE_STRING UNICODE_STRING;
typedef ushort USHORT;
typedef wchar_t *PWSTR;
typedef wchar_t *LPWSTR;
typedef uint uint32_t;

struct LDR_MODULE {};

struct _LSA_UNICODE_STRING {
  USHORT Length;
  USHORT MaximumLength;
  PWSTR Buffer;
};

struct RTL_USER_PROCESS_PARAMETERS {
  uint8_t field0_0x0[16];
  void *field1_0x10[10];
  UNICODE_STRING ImagePathName;
  UNICODE_STRING Cmdline;
  wchar16 **envp;
};

struct _LIST_ENTRY {
  struct _LIST_ENTRY *Flink;
  struct _LIST_ENTRY *Blink;
};

struct PEB_LDR_DATA {
  uint8_t res0[8];
  void *res1[3];
  LIST_ENTRY InMemoryOrderModuleList;
};

struct PEB {
  uint8_t field0_0x0[2];
  uint8_t begingDebugged;
  uint8_t field2_0x3[21];
  struct PEB_LDR_DATA *LoaderData;
  struct RTL_USER_PROCESS_PARAMETERS *ProcessParameters;
  uint8_t field5_0x28[520];
};

struct GS {
  uint8_t field0_0x0[96];
  struct PEB *peb;
  undefined field2_0x68;
  undefined field3_0x69;
  undefined field4_0x6a;
  undefined field5_0x6b;
  undefined field6_0x6c;
  undefined field7_0x6d;
  undefined field8_0x6e;
  undefined field9_0x6f;
  undefined field10_0x70;
  undefined field11_0x71;
  undefined field12_0x72;
  undefined field13_0x73;
  undefined field14_0x74;
  undefined field15_0x75;
  undefined field16_0x76;
  undefined field17_0x77;
  undefined field18_0x78;
  undefined field19_0x79;
  undefined field20_0x7a;
  undefined field21_0x7b;
  undefined field22_0x7c;
  undefined field23_0x7d;
  undefined field24_0x7e;
  undefined field25_0x7f;
  undefined field26_0x80;
  undefined field27_0x81;
  undefined field28_0x82;
  undefined field29_0x83;
  undefined field30_0x84;
  undefined field31_0x85;
  undefined field32_0x86;
  undefined field33_0x87;
};

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void entry(void)

{
  LIST_ENTRY *pLVar1;
  LIST_ENTRY *pLVar2;
  undefined8 handle;
  longlong i;
  int *t2;
  wchar16 *envp;
  GS *gs;
  ulonglong flag[6];
  uint32_t *mod1;
  uint offset;

  /* Finding 'CTF4B=1' in envp */
  envp = (wchar16 *)gs->peb->ProcessParameters->envp;
  while (true) {
    if (*(int *)envp == 0) {
      return;
    }
    if ((((*(int *)envp == 0x540043) &&
          (*(int *)((longlong)envp + 4) == 0x340046)) &&
         (*(int *)((longlong)envp + 8) == 0x3d0042)) &&
        (*(int *)((longlong)envp + 0xc) == 0x31))
      break;
    envp = (wchar16 *)((longlong)envp + 2);
  }
  pLVar1 = (gs->peb->Ldr->InMemoryOrderModuleList->list).Flink;
  pLVar2 = pLVar1->Flink;
  flag[4] =
      (ulonglong)((pLVar2[5].Flink)->Flink +
                  (((ulonglong)(pLVar1[5].Flink)->Flink | 0x20002000200020) ^
                   (ulonglong) * (wchar16 **)envp) *
                      0x10) |
      0x20002000200020;
  mod1 = (uint32_t *)pLVar2[2].Flink;
  offset = *(uint *)((longlong)mod1 + (ulonglong)mod1[0xf] + 0x88);
  flag[2] = 0x2a087d454e564005;
  /* Finding 'GetStdHandle' (12B) */
  i = 0;
  while (((t2 = (int *)((longlong)mod1 +
                        (ulonglong) *
                            (uint *)((longlong)mod1 + i * 4 +
                                     (ulonglong) *
                                         (uint *)((longlong)mod1 +
                                                  (ulonglong)offset + 0x20))),
           *t2 != 0x53746547 || (t2[1] != 0x61486474)) ||
          (t2[2] != 0x656c646e))) {
    i = i + 1;
  }
  flag[3] = 0x52134041503a405b;
  handle = (*(
      code *)((longlong)mod1 +
              (ulonglong) *
                  (uint *)((longlong)mod1 +
                           CONCAT62(
                               (int6)((ulonglong)i >> 0x10),
                               *(undefined2 *)((longlong)mod1 + i * 2 +
                                               (ulonglong) *
                                                   (uint *)((longlong)mod1 +
                                                            (ulonglong)offset +
                                                            0x24))) *
                               4 +
                           (ulonglong) *
                               (uint *)((longlong)mod1 + (ulonglong)offset +
                                        0x1c))))();
  flag[0] = 0x6b09591014035908;
  /* Finding 'WriteConsole' */
  i = 0;
  while (((t2 = (int *)((longlong)mod1 +
                        (ulonglong) *
                            (uint *)((longlong)mod1 + i * 4 +
                                     (ulonglong) *
                                         (uint *)((longlong)mod1 +
                                                  (ulonglong)offset + 0x20))),
           *t2 != 0x74697257 || (t2[1] != 0x6e6f4365)) ||
          (t2[2] != 0x656c6f73))) {
    i = i + 1;
  }
  flag[1] = 0x681c13044e56721f;
  offset = *(uint *)((longlong)mod1 +
                     CONCAT62((int6)((ulonglong)i >> 0x10),
                              *(undefined2 *)((longlong)mod1 + i * 2 +
                                              (ulonglong) *
                                                  (uint *)((longlong)mod1 +
                                                           (ulonglong)offset +
                                                           0x24))) *
                         4 +
                     (ulonglong) *
                         (uint *)((longlong)mod1 + (ulonglong)offset + 0x1c));
  for (i = 0; i != 4; i = i + 1) {
    flag[i] = flag[4] ^ flag[i];
  }
  (*(code *)((longlong)mod1 + (ulonglong)offset))(handle, flag, 0x20, 0, 0);
  return;
}
