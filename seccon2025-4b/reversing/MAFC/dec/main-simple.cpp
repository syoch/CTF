#include <stdlib.h>

int main(int argc, char **argv) {
  //* flag_handle("flag.txt")

  //* flag_end_handle ("flag.encrypted")

  //* hash_handle <--- "ThisIsTheEncryptKey\0"
  //* aes256_key_handle <--- hash_handle (CryptoDeriveKey)

  //* flag_data <--- flag_fp
  //* flag_data <--- encrypt (aes256_key_handle flag_data)
  //* flag_enc_handle <--- flag_data

  return 0;
}
