#include <array>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <optional>
#include <vector>

enum MinoType {
  kMinoT = 0,
  kMinoO = 1,
  kMinoS = 2,
  kMinoZ = 3,
  kMinoL = 4,
  kMinoJ = 5,
  kMinoI = 6,
};

class Mino {
  MinoType type_;

public:
  Mino(MinoType type) : type_(type) {}

  auto GetType() const { return type_; }

  auto GetChar() const {
    switch (type_) {
    case kMinoT:
      return 'T';
    case kMinoO:
      return 'O';
    case kMinoS:
      return 'S';
    case kMinoZ:
      return 'Z';
    case kMinoL:
      return 'L';
    case kMinoJ:
      return 'J';
    case kMinoI:
      return 'I';
    }
    return ' ';
  }
};

class MinoGenerator {
public:
  auto Init(uint seed) { srand(seed); }

  auto Get() { return Mino(static_cast<MinoType>(rand() % 7)); }
};

void TestMinoGen() {
  int seed;
  std::cin >> seed;

  MinoGenerator mino_gen;
  mino_gen.Init(seed);

  while (1) {
    getchar();

    for (int i = 0; i < 10; ++i) {
      auto mino = mino_gen.Get();
      auto mino_char = mino.GetChar();
      std::cout << mino_char << " ";
    }
    std::cout << std::endl;
  }
}

#define kDetailSearchEnabled 0
// clang-format off
const std::vector<std::array<int, 8>> kMinoRequireTable = {
    // T O S Z L J I total
      {2,0,1,2,1,1,0,    7},
      {2,1,0,2,0,1,0,    6},

      //{0,0,0,0,0,0,0},

};
// clang-format on

const std::vector<int> kFoundSeeds = {
    //
    0};

const auto kSeedSearch_Begin /**/ = 0x0000'0000;
const auto kSeedSearch_End /*  */ = 0x0100'0000;

struct ReviewResult {
  bool mino_constraint_passed = false;
  Mino next;

#if kDetailSearchEnabled
  float mean_score = 0;
  float mino_score = 0;
  float distance_score = 0;

  float mino_mean = 0;
  float distance_mean = 0;
  float score = 0;
#endif
};

auto ReviewSeed(uint seed) {
#if kDetailSearchEnabled
  std::array<int, 7> counter = {0};
  std::array<int, 7> neighbor_distance = {0};
  std::array<int, 7> neighbor_distance_total = {0};
  const size_t N = 40;
#endif
  MinoGenerator mino_gen;
  mino_gen.Init(seed);
  auto mino_requires = kMinoRequireTable;

  for (auto &current_reqs : mino_requires) {
    for (int i = 0; i < current_reqs[7]; ++i) {
      auto mino = mino_gen.Get();

      auto &counter = current_reqs[mino.GetType()];
      if (counter == 0) {
        return ReviewResult{.mino_constraint_passed = false,
                            .next = mino_gen.Get()};
      }

      counter--;
    }
  }

#if kDetailSearchEnabled
  for (int i = 0; i < N; ++i) {
    auto mino = mino_gen.Get();
    counter[mino.GetType()]++;

    neighbor_distance_total[mino.GetType()] = neighbor_distance[mino.GetType()];
    neighbor_distance[mino.GetType()] = 0;

    for (int j = 0; j < 7; ++j) {
      neighbor_distance[j] += 1;
    }

    if (mino_requires.size() == 0) {
      continue;
    }
  }

  // mean
  float mino_mean = 0;
  for (int i = 0; i < 7; ++i) {
    mino_mean += counter[i] * i;
  }
  mino_mean /= N;

  auto mean_score = (mino_mean - 3) * 100 / 3;

  // std
  float mino_std = 0;
  for (int i = 0; i < 7; ++i) {
    mino_std += (counter[i] - mino_mean) * (counter[i] - mino_mean);
  }
  mino_std /= N;
  mino_std = sqrt(mino_std);
  float mino_score = mino_std;

  // distance score
  float distance_score = 0;
  float distance_global_mean = 0;
  for (int i = 0; i < 7; ++i) {
    if (counter[i] == 0) {
      counter[i] = 1;
    }
    auto distance_mean = neighbor_distance_total[i] / counter[i];
    const auto kGoodDistance = 7;

    auto dist_error = distance_mean - kGoodDistance;
    if (dist_error < 0)
      distance_score += dist_error * dist_error * 20;
    else
      distance_score += dist_error * dist_error;
    distance_global_mean += distance_mean;
  }
  distance_score /= N;
  distance_global_mean /= 7;

  auto total_score =
      0.4f * mino_std + 0.3f * distance_score + 0.3f * mean_score / 100;
#endif

  ReviewResult result = {.mino_constraint_passed = true,
#if kDetailSearchEnabled
                         .score = total_score,
                         .mean_score = mean_score,
                         .mino_score = mino_score,
                         .distance_score = distance_score,
                         .mino_mean = mino_mean,
                         .distance_mean = distance_global_mean,
#endif
                         .next = mino_gen.Get()};
  return result;
}

