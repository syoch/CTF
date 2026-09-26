#include <stdbool.h>

typedef unsigned char undefined;

typedef unsigned char byte;
typedef unsigned char dwfenc;
typedef unsigned int dword;
typedef unsigned long qword;
typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned char undefined1;
typedef unsigned int undefined4;
typedef unsigned long undefined8;
typedef unsigned short ushort;
typedef unsigned short word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
  byte eh_frame_hdr_version;        // Exception Handler Frame Header Version
  dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
  dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception
                                             // Handler FDEs
  dwfenc eh_frame_table_encoding;            // Exception Handler Table Encoding
};

typedef struct NoteGnuPropertyElement_4 NoteGnuPropertyElement_4,
    *PNoteGnuPropertyElement_4;

struct NoteGnuPropertyElement_4 {
  dword prType;
  dword prDatasz;
  byte data[4];
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
  dword initial_loc; // Initial Location
  dword data_loc;    // Data location
};

typedef void _IO_lock_t;

typedef struct _IO_marker _IO_marker, *P_IO_marker;

typedef struct _IO_FILE _IO_FILE, *P_IO_FILE;

typedef long __off_t;

typedef long __off64_t;

typedef ulong size_t;

struct _IO_FILE {
  int _flags;
  char *_IO_read_ptr;
  char *_IO_read_end;
  char *_IO_read_base;
  char *_IO_write_base;
  char *_IO_write_ptr;
  char *_IO_write_end;
  char *_IO_buf_base;
  char *_IO_buf_end;
  char *_IO_save_base;
  char *_IO_backup_base;
  char *_IO_save_end;
  struct _IO_marker *_markers;
  struct _IO_FILE *_chain;
  int _fileno;
  int _flags2;
  __off_t _old_offset;
  ushort _cur_column;
  char _vtable_offset;
  char _shortbuf[1];
  _IO_lock_t *_lock;
  __off64_t _offset;
  void *__pad1;
  void *__pad2;
  void *__pad3;
  void *__pad4;
  size_t __pad5;
  int _mode;
  char _unused2[20];
};

struct _IO_marker {
  struct _IO_marker *_next;
  struct _IO_FILE *_sbuf;
  int _pos;
};

typedef struct _IO_FILE FILE;

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

struct evp_pkey_ctx_st {};

typedef enum Elf_ProgramHeaderType {
  PT_NULL = 0,
  PT_LOAD = 1,
  PT_DYNAMIC = 2,
  PT_INTERP = 3,
  PT_NOTE = 4,
  PT_SHLIB = 5,
  PT_PHDR = 6,
  PT_TLS = 7,
  PT_GNU_EH_FRAME = 1685382480,
  PT_GNU_STACK = 1685382481,
  PT_GNU_RELRO = 1685382482
} Elf_ProgramHeaderType;

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
  SHT_NULL = 0,
  SHT_PROGBITS = 1,
  SHT_SYMTAB = 2,
  SHT_STRTAB = 3,
  SHT_RELA = 4,
  SHT_HASH = 5,
  SHT_DYNAMIC = 6,
  SHT_NOTE = 7,
  SHT_NOBITS = 8,
  SHT_REL = 9,
  SHT_SHLIB = 10,
  SHT_DYNSYM = 11,
  SHT_INIT_ARRAY = 14,
  SHT_FINI_ARRAY = 15,
  SHT_PREINIT_ARRAY = 16,
  SHT_GROUP = 17,
  SHT_SYMTAB_SHNDX = 18,
  SHT_ANDROID_REL = 1610612737,
  SHT_ANDROID_RELA = 1610612738,
  SHT_GNU_ATTRIBUTES = 1879048181,
  SHT_GNU_HASH = 1879048182,
  SHT_GNU_LIBLIST = 1879048183,
  SHT_CHECKSUM = 1879048184,
  SHT_SUNW_move = 1879048186,
  SHT_SUNW_COMDAT = 1879048187,
  SHT_SUNW_syminfo = 1879048188,
  SHT_GNU_verdef = 1879048189,
  SHT_GNU_verneed = 1879048190,
  SHT_GNU_versym = 1879048191
} Elf_SectionHeaderType;

