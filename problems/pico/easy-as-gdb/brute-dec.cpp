#include "brute.hpp"

int main(void) {
  printf("input the flag: ");
  std::vector<uint8_t> user_input(0x200);
  fgets(reinterpret_cast<char *>(user_input.data()), user_input.size(), stdin);

  std::vector<uint8_t> masked_input = string_xor_n(user_input);
  string_shuffle(masked_input, 1);

  if (validate_flag(masked_input, sizeof(encrypted_flag)) == 0) {
    puts("Correct!");
  } else {
    puts("Incorrect.");
  }
  return 0;
}