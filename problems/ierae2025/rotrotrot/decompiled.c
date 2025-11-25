#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
int64_t g1 = 0; // 0x4020
char g2 = 0;    // 0x4028
int32_t g3;

uint FUN_001012db(char x) {
  uint ret;

  if (((x < 'a') || ('m' < x)) && ((x < 'A' || ('M' < x)))) {
    if (((x < 'n') || ('z' < x)) && ((x < 'N' || ('Z' < x)))) {
      return (uint)x;
    } else {
      return x - 0xd;
    }
  } else {
    return x + 0xd;
  }
}

uint rot1_A(uint8_t x, uint8_t n)

{
  return (int)(uint)x >> (8 - (n & 7) & 0x1f) | (uint)x << (n & 7);
}

uint rot1_B(uint8_t x, uint8_t n)

{
  return (uint)x << (8 - (n & 7) & 0x1f) | (int)(uint)x >> (n & 7);
}

uint KeyFunc_1(uint param_1, uint8_t param_2)

{
  return param_1 << (param_2 & 0x1f) | param_1 >> 0x20 - (param_2 & 0x1f);
}

uint KeyFunc_2(uint param_1, uint8_t param_2)

{
  return param_1 >> (param_2 & 0x1f) | param_1 << 0x20 - (param_2 & 0x1f);
}

uint UpdateKey(int param_1)

{
  uint uVar1;
  uint uVar2;

  uVar1 = KeyFunc_1(param_1 * -0x179fefe9, 0xd);
  uVar1 = (param_1 * -0x179fefe9 ^ uVar1) * -0x655bab11;
  uVar2 = KeyFunc_2(uVar1, 5);
  uVar1 = (uVar1 ^ uVar2) * -0x56b23731;
  uVar2 = KeyFunc_1(uVar1, 0x18);
  uVar1 = (uVar1 ^ uVar2) * -0x25be3b7a;
  uVar2 = KeyFunc_2(uVar1, 0x11);
  return uVar1 ^ uVar2;
}

void encrypt(char *raw, char *enc) {
  size_t raw_length;
  uint init_key;
  ulong local_48;

  raw_length = strlen(raw);
  for (int i = 0, n = 0; i < raw_length; i = i + 1) {
    char x = FUN_001012db((int)raw[i]);
    n = (n + 4) % 7 + 1;

    enc[i] = (i & 1) == 0 ? rot1_A(x, n) : rot1_B(x, n);
  }
  local_48 = 0;
  for (int i = 0; i < raw_length; i = i + 8) {
    ulong uVar3 = raw_length - i;
    if (8 < uVar3) {
      uVar3 = 8;
    }
    local_48 = local_48 + 3;
    local_48 = local_48 +
               ((local_48 - local_48 / 7 >> 1) + local_48 / 7 >> 2) * -7 + 1;
    for (int j = 0; j < local_48; j = j + 1) {
      char uVar1 = enc[i];
      for (int k = 0; k < uVar3 - 1; k = k + 1) {
        enc[i + k] = enc[k + i + 1];
      }
      enc[uVar3 + i - 1] = uVar1;
    }
  }

  init_key = 0;
  for (int i = 0; i < 4; i = i + 1) {
    init_key = init_key | (uint)(uint8_t)raw[i]
                              << ((uint8_t)((int)i << 3) & 0x1f);
  }

  for (int i = 0, key = UpdateKey(init_key); i < raw_length; i = i + 1) {
    enc[i] = enc[i] ^ (uint8_t)key;
    key = UpdateKey(key);
  }
}

// Address range: 0x1693 - 0x19a0
int main(int argc, char **argv) {
  if ((int32_t)argc != 3) {
    fprintf(stderr, "Usage: %s <input> <output>\n", argv[0]);
    return 1;
  }

  char *input_fname = argv[1];
  char *output_fname = argv[2];
  FILE *fp = fopen(input_fname, "rb");
  if (fp == 0) {
    fprintf(stderr, "Failed to open input file: %s\n", input_fname);
    return 1;
  }

  fseek(fp, 0, 2);
  int64_t fsize = ftell(fp);
  fseek(fp, 0, 0);

  uint64_t size2 = -fsize % 8 + fsize;
  uint8_t *input_data = malloc(size2 + 1); // 0x17a1
  if (input_data == 0) {
    fwrite("Failed to allocate memory\n", 1, 26, stderr);
    fclose(fp);
    return 1;
  }

  int64_t read_uint8_ts = fread(input_data, 1, fsize, fp); // 0x17fe
  if (read_uint8_ts != fsize) {
    fprintf(stderr,
            "Failed to read input file: read %zu uint8_ts, expected %zu\n",
            read_uint8_ts, fsize);
    fclose(fp);
    free(input_data);
    return 1;
  }

  // Padding
  int64_t i = fsize; // 0x187b
  if (fsize < size2) {
    input_data[i++] = ' ';
    while (i != size2) {
      // 0x1860
      input_data[i++] = ' ';
    }
  }
  input_data[size2] = 0;

  fclose(fp);

  uint8_t *v9 = malloc(size2); // 0x189e
  if (v9 == 0) {
    // 0x18ae
    fwrite("Failed to allocate memory\n", 1, 26, stderr);
    free(input_data);
    // 0x199e
    return 1;
  }
  // 0x18e7
  encrypt(input_data, v9);
  FILE *v10 = fopen(output_fname, "wb"); // 0x190b
  int64_t result;                        // 0x1693
  if (v10 != NULL) {
    // 0x195c
    fwrite(v9, 1, size2, v10);
    fclose(v10);
    free(v9);
    free(input_data);
    result = 0;
  } else {
    // 0x191b
    fprintf(stderr, "Failed to open file: %s\n", output_fname);
    free(v9);
    free(input_data);
    result = 1;
  }
  // 0x199e
  return result;
}
