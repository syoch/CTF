{ stdenv, gcc }:

stdenv.mkDerivation {
  pname = "libov";
  version = "1.0";

  src = ./.;

  buildInputs = [
    gcc
  ];

  buildPhase = ''
    gcc -shared -fPIC -o libov.so lib.c
  '';

  installPhase = ''
    mkdir -p $out/lib
    cp libov.so $out/lib/
  '';
}
