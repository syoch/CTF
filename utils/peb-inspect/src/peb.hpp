#pragma once

#include <windows.h>
#include <winternl.h>

typedef NTSTATUS(WINAPI *KERNEL_CALLBACK_PROC)(
    void *, ULONG); /* FIXME: not the correct name */

typedef struct {
  UINT next;
  UINT id;
  ULONGLONG addr;
  ULONGLONG size;
  UINT args[4];
} CROSS_PROCESS_WORK_ENTRY;

typedef union {
  struct _ {
    UINT first;
    UINT counter;
  };
  volatile LONGLONG hdr;
} CROSS_PROCESS_WORK_HDR;

typedef struct {
  CROSS_PROCESS_WORK_HDR free_list;
  CROSS_PROCESS_WORK_HDR work_list;
  ULONGLONG unknown[4];
  CROSS_PROCESS_WORK_ENTRY entries[1];
} CROSS_PROCESS_WORK_LIST;

typedef struct _CHPEV2_PROCESS_INFO {
  ULONG Wow64ExecuteFlags;                       /* 000 */
  USHORT NativeMachineType;                      /* 004 */
  USHORT EmulatedMachineType;                    /* 006 */
  HANDLE SectionHandle;                          /* 008 */
  CROSS_PROCESS_WORK_LIST *CrossProcessWorkList; /* 010 */
  void *unknown;                                 /* 018 */
} CHPEV2_PROCESS_INFO, *PCHPEV2_PROCESS_INFO;

typedef struct tagRTL_BITMAP {
  ULONG SizeOfBitMap; /* Number of bits in the bitmap */
  PULONG Buffer;      /* Bitmap data, assumed sized to a DWORD boundary */
} RTL_BITMAP, *PRTL_BITMAP;

typedef struct _CURDIR {
  UNICODE_STRING DosPath;
  PVOID Handle;
} CURDIR, *PCURDIR;

typedef struct {
  USHORT Flags;
  USHORT Length;
  ULONG TimeStamp;
  UNICODE_STRING DosPath;
} RTL_DRIVE_LETTER_CURDIR, *PRTL_DRIVE_LETTER_CURDIR;

typedef struct {
  ULONG AllocationSize;
  ULONG Size;
  ULONG Flags;
  ULONG DebugFlags;
  HANDLE ConsoleHandle;
  ULONG ConsoleFlags;
  HANDLE hStdInput;
  HANDLE hStdOutput;
  HANDLE hStdError;
  CURDIR CurrentDirectory;
  UNICODE_STRING DllPath;
  UNICODE_STRING ImagePathName;
  UNICODE_STRING CommandLine;
  PWSTR Environment;
  ULONG dwX;
  ULONG dwY;
  ULONG dwXSize;
  ULONG dwYSize;
  ULONG dwXCountChars;
  ULONG dwYCountChars;
  ULONG dwFillAttribute;
  ULONG dwFlags;
  ULONG wShowWindow;
  UNICODE_STRING WindowTitle;
  UNICODE_STRING Desktop;
  UNICODE_STRING ShellInfo;
  UNICODE_STRING RuntimeInfo;
  RTL_DRIVE_LETTER_CURDIR DLCurrentDirectory[0x20];
  ULONG_PTR EnvironmentSize;
  ULONG_PTR EnvironmentVersion;
  PVOID PackageDependencyData;
  ULONG ProcessGroupId;
  ULONG LoaderThreads;
} RTL_USER_PROCESS_PARAMETERS_WINE;

