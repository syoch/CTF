#include <cstdint>

uint64_t Random::GetRandom(Random *this) {
  uint64_t value;

  value =
      (ulong)(this->last_random * this->mul + this->add) % (ulong)this->range;
  this->last_random = (uint32_t)value;
  return value;
}