struct Elf64_Shdr {
  dword sh_name;
  enum Elf_SectionHeaderType sh_type;
  qword sh_flags;
  qword sh_addr;
  qword sh_offset;
  qword sh_size;
  dword sh_link;
  dword sh_info;
  qword sh_addralign;
  qword sh_entsize;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

typedef enum Elf64_DynTag {
  DT_NULL = 0,
  DT_NEEDED = 1,
  DT_PLTRELSZ = 2,
  DT_PLTGOT = 3,
  DT_HASH = 4,
  DT_STRTAB = 5,
  DT_SYMTAB = 6,
  DT_RELA = 7,
  DT_RELASZ = 8,
  DT_RELAENT = 9,
  DT_STRSZ = 10,
  DT_SYMENT = 11,
  DT_INIT = 12,
  DT_FINI = 13,
  DT_SONAME = 14,
  DT_RPATH = 15,
  DT_SYMBOLIC = 16,
  DT_REL = 17,
  DT_RELSZ = 18,
  DT_RELENT = 19,
  DT_PLTREL = 20,
  DT_DEBUG = 21,
  DT_TEXTREL = 22,
  DT_JMPREL = 23,
  DT_BIND_NOW = 24,
  DT_INIT_ARRAY = 25,
  DT_FINI_ARRAY = 26,
  DT_INIT_ARRAYSZ = 27,
  DT_FINI_ARRAYSZ = 28,
  DT_RUNPATH = 29,
  DT_FLAGS = 30,
  DT_PREINIT_ARRAY = 32,
  DT_PREINIT_ARRAYSZ = 33,
  DT_RELRSZ = 35,
  DT_RELR = 36,
  DT_RELRENT = 37,
  DT_ANDROID_REL = 1610612751,
  DT_ANDROID_RELSZ = 1610612752,
  DT_ANDROID_RELA = 1610612753,
  DT_ANDROID_RELASZ = 1610612754,
  DT_ANDROID_RELR = 1879040000,
  DT_ANDROID_RELRSZ = 1879040001,
  DT_ANDROID_RELRENT = 1879040003,
  DT_GNU_PRELINKED = 1879047669,
  DT_GNU_CONFLICTSZ = 1879047670,
  DT_GNU_LIBLISTSZ = 1879047671,
  DT_CHECKSUM = 1879047672,
  DT_PLTPADSZ = 1879047673,
  DT_MOVEENT = 1879047674,
  DT_MOVESZ = 1879047675,
  DT_FEATURE_1 = 1879047676,
  DT_POSFLAG_1 = 1879047677,
  DT_SYMINSZ = 1879047678,
  DT_SYMINENT = 1879047679,
  DT_GNU_XHASH = 1879047924,
  DT_GNU_HASH = 1879047925,
  DT_TLSDESC_PLT = 1879047926,
  DT_TLSDESC_GOT = 1879047927,
  DT_GNU_CONFLICT = 1879047928,
  DT_GNU_LIBLIST = 1879047929,
  DT_CONFIG = 1879047930,
  DT_DEPAUDIT = 1879047931,
  DT_AUDIT = 1879047932,
  DT_PLTPAD = 1879047933,
  DT_MOVETAB = 1879047934,
  DT_SYMINFO = 1879047935,
  DT_VERSYM = 1879048176,
  DT_RELACOUNT = 1879048185,
  DT_RELCOUNT = 1879048186,
  DT_FLAGS_1 = 1879048187,
  DT_VERDEF = 1879048188,
  DT_VERDEFNUM = 1879048189,
  DT_VERNEED = 1879048190,
  DT_VERNEEDNUM = 1879048191,
  DT_AUXILIARY = 2147483645,
  DT_FILTER = 2147483647
} Elf64_DynTag;

struct Elf64_Dyn {
  enum Elf64_DynTag d_tag;
  qword d_val;
};

typedef struct GnuBuildId GnuBuildId, *PGnuBuildId;

struct GnuBuildId {
  dword namesz; // Length of name field
  dword descsz; // Length of description field
  dword type;   // Vendor specific type
  char name[4]; // Vendor name
  byte hash[20];
};

typedef struct NoteGnuProperty_4 NoteGnuProperty_4, *PNoteGnuProperty_4;

struct NoteGnuProperty_4 {
  dword namesz; // Length of name field
  dword descsz; // Length of description field
  dword type;   // Vendor specific type
  char name[4]; // Vendor name
};

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

struct Elf64_Phdr {
  enum Elf_ProgramHeaderType p_type;
  dword p_flags;
  qword p_offset;
  qword p_vaddr;
  qword p_paddr;
  qword p_filesz;
  qword p_memsz;
  qword p_align;
};

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
  qword r_offset; // location to apply the relocation action
  qword r_info;   // the symbol table index and the type of relocation
  qword
      r_addend; // a constant addend used to compute the relocatable field value
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
  byte e_ident_magic_num;
  char e_ident_magic_str[3];
  byte e_ident_class;
  byte e_ident_data;
  byte e_ident_version;
  byte e_ident_osabi;
  byte e_ident_abiversion;
  byte e_ident_pad[7];
  word e_type;
  word e_machine;
  dword e_version;
  qword e_entry;
  qword e_phoff;
  qword e_shoff;
  dword e_flags;
  word e_ehsize;
  word e_phentsize;
  word e_phnum;
  word e_shentsize;
  word e_shnum;
  word e_shstrndx;
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
  dword st_name;
  byte st_info;
  byte st_other;
  word st_shndx;
  qword st_value;
  qword st_size;
};

