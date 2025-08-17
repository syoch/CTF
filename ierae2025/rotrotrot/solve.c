#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

uint FUN_001012db_reverse(char x) {
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

uint rot1_A_reverse(uint8_t x, uint8_t n) {
  return (uint)x << (8 - (n & 7) & 0x1f) | (int)(uint)x >> (n & 7);
}

uint rot1_B_reverse(uint8_t x, uint8_t n) {
  return (int)(uint)x >> (8 - (n & 7) & 0x1f) | (uint)x << (n & 7);
}

uint KeyFunc_1(uint param_1, uint8_t param_2) {
  return param_1 << (param_2 & 0x1f) | param_1 >> (0x20 - (param_2 & 0x1f));
}

uint KeyFunc_2(uint param_1, uint8_t param_2) {
  return param_1 >> (param_2 & 0x1f) | param_1 << (0x20 - (param_2 & 0x1f));
}

uint UpdateKey(int param_1) {
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

void decrypt_with_key(uint8_t *enc, uint8_t *raw, size_t raw_length,
                      uint init_key) {

  memcpy(raw, enc, raw_length);

  for (int i = 0, key = UpdateKey(init_key); i < raw_length; i++) {
    raw[i] = enc[i] ^ (uint8_t)key;
    key = UpdateKey(key);
  }

  ulong k = 0;
  for (int i = 0; i < raw_length; i += 8) {
    ulong uVar3 = raw_length - i;
    if (8 < uVar3) {
      uVar3 = 8;
    }
    k = k + 3;
    k = k + ((((k - (k / 7)) >> 1) + (k / 7)) >> 2) * -7 + 1;

    for (int j = 0; j < k; j++) {
      uint8_t uVar1 = raw[uVar3 + i - 1];
      for (int k = uVar3 - 1; k > 0; k--) {
        raw[i + k] = raw[k + i - 1];
      }
      raw[i] = uVar1;
    }
  }

  for (int i = 0, n = 0; i < raw_length; i++) {
    n = (n + 4) % 7 + 1;

    if ((i & 1) == 0) {
      raw[i] = rot1_A_reverse(raw[i], n);
    } else {
      raw[i] = rot1_B_reverse(raw[i], n);
    }
  }

  for (int i = 0; i < raw_length; i++) {
    raw[i] = FUN_001012db_reverse(raw[i]);
  }
}

int is_printable(uint8_t *data, size_t len) {
  for (int i = 0; i < len; i++) {
    if (data[i] < 32 || data[i] > 126) {
      if (data[i] != '\n' && data[i] != '\r' && data[i] != '\t') {
        return 0;
      }
    }
  }
  return 1;
}

void decrypt(uint8_t *enc, uint8_t *raw, size_t raw_length) {
  uint init_key = 0;
  char *prefix = "IERAE";

  for (int i = 0; i < 4; i++) {
    init_key |= prefix[i] << ((i << 3) & 0x1f);
  }

  uint8_t *temp = malloc(raw_length);
  decrypt_with_key(enc, temp, raw_length, init_key);

  if (is_printable(temp, raw_length)) {
    memcpy(raw, temp, raw_length);
    free(temp);
    return;
  }

  printf("Trying brute force...\n");
  for (uint32_t key = 0; key < 0x1000000; key++) {
    if (key % 0x100000 == 0) {
      printf("Trying key: 0x%08x\n", key);
    }

    decrypt_with_key(enc, temp, raw_length, key);

    if (is_printable(temp, raw_length)) {
      printf("Found match with key 0x%08x\n", key);
      memcpy(raw, temp, raw_length);
      return;
    }
  }

  decrypt_with_key(enc, raw, raw_length, 0);
}

int main(int argc, char **argv) {
  if (argc != 3) {
    fprintf(stderr, "Usage: %s <encrypted_input> <decrypted_output>\n",
            argv[0]);
    return 1;
  }

  char *input_fname = argv[1];
  char *output_fname = argv[2];
  FILE *fp = fopen(input_fname, "rb");
  if (fp == NULL) {
    fprintf(stderr, "Failed to open input file: %s\n", input_fname);
    return 1;
  }

  fseek(fp, 0, SEEK_END);
  int64_t fsize = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  uint8_t *input_data = malloc(fsize + 1);
  if (input_data == NULL) {
    fprintf(stderr, "Failed to allocate memory\n");
    fclose(fp);
    return 1;
  }

  int64_t read_bytes = fread(input_data, 1, fsize, fp);
  if (read_bytes != fsize) {
    fprintf(stderr, "Failed to read input file: read %zu bytes, expected %zu\n",
            read_bytes, fsize);
    fclose(fp);
    free(input_data);
    return 1;
  }

  fclose(fp);

  uint8_t *decrypted_data = malloc(fsize + 1);
  if (decrypted_data == NULL) {
    fprintf(stderr, "Failed to allocate memory\n");
    free(input_data);
    return 1;
  }

  decrypt(input_data, decrypted_data, fsize);

  int64_t real_size = fsize;
  while (real_size > 0 && decrypted_data[real_size - 1] == ' ') {
    real_size--;
  }

  decrypted_data[real_size] = '\0';

  FILE *output_fp = fopen(output_fname, "wb");
  if (output_fp == NULL) {
    fprintf(stderr, "Failed to open output file: %s\n", output_fname);
    free(input_data);
    free(decrypted_data);
    return 1;
  }

  fwrite(decrypted_data, 1, real_size, output_fp);
  fclose(output_fp);

  free(input_data);
  free(decrypted_data);

  printf("Decryption completed. Output written to %s\n", output_fname);
  return 0;
}
