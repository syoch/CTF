{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "cc-gs-firstgrep";
  version = "1";

  src = pkgs.fetchurl {
    url = "https://shell1.production.cognitivectf.com/static/6f7bcf6f937159e689ccb3dacae50936/file";
    sha256 = "P3HmNHzik+ja78XvfQWgRuP1i4KflhhrTWX/sA9FhOw=";
  };

  unpackPhase = ''
    mkdir -p "$out"
    grep "CTF{" "$src" > "$out/flag.txt"
  '';
}
