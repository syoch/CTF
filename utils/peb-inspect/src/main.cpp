#include "peb.hpp"
#include <cctype>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

bool memory_readable(void *ptr, size_t byteCount) {
  MEMORY_BASIC_INFORMATION mbi;
  if (VirtualQuery(ptr, &mbi, sizeof(MEMORY_BASIC_INFORMATION)) == 0)
    return false;

  if (mbi.State != MEM_COMMIT)
    return false;

  if (mbi.Protect == PAGE_NOACCESS || mbi.Protect == PAGE_EXECUTE)
    return false;

  // This checks that the start of memory block is in the same "region" as the
  // end. If it isn't you "simplify" the problem into checking that the rest of
  // the memory is readable.
  size_t blockOffset = (size_t)((char *)ptr - (char *)mbi.BaseAddress);
  size_t blockBytesPostPtr = mbi.RegionSize - blockOffset;

  if (blockBytesPostPtr < byteCount)
    return memory_readable((char *)ptr + blockBytesPostPtr,
                           byteCount - blockBytesPostPtr);

  return true;
}

void hex_dump(const void *addr, size_t size) {
  auto ptr = (uint8_t *)addr;

  while (ptr < (uint8_t *)addr + size) {
    const auto remaining_bytes = size - (ptr - (uint8_t *)addr);
    const auto printable_bytes =
        remaining_bytes < 0x10 ? remaining_bytes : 0x10;

    printf("|%016llx|", (uintptr_t)ptr);
    for (size_t i = 0; i < 0x10; ++i) {
      if (i < printable_bytes) {
        printf("%02x", ptr[i]);
      } else {
        printf("  ");
      }

      if (i % 4 == 3) {
        printf(" ");
      }
    }
    printf("| ");
    for (size_t i = 0; i < 0x10; ++i) {
      if (i < printable_bytes) {
        const auto byte = ptr[i];
        printf("%c", std::isprint(byte) ? byte : '.');
      } else {
        printf(" ");
      }

      if (i % 4 == 3) {
        printf(" ");
      }
    }
    printf("|\n");
    ptr += 0x10;
  }
}

int main() {
  auto peb_addr = (PEB_WINE *)__readgsqword(0x60);
  printf("PEB Address: %p\n", (void *)peb_addr);

  auto list_first = &peb_addr->LdrData->InMemoryOrderModuleList;

  printf("InMemoryOrderModuleList:\n");
  for (auto entry = list_first->Flink; entry != list_first;
       entry = entry->Flink) {
    auto e = (LDR_DATA_TABLE_ENTRY *)entry->Flink;
    if (e == nullptr) {
      std::cerr << "Error: Encountered null entry in list." << std::endl;
      continue;
    }

    const auto len = e->FullDllName.Length;
    const auto ptr = e->FullDllName.Buffer;
    if (ptr == nullptr) {
      std::wcout << L"  " << e << L": (null)" << std::endl;
    } else {
      const auto str = std::wstring(ptr, ptr + len / sizeof(wchar_t));
      std::wcout << L"  " << e << L": " << str << std::endl;
    }
  }

  return 0;
}
