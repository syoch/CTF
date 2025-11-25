#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char BYTE;
typedef unsigned int uint;
typedef unsigned long long ulonglong;
typedef long long longlong;
typedef int BOOL;
typedef unsigned long DWORD;
typedef void *HANDLE;
typedef void *LPSECURITY_ATTRIBUTES;
typedef void *LPOVERLAPPED;
typedef void *HCRYPTPROV;
typedef void *HCRYPTKEY;
typedef void *HCRYPTHASH;
typedef wchar_t WCHAR;
typedef const WCHAR *LPCWSTR;
typedef unsigned char undefined1;

void main(int argc, char **argv)

{
  uint uVar1;
  BOOL ret;
  DWORD flag_size;
  void *pvVar3;
  char *flag_data;
  BYTE *_Memory;
  ulonglong _Size;
  longlong enc_key_length;
  undefined1 auStackY_b8[32];
  HCRYPTKEY key_handle;
  HCRYPTPROV hash_ctx;

  DWORD read_bytes;
  DWORD write_bytes;
  HCRYPTHASH hash_handle;
  BYTE enc_key[24];
  ulonglong local_38;
  longlong i;
  longlong i3;

  local_38 = DAT_140005000 ^ (ulonglong)auStackY_b8;
  flag_data = (char *)0x0;
  HANDLE flag_handle =
      CreateFileA("flag.txt", 0x80000000, 1, (LPSECURITY_ATTRIBUTES)0x0, 3,
                  0x80, (HANDLE)0x0);
  if (flag_handle == (HANDLE)0xffffffffffffffff) {
    puts("Failed to handle flag.txt\n");
    goto exit_as_failure;
  }

  HANDLE flag_enc_handle =
      CreateFileA("flag.encrypted", 0x40000000, 0, (LPSECURITY_ATTRIBUTES)0x0,
                  2, 0x80, (HANDLE)0x0);
  if (flag_enc_handle == (HANDLE)0xffffffffffffffff) {
    puts("Failed to handle flag.encrypted\n");
    goto exit_as_failure;
  }

  ret = CryptAcquireContext(
      &hash_ctx, (LPCWSTR)0x0,
      L"Microsoft Enhanced RSA and AES Cryptographic Provider", 0x18, 0);
  if (ret == 0) {
    puts("CryptAcquireContext() Error\n");
    goto exit_as_failure;
  }

  ret = CryptCreateHash(hash_ctx, 0x800c, 0, 0, &hash_handle);
  if (ret == 0) {
    puts("CryptCreateHash() Error\n");
    goto exit_as_failure;
  }

  memcpy(enc_key, "ThisIsTheEncryptKey\0", 0x14);
  i = -1;
  do {
    enc_key_length = i + 1;
    i3 = i + 1;
    i = enc_key_length;
  } while (enc_key[i3] != '\0');

  ret = CryptHashData(hash_handle, enc_key, (DWORD)enc_key_length, 0);
  if (ret == 0) {
    puts("CryptHashData() Error\n");
    goto exit_as_failure;
  }
  ret = CryptDeriveKey(hash_ctx, 0x6610, hash_handle, 0x1000000, &key_handle);
  if (ret == 0) {
    puts("CryptDeriveKey() Error\n");
    goto exit_as_failure;
  }

  {
    BYTE key_param[4];
    key_param[0] = '\x01';
    key_param[1] = '\0';
    key_param[2] = '\0';
    key_param[3] = '\0';
    ret = CryptSetKeyParam(key_handle, 3, key_param, 0);
    if (ret == 0) {
      puts("CryptSeKeyParam() Error\n");
      goto exit_as_failure;
    }
  }

  ret = CryptSetKeyParam(key_handle, 1, (BYTE *)L"IVCanObfuscation", 0);
  if (ret == 0) {
    puts("CryptSeKeyParam() with IV Error\n");
    goto exit_as_failure;
  }

  {
    BYTE key_param[4];
    key_param[0] = '\x01';
    key_param[1] = '\0';
    key_param[2] = '\0';
    key_param[3] = '\0';
    ret = CryptSetKeyParam(key_handle, 4, key_param, 0);
    if (ret == 0) {
      puts("CryptSetKeyParam() with set MODE Error\n");
      goto exit_as_failure;
    }
  }

  flag_size = GetFileSize(flag_handle, (LPDWORD)0x0);
  uVar1 = flag_size + 0x10;
  _Size = (ulonglong)uVar1;
  if (uVar1 != 0) {
    flag_data = new char[_Size];
    memset(flag_data, 0, _Size);
  }

  read_bytes = 0;
  ret = ReadFile(flag_handle, flag_data, flag_size, &read_bytes,
                 (LPOVERLAPPED)0x0);
  if (ret == 0) {
    puts("ReadFile() Error\n");
    delete[] flag_data;
    return;
  }

  i = -1;
  do {
    i = i + 1;
  } while (((BYTE *)flag_data)[i] != '\0');
  write_bytes = (int)i + 1;
  ret =
      CryptEncrypt(key_handle, 0, 1, 0, (BYTE *)flag_data, &write_bytes, 0x40);
  if (ret == 0) {
    puts("CryptEncrypt() Error\n");
    delete[] flag_data;
  }

  ret = WriteFile(flag_enc_handle, flag_data, 0x40, (LPDWORD)0x0,
                  (LPOVERLAPPED)0x0);
  if (ret == 0) {
    puts("WriteFile() error\n");
    delete[] flag_data;
  }
  CloseHandle(flag_handle);
  CloseHandle(flag_enc_handle);

  ret = DeleteFileA("flag.txt");
  if (ret == 0) {
    puts("DeleteFileA() error\n");
    delete[] flag_data;
  }

  ret = CryptDestroyKey(key_handle);
  if (ret == 0) {
    puts("CryptDestroyKey() error\n");
    delete[] flag_data;
  }

  ret = CryptDestroyHash(hash_handle);
  if (ret == 0) {
    puts("CryptDestroyHash() error\n");
    delete[] flag_data;
  }

  ret = CryptReleaseContext(hash_ctx, 0);
  if (ret == 0) {
    puts("CryptReleaseContext() error\n");
  }

  return; // ADDED CODE

exit_as_failure:
  FUN_140001680(local_38 ^ (ulonglong)auStackY_b8);
  return;
}