typedef uint uint32_t;

undefined *PTR_LOOP_00104000;
dword fde_001022a0;
undefined DAT_001040e0;
int (*machine[33])(char);
uint32_t code[33];

// WARNING: Unknown calling convention -- yet parameter storage is locked
int prctl(int __option, ...)

{
  int iVar1;

  iVar1 = prctl(__option);
  return iVar1;
}

// WARNING: Removing unreachable block (ram,0x001010e3)
// WARNING: Removing unreachable block (ram,0x001010ef)

void FUN_001010d0(void)

{
  return;
}

// WARNING: Removing unreachable block (ram,0x00101124)
// WARNING: Removing unreachable block (ram,0x00101130)

void FUN_00101100(void)

{
  return;
}

// WARNING: Removing unreachable block (ram,0x001011d0)

bool FUN_001011d5(char param_1)

{
  return param_1 == 'a';
}

bool FUN_001011f2(char param_1)

{
  return param_1 == 'b';
}

bool FUN_0010120f(char param_1)

{
  return param_1 == 'c';
}

bool FUN_0010122c(char param_1)

{
  return param_1 == 'd';
}

bool FUN_00101249(char param_1)

{
  return param_1 == 'e';
}

bool FUN_00101266(char param_1)

{
  return param_1 == 'f';
}

bool FUN_00101283(char param_1)

{
  return param_1 == 'g';
}

bool FUN_001012a0(char param_1)

{
  return param_1 == 'h';
}

bool FUN_001012bd(char param_1)

{
  return param_1 == 'i';
}

bool FUN_001012da(char param_1)

{
  return param_1 == 'j';
}

bool FUN_001012f7(char param_1)

{
  return param_1 == 'k';
}

bool FUN_00101314(char param_1)

{
  return param_1 == 'l';
}

bool FUN_00101331(char param_1)

{
  return param_1 == 'm';
}

bool FUN_0010134e(char param_1)

{
  return param_1 == 'n';
}

bool FUN_0010136b(char param_1)

{
  return param_1 == 'o';
}

bool FUN_00101388(char param_1)

{
  return param_1 == 'p';
}

bool FUN_001013a5(char param_1)

{
  return param_1 == 'q';
}

bool FUN_001013c2(char param_1)

{
  return param_1 == 'r';
}

bool FUN_001013df(char param_1)

{
  return param_1 == 's';
}

bool FUN_001013fc(char param_1)

{
  return param_1 == 't';
}

bool FUN_00101419(char param_1)

{
  return param_1 == 'u';
}

bool FUN_00101436(char param_1)

{
  return param_1 == 'v';
}

bool FUN_00101453(char param_1)

{
  return param_1 == 'w';
}

bool FUN_00101470(char param_1)

{
  return param_1 == 'x';
}

bool FUN_0010148d(char param_1)

{
  return param_1 == 'y';
}

bool FUN_001014aa(char param_1)

{
  return param_1 == 'z';
}

bool FUN_001014c7(char param_1)

{
  return param_1 == 'A';
}

bool FUN_001014e4(char param_1)

{
  return param_1 == 'B';
}

bool FUN_00101501(char param_1)

{
  return param_1 == 'C';
}

bool FUN_0010151e(char param_1)

{
  return param_1 == 'D';
}

