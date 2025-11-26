{
  stdenv,
  fetchFromGitHub,
  gmp,
  mpfr,
  fplll,
  eigen,
  openblas,

  ninja,
  cmake
}:
stdenv.mkDerivation {
  pname = "flatter";
  version = "0.1.0";

  buildInputs = [
    gmp
    mpfr
    fplll
    eigen
    openblas
  ];

  nativeBuildInputs = [ ninja cmake ];

  configurePhase = ''
    mkdir build
    cmake -S $src -B build -G Ninja -DCMAKE_INSTALL_PREFIX=$out
  '';

  buildPhase = ''
    ninja -C build all
  '';

  installPhase = ''
    ninja -C build install
  '';

  src = fetchFromGitHub {
    owner = "keeganryan";
    repo = "flatter";
    rev = "master";
    sha256 = "sha256-NAefYPJ+syTmpDiOzkgKB1IZmgQ2DNmvLrtoBee/IX4=";
  };
}
