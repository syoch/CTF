#include "brute.hpp"
#include <algorithm>

void test_xor_n_symmetry() {
  std::vector<uint8_t> test_str = {'t', 'e', 's', 't', '_', 's',
                                   't', 'r', 'i', 'n', 'g'};
  string_xor_n(test_str);
  string_xor_n(test_str);

  for (int i = 0; i < test_str.size(); ++i) {
    if (test_str[i] != "test_string"[i]) {
      puts("XOR symmetry test failed!");
      abort();
      return;
    }
  }
}
void test_shuffle_symmetry() {
  std::vector<uint8_t> test_str = {'t', 'e', 's', 't', '_', 's',
                                   't', 'r', 'i', 'n', 'g'};
  string_shuffle(test_str, 1);
  string_shuffle(test_str, -1);

  for (int i = 0; i < test_str.size(); ++i) {
    if (test_str[i] != "test_string"[i]) {
      puts("Shuffle symmetry test failed!");
      abort();
      return;
    }
  }
}

void test_xor_comprehensiveness() {
  std::vector<uint8_t> test_vec;
  test_vec.resize(30);

  for (int i = 0; i < 30; ++i) {
    test_vec[i] = 0xff;
    auto v1 = test_vec;
    string_xor(v1, 0x55aa55aa);

    test_vec[i] = 0x00;
    auto v2 = test_vec;
    string_xor(v2, 0x55aa55aa);

    // if v == test_vec: error
    if (std::equal(v1.begin(), v1.end(), test_vec.begin())) {
      printf("XOR failed at index %d with value %d\n", i, i);
      dump(test_vec);
      dump(v1);
      dump(v2);
      abort();
      return;
    }
  }
}

void test_shuffle_comprehensiveness(int mode) {
  std::vector<uint8_t> test_vec;
  test_vec.resize(30);

  for (int i = 0; i < 30; ++i) {
    test_vec[i] = 0xff;
    auto v1 = test_vec;
    string_shuffle(v1, mode);

    test_vec[i] = 0x00;
    auto v2 = test_vec;
    string_shuffle(v2, mode);

    if (std::equal(v1.begin(), v1.end(), v2.begin())) {
      printf("Shuffle failed at index %d with value %d\n", i, i);
      dump(test_vec);
      dump(v1);
      dump(v2);
      abort();
      return;
    }
  }
}

int calc_error(std::vector<uint8_t> flag) {
  flag = string_xor_n(flag);
  string_shuffle(flag, 1);

  return validate_flag(flag);
}

void solve() {
  std::vector<uint8_t> input(30);
  std::fill(input.begin(), input.end(), 0);

  input[0] = 0;
  int min_error = calc_error(input);
  for (int i = 0; i < 30; i++) {
    for (int c = 0; c < 256; c++) {
      input[i] = c;
      int error = calc_error(input);
      printf("i=%d c=%d e=%d ", i, c, error);
      dump(input);

      if (error < min_error) {
        min_error = error;
        break;
      }
    }
  }
}

int main() {
  test_xor_comprehensiveness();
  test_shuffle_comprehensiveness(1);
  test_shuffle_comprehensiveness(-1);
  test_xor_n_symmetry();
  test_shuffle_symmetry();

  solve();
  return 0;
}