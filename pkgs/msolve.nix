{
  stdenv,
  fetchFromGitHub,
  
  # Build requirements
  autoreconfHook,
  
  # dependencies
  gmp,
  mpfr,
  flint,
    

  ninja,
  cmake
}:
stdenv.mkDerivation {
  pname = "msolve";
  version = "0.1.0";

  nativeBuildInputs = [
    autoreconfHook
  ];
  buildInputs = [
    gmp
    mpfr
    flint
  ];

  src = fetchFromGitHub {
    owner = "algebraic-solving";
    repo = "msolve";
    rev = "v0.9.2";
    sha256 = "sha256-/KV4zmato86DKDOUe3D/Ru/cFQaKOPyx6cQ8wZS4bgA=";
  };
}