typedef struct {                    /* win32/win64 */
  BOOLEAN InheritedAddressSpace;    /* 000/000 */
  BOOLEAN ReadImageFileExecOptions; /* 001/001 */
  BOOLEAN BeingDebugged;            /* 002/002 */
  UCHAR ImageUsedLargePages : 1;    /* 003/003 */
  UCHAR IsProtectedProcess : 1;
  UCHAR IsImageDynamicallyRelocated : 1;
  UCHAR SkipPatchingUser32Forwarders : 1;
  UCHAR IsPackagedProcess : 1;
  UCHAR IsAppContainer : 1;
  UCHAR IsProtectedProcessLight : 1;
  UCHAR IsLongPathAwareProcess : 1;
  HANDLE Mutant;                                       /* 004/008 */
  HMODULE ImageBaseAddress;                            /* 008/010 */
  PEB_LDR_DATA *LdrData;                               /* 00c/018 */
  RTL_USER_PROCESS_PARAMETERS_WINE *ProcessParameters; /* 010/020 */
  void *SubSystemData;                                 /* 014/028 */
  HANDLE ProcessHeap;                                  /* 018/030 */
  RTL_CRITICAL_SECTION *FastPebLock;                   /* 01c/038 */
  void *AtlThunkSListPtr;                              /* 020/040 */
  void *IFEOKey;                                       /* 024/048 */
  ULONG ProcessInJob : 1;                              /* 028/050 */
  ULONG ProcessInitializing : 1;
  ULONG ProcessUsingVEH : 1;
  ULONG ProcessUsingVCH : 1;
  ULONG ProcessUsingFTH : 1;
  ULONG ProcessPreviouslyThrottled : 1;
  ULONG ProcessCurrentlyThrottled : 1;
  ULONG ProcessImagesHotPatched : 1;
  ULONG ReservedBits0 : 24;
  KERNEL_CALLBACK_PROC *KernelCallbackTable; /* 02c/058 */
  ULONG Reserved;                            /* 030/060 */
  ULONG AtlThunkSListPtr32;                  /* 034/064 */
  void *ApiSetMap;                           /* 038/068 */
  ULONG TlsExpansionCounter;                 /* 03c/070 */
  RTL_BITMAP *TlsBitmap;                     /* 040/078 */
  ULONG TlsBitmapBits[2];                    /* 044/080 */
  void *ReadOnlySharedMemoryBase;            /* 04c/088 */
  void *SharedData;                          /* 050/090 */
  void **ReadOnlyStaticServerData;           /* 054/098 */
  void *AnsiCodePageData;                    /* 058/0a0 */
  void *OemCodePageData;                     /* 05c/0a8 */
  void *UnicodeCaseTableData;                /* 060/0b0 */
  ULONG NumberOfProcessors;                  /* 064/0b8 */
  ULONG NtGlobalFlag;                        /* 068/0bc */
  LARGE_INTEGER CriticalSectionTimeout;      /* 070/0c0 */
  SIZE_T HeapSegmentReserve;                 /* 078/0c8 */
  SIZE_T HeapSegmentCommit;                  /* 07c/0d0 */
  SIZE_T HeapDeCommitTotalFreeThreshold;     /* 080/0d8 */
  SIZE_T HeapDeCommitFreeBlockThreshold;     /* 084/0e0 */
  ULONG NumberOfHeaps;                       /* 088/0e8 */
  ULONG MaximumNumberOfHeaps;                /* 08c/0ec */
  void **ProcessHeaps;                       /* 090/0f0 */
  void *GdiSharedHandleTable;                /* 094/0f8 */
  void *ProcessStarterHelper;                /* 098/100 */
  void *GdiDCAttributeList;                  /* 09c/108 */
  void *LoaderLock;                          /* 0a0/110 */
  ULONG OSMajorVersion;                      /* 0a4/118 */
  ULONG OSMinorVersion;                      /* 0a8/11c */
  ULONG OSBuildNumber;                       /* 0ac/120 */
  ULONG OSPlatformId;                        /* 0b0/124 */
  ULONG ImageSubSystem;                      /* 0b4/128 */
  ULONG ImageSubSystemMajorVersion;          /* 0b8/12c */
  ULONG ImageSubSystemMinorVersion;          /* 0bc/130 */
  KAFFINITY ActiveProcessAffinityMask;       /* 0c0/138 */
#ifdef _WIN64
  ULONG GdiHandleBuffer[60]; /*    /140 */
#else
  ULONG GdiHandleBuffer[34]; /* 0c4/    */
#endif
  void *PostProcessInitRoutine;      /* 14c/230 */
  RTL_BITMAP *TlsExpansionBitmap;    /* 150/238 */
  ULONG TlsExpansionBitmapBits[32];  /* 154/240 */
  ULONG SessionId;                   /* 1d4/2c0 */
  ULARGE_INTEGER AppCompatFlags;     /* 1d8/2c8 */
  ULARGE_INTEGER AppCompatFlagsUser; /* 1e0/2d0 */
  void *ShimData;                    /* 1e8/2d8 */
  void *AppCompatInfo;               /* 1ec/2e0 */
  UNICODE_STRING CSDVersion;         /* 1f0/2e8 */
  void *ActivationContextData;       /* 1f8/2f8 */
  void *ProcessAssemblyStorageMap;   /* 1fc/300 */
  void *SystemDefaultActivationData; /* 200/308 */
  void *SystemAssemblyStorageMap;    /* 204/310 */
  SIZE_T MinimumStackCommit;         /* 208/318 */
  void **FlsCallback;                /* 20c/320 */
  LIST_ENTRY FlsListHead;            /* 210/328 */
  union {
    RTL_BITMAP *FlsBitmap; /* 218/338 */
#ifdef _WIN64
    CHPEV2_PROCESS_INFO *ChpeV2ProcessInfo; /*    /338 */
#endif
  };
  ULONG FlsBitmapBits[4];       /* 21c/340 */
  ULONG FlsHighIndex;           /* 22c/350 */
  void *WerRegistrationData;    /* 230/358 */
  void *WerShipAssertPtr;       /* 234/360 */
  void *EcCodeBitMap;           /* 238/368 */
  void *pImageHeaderHash;       /* 23c/370 */
  ULONG HeapTracingEnabled : 1; /* 240/378 */
  ULONG CritSecTracingEnabled : 1;
  ULONG LibLoaderTracingEnabled : 1;
  ULONG SpareTracingBits : 29;
  ULONGLONG CsrServerReadOnlySharedMemoryBase;  /* 248/380 */
  ULONG TppWorkerpListLock;                     /* 250/388 */
  LIST_ENTRY TppWorkerpList;                    /* 254/390 */
  void *WaitOnAddressHashTable[0x80];           /* 25c/3a0 */
  void *TelemetryCoverageHeader;                /* 45c/7a0 */
  ULONG CloudFileFlags;                         /* 460/7a8 */
  ULONG CloudFileDiagFlags;                     /* 464/7ac */
  CHAR PlaceholderCompatibilityMode;            /* 468/7b0 */
  CHAR PlaceholderCompatibilityModeReserved[7]; /* 469/7b1 */
  void *LeapSecondData;                         /* 470/7b8 */
  ULONG LeapSecondFlags;                        /* 474/7c0 */
  ULONG NtGlobalFlag2;                          /* 478/7c4 */
} PEB_WINE;