void FindMeanSeed() {
  struct Result {
    int seed = 0;
    ReviewResult result;

#if kDetailSearchEnabled
    auto UpdateIfBetter(Result new_result) {
      if (new_result.result.score < result.score) {
        seed = new_result.seed;
        result = new_result.result;
        return true;
      }
      return false;
    }
#endif

    auto Show() {
      std::cout << "Seed: " << seed << std::endl;
#if kDetailSearchEnabled
      std::cout << "Mino/Mean/Dist Score: " << result.mino_score << "/"
                << result.mean_score << "/" << result.distance_score
                << std::endl;
      std::cout << "Mino Mean: " << result.mino_mean << std::endl;
      std::cout << "Distance Mean: " << result.distance_mean << std::endl;
      std::cout << "Score: " << result.score << std::endl;
#endif

      MinoGenerator mino_gen;
      mino_gen.Init(seed);
      for (auto const &def : kMinoRequireTable) {
        for (size_t i = 0; i < def[7]; i++) {
          std::cout << mino_gen.Get().GetChar();
        }
        std::cout << " ";
      }
      for (int i = 0; i < 20; ++i) {
        std::cout << mino_gen.Get().GetChar();
      }

      std::cout << std::endl;
    }
  };

  std::optional<Result> res1_result;
  std::optional<Result> res0_result;
  std::optional<Result> res2_result;
  int match_count = 0;

  std::array<int, 7> next_mino_counts = {0};

  const auto kSeqSearch_Length = kSeedSearch_End - kSeedSearch_Begin;
  for (int i = 0; i < kSeqSearch_Length + kFoundSeeds.size(); i++) {
    int seed = i < kFoundSeeds.size()
                   ? kFoundSeeds[i]
                   : (kSeedSearch_Begin + i - kFoundSeeds.size());

    if ((i & 0xFFFF) == 0) {
      printf("%8x: seed=%8x, found=%d\n", i, seed, match_count);
    }

    auto result = ReviewSeed(seed);

    if (not result.mino_constraint_passed) {
      continue;
    }

    next_mino_counts[result.next.GetType()]++;

    match_count++;
    if (res0_result == std::nullopt) {
      res0_result = {seed, result};
      continue;
    }
    if (res1_result == std::nullopt) {
      res1_result = {seed, result};
      continue;
    }
    if (res2_result == std::nullopt) {
      res2_result = {seed, result};
      continue;
    }

#if kDetailSearchEnabled
    if (res0_result.UpdateIfBetter({seed, result}))
      continue;
    if (res1_result.UpdateIfBetter({seed, result}))
      continue;
    if (res2_result.UpdateIfBetter({seed, result}))
      continue;
#endif
  }
  std::cout << "===================================================="
            << std::endl;
  std::cout << "Match Count: " << match_count << std::endl;

  std::cout << "===== res0 =====" << std::endl;
  if (res0_result)
    res0_result->Show();
  std::cout << "===== res1 =====" << std::endl;
  if (res1_result)
    res1_result->Show();
  std::cout << "===== res2 =====" << std::endl;
  if (res2_result)
    res2_result->Show();

  std::cout << "===== Next Mino Counts =====" << std::endl;
  for (int i = 0; i < 7; ++i) {
    std::cout << "Mino " << Mino(static_cast<MinoType>(i)).GetChar() << ": "
              << next_mino_counts[i] << std::endl;
  }
}

int main() {
  // TestMinoGen();
  FindMeanSeed();
}