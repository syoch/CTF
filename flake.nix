{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          qemu-user
          steam-run-free
          openssl_3_5
          clang-tools
          flint3

          one_gadget
          ropgadget
          rp
          binsider
          gdb

          # Utilities
          cmake
          unzip
          p7zip

          # Windows Integration
          pkgsCross.mingwW64.buildPackages.gcc
          powershell

          # Python things
          ruff
          sage

          (python313.withPackages (
            ps: with ps; [
              jupyter
              numpy
              sympy
              matplotlib
              pwntools
              fastecdsa
              gmpy2
              pypng
              galois
              sage
              pycryptodome
              z3
              (ps.buildPythonPackage {
                pname = "RsaCtfTool";
                version = "1.0.0";
                format = "setuptools";
                src = fetchFromGitHub {
                  owner = "RsaCtfTool";
                  repo = "RsaCtfTool";
                  rev = "master";
                  sha256 = "sha256-xttrOyStaTy6ZoL+2S3oVbEidiq0hukKDZsN0WM4Zdw=";
                };
              })
            ]
          ))
        ];
      };
    };
}
