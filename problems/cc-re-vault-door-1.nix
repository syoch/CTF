{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "cc-gs-firstgrep";
  version = "1";

  src = pkgs.fetchurl {
    url = "https://shell1.production.cognitivectf.com/static/f47352c1fbb801dc2171b2b9a401a294/VaultDoor1.java";
    sha256 = "B0/9kb0yvjHp7VIVPRq7hwtTdcqb8Iw9ptP601JZEvo=";
  };

  unpackPhase = ''
    mkdir -p "$out"
    cp "$src" "$out/VaultDoor1.java"
  '';
}
