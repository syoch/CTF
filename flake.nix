{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
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
          frida-tools

          # Utilities
          cmake
          unzip
          p7zip
          sage

          # Windows Integration
          pkgsCross.mingwW64.buildPackages.gcc
          powershell

          # Python things
          ruff

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
              tqdm
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
        shellHook = ''
          # Find CTF directory with matching .envrc
          function find_ctf_dir() {
            local dir="$PWD"
            while [ "$dir" != "/" ]; do
              if [ -f "$dir/.envrc" ]; then
                echo "$dir"
                return
              fi
              dir="$(dirname "$dir")"
            done
          }
          export PYTHONPATH=$PYTHONPATH:`find_ctf_dir`/common
        '';
      };
    };
}
