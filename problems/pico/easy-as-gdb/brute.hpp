#include <cstdint>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

void string_gap_mirror(std::vector<uint8_t> &st, int skip) {
  for (size_t i = 0; i < (st.size() - skip) + 1U; i = i + skip) {
    auto tmp = st[i];
    st[i] = st[skip + i + -1];
    st[skip + i + -1] = tmp;
  }
  return;
}

void string_shuffle(std::vector<uint8_t> &st, int reverse_mode) {
  if (reverse_mode < 1) {
    for (uint32_t skip = st.size() - 1; skip > 0; skip = skip - 1) {
      string_gap_mirror(st, skip);
    }
  } else {
    for (uint32_t skip = 1; skip < st.size(); skip = skip + 1) {
      string_gap_mirror(st, skip);
    }
  }
  return;
}

void string_xor(std::vector<uint8_t> &st, uint32_t mask) {
  uint8_t toggles[4];
  toggles[0] = (uint8_t)((uint32_t)mask >> 0x18);
  toggles[1] = (char)((uint32_t)mask >> 0x10);
  toggles[2] = (char)((uint32_t)mask >> 8);
  toggles[3] = (char)mask;

  for (int i = 0; i < st.size(); i = i + 1) {
    st[i] = st[i] ^ toggles[i & 3];
  }
  return;
}

auto string_xor_n(std::vector<uint8_t> const &st) -> std::vector<uint8_t> {
  std::vector<uint8_t> out = st;
  for (int i = 0xabcf00d; i < 0xdeadbeef; i = i + 0x1fab4d) {
    string_xor(out, i);
  }
  return out;
}

std::vector<uint8_t> encrypted_flag = {
    0x7a, 0x2e, 0x6e, 0x68, 0x1d, 0x65, 0x16, 0x7c, 0x6d, 0x43,
    0x6f, 0x36, 0x3f, 0x62, 0x15, 0x46, 0x43, 0x36, 0x40, 0x37,
    0x58, 0x01, 0x58, 0x35, 0x62, 0x6b, 0x53, 0x30, 0x38, 0x17};

#include <cctype>
void dump(std::vector<uint8_t> const &st, bool hex = false,
          bool no_ln = false) {
  for (size_t i = 0; i < st.size(); ++i) {
    if (hex) {
      printf("%02x", st[i]);
    } else {
      if (std::isprint(st[i])) {
        putchar(st[i]);
      } else {
        putchar('.');
      }
    }
  }
  if (!no_ln) {
    puts("");
  }
}

int validate_flag(std::vector<uint8_t> const &in) {
  if (in.size() != encrypted_flag.size()) {
    puts("Invalid input size.");
    return -1;
  }

  std::vector<uint8_t> shuffled_in = in;
  string_shuffle(shuffled_in, -1);

  std::vector<uint8_t> shuffled_flag = encrypted_flag;
  string_shuffle(shuffled_flag, -1);

  // same -> 0, different -> (number of different characters)
  int diff_count = 0;
  for (uint32_t i = 0; i < 30; i++) {
    if (shuffled_in[i] != shuffled_flag[i]) {
      diff_count++;
    }
  }
  // dump(shuffled_in, true, true);
  // printf("<=>");
  // dump(shuffled_flag, true, true);
  // printf("---> %d differences\n", diff_count);
  return diff_count;
}