bool FUN_0010153b(char param_1)

{
  return param_1 == 'E';
}

bool FUN_00101558(char param_1)

{
  return param_1 == 'F';
}

bool FUN_00101575(char param_1)

{
  return param_1 == 'G';
}

bool FUN_00101592(char param_1)

{
  return param_1 == 'H';
}

bool FUN_001015af(char param_1)

{
  return param_1 == 'I';
}

bool FUN_001015cc(char param_1)

{
  return param_1 == 'J';
}

bool FUN_001015e9(char param_1)

{
  return param_1 == 'K';
}

bool FUN_00101606(char param_1)

{
  return param_1 == 'L';
}

bool FUN_00101623(char param_1)

{
  return param_1 == 'M';
}

bool FUN_00101640(char param_1)

{
  return param_1 == 'N';
}

bool FUN_0010165d(char param_1)

{
  return param_1 == 'O';
}

bool FUN_0010167a(char param_1)

{
  return param_1 == 'P';
}

bool FUN_00101697(char param_1)

{
  return param_1 == 'Q';
}

bool FUN_001016b4(char param_1)

{
  return param_1 == 'R';
}

bool FUN_001016d1(char param_1)

{
  return param_1 == 'S';
}

bool FUN_001016ee(char param_1)

{
  return param_1 == 'T';
}

bool FUN_0010170b(char param_1)

{
  return param_1 == 'U';
}

bool FUN_00101728(char param_1)

{
  return param_1 == 'V';
}

bool FUN_00101745(char param_1)

{
  return param_1 == 'W';
}

bool FUN_00101762(char param_1)

{
  return param_1 == 'X';
}

bool FUN_0010177f(char param_1)

{
  return param_1 == 'Y';
}

bool FUN_0010179c(char param_1)

{
  return param_1 == 'Z';
}

bool FUN_001017b9(char param_1)

{
  return param_1 == '0';
}

bool FUN_001017d6(char param_1)

{
  return param_1 == '1';
}

bool FUN_001017f3(char param_1)

{
  return param_1 == '2';
}

bool FUN_00101810(char param_1)

{
  return param_1 == '3';
}

bool FUN_0010182d(char param_1)

{
  return param_1 == '4';
}

bool FUN_0010184a(char param_1)

{
  return param_1 == '5';
}

bool FUN_00101867(char param_1)

{
  return param_1 == '6';
}

bool FUN_00101884(char param_1)

{
  return param_1 == '7';
}

bool FUN_001018a1(char param_1)

{
  return param_1 == '8';
}

bool FUN_001018be(char param_1)

{
  return param_1 == '9';
}

bool FUN_001018db(char param_1)

{
  return param_1 == '_';
}

bool FUN_001018f8(char param_1)

{
  return param_1 == '{';
}

bool FUN_00101915(char param_1)

{
  return param_1 == '}';
}

#include <stdio.h>
#include <unistd.h>

void FUN_00101932(int param_1)

{
  undefined4 i;

  for (i = 0; i < param_1; i = i + 1) {
    putchar(0x2a);
    fflush((FILE *)0x0);
    sleep(1);
  }
  putchar(10);
  return;
}

undefined8 main(int param_1, char **argv)

{
  int iVar1;
  undefined8 uVar2;
  int local_10;
  int i;

  prctl(0x59616d61, 0xffffffffffffffff, 0, 0, 0);
  if (param_1 == 2) {
    for (local_10 = 0; local_10 < 0x20; local_10 = local_10 + 1) {
      putchar(0x3d);
      fflush((FILE *)0x0);
    }
    puts("v");
    for (i = 0; i < 0x21; i = i + 1) {
      sleep(1);
      iVar1 = machine[(int)code[i]]((int)argv[1][i]);
      if (iVar1 == 0) {
        FUN_00101932(0x21 - i);
        puts("Incorrect");
        return 1;
      }
      putchar(0x2a);
      fflush((FILE *)0x0);
    }
    sleep(1);
    if (argv[1][0x21] == '\0') {
      puts("\nCorrect");
      uVar2 = 0;
    } else {
      puts("\nIncorrect");
      uVar2 = 1;
    }
  } else {
    printf("Usage: %s <flag>\n", *argv);
    uVar2 = 1;
  }
  return uVar2;
}

undefined8 _fini(void)

{
  undefined8 in_RAX;

  return in_RAX;
}
