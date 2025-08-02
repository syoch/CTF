#include <cstdint>

struct Random {
  uint32_t mul;
  uint32_t add;
  uint32_t range;
  uint32_t last_random;

  Random(uint32_t mul) {
    uint64_t value;

    this->mul = mul ^ 0x77777777;
    this->add = 2021;
    this->range = 0x7fffffff;
    value = std::random_device::_M_getval();
    this->last_random = value ^ 0x77777777;
  }

  uint64_t GetRandom() {
    uint64_t value;

    value = (this->last_random * this->mul + this->add) % this->range;
    this->last_random = (uint32_t)value;
    return value;
  }
};