{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "cc-be-practive-run-1";
  version = "1";

  src = pkgs.fetchurl {
    url = "https://shell1.production.cognitivectf.com/static/6bfc49b542b81277718bfa9bfba22063/run_this";
    sha256 = "nuKMkW7J1dTTCRoxXDW3w98QVF9F5mN92G3CKXn4eLU=";
  };

  unpackPhase = ''
    mkdir -p "$out"

    cp "$src" "$out/run_this"
    chmod +x "$out/run_this"
    $out/run_this > "$out/flag.txt"

  '';
}
