{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "cc-gs-firstgrep";
  version = "1";

  src = pkgs.fetchurl {
    url = "https://shell1.production.cognitivectf.com/static/8bbae9e50cf8365659bf50b592e2180b/vuln";
    sha256 = "40j17uhQL4F4cWN2xOAhqmsID2GnXxc4D0bNSQROVR8=";
  };

  unpackPhase = ''
    mkdir -p "$out"
    cp "$src" "$out/vuln"
  '';
}
