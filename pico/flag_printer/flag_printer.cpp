/*
 * コンパイル方法 (例):
 * gcc solution.c -o solution -lflint -lgmp
 */

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/fmpz_mod.h>
#include <flint/fmpz_mod_poly.h>
#include <flint/fmpz_vec.h>
#include <stdio.h>

/**
 * ヴァンデルモンド行列の方程式 (x_i^j) * v = y (MOD N) を解く関数
 *
 * @param result_v  結果の係数ベクトル v を格納する配列 (出力)
 * @param X         x_i の配列 (入力)
 * @param Y         y_i の配列 (入力)
 * @param len       配列の長さ (k)
 * @param mod_n     法の値 N
 */
void solve_vandermonde_system(fmpz *result_v, const fmpz *X, const fmpz *Y,
                              slong len, const fmpz_t mod_n) {
  /* 1. コンテキストの初期化 (法 N での計算準備) */
  fmpz_mod_ctx_t ctx;
  fmpz_mod_ctx_init(ctx, mod_n);

  /* 2. 多項式の初期化 */
  fmpz_mod_poly_t poly;
  fmpz_mod_poly_init(poly, ctx);

  /* 3. 多項式補間の実行
   * FLINTの内部アルゴリズムにより、O(len * log(len)^2) などの高速な手法が
   * 自動的に選択されます（点の数が多い場合）。
   * 数学的には、これが「ヴァンデルモンド行列の逆行列を掛ける」操作と等価です。
   */
  fmpz_mod_poly_inter(poly, X, Y, len, ctx);

  /* 4. 結果の抽出
   * 多項式の係数が、求めたいベクトル v に対応します。
   * v_0 + v_1*x + v_2*x^2 ... なので、i番目の係数が v[i] です。
   */
  for (slong i = 0; i < len; i++) {
    // 係数を取得し、result_v[i] に格納
    fmpz_mod_poly_get_coeff_fmpz(result_v + i, poly, i, ctx);
  }

  /* 5. メモリの解放 */
  fmpz_mod_poly_clear(poly, ctx);
  fmpz_mod_ctx_clear(ctx);
}

// ---------------------------------------------------------
// 使用例 (Main)
// ---------------------------------------------------------
int main() {
  slong k = 3;

  // x = {1, 2, 3}
  long x_vals[] = {1, 2, 3};
  // y = {3, 7, 13}  (例: v={1, 1, 1} なら 1+2+4=7, 1+3+9=13...)
  long y_vals[] = {3, 7, 13};

  /* 変数の初期化 */
  fmpz_t N;
  fmpz_init(N);
  fmpz_set_str(N, "7514777789", 10);

  // FLINTの整数型配列 (fmpzの配列) を確保
  fmpz *X = _fmpz_vec_init(k);
  fmpz *Y = _fmpz_vec_init(k);
  fmpz *V = _fmpz_vec_init(k);

  // データのセット
  for (slong i = 0; i < k; i++) {
    fmpz_set_si(X + i, x_vals[i]);
    fmpz_set_si(Y + i, y_vals[i]);
  }

  /* --- 計算実行 --- */
  printf("Solving (x^j)*v = y mod %s ...\n", fmpz_get_str(NULL, 10, N));
  solve_vandermonde_system(V, X, Y, k, N);

  /* 結果表示 */
  printf("Result vector v:\n");
  for (slong i = 0; i < k; i++) {
    flint_printf("v[%wd] = %Zd\n", i, V + i);
  }

  /* クリーンアップ */
  _fmpz_vec_clear(X, k);
  _fmpz_vec_clear(Y, k);
  _fmpz_vec_clear(V, k);
  fmpz_clear(N);

  return 0;
}