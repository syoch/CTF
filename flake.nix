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
    rec {
      packages.${system} = {
        flatter = pkgs.callPackage ./pkgs/flatter.nix { };
        msolve = pkgs.callPackage ./pkgs/msolve.nix { };

        RsaCtfTool = pkgs.python313Packages.callPackage ./pkgs/RsaCtfTool.nix { };
        cuso = pkgs.python313Packages.callPackage ./pkgs/cuso.nix {
          sage = pkgs.sage.lib;
        };
      };

      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          qemu-user
          steam-run-free
          openssl_3_5
          clang-tools

          # Rev/Pwn tools
          one_gadget
          ropgadget
          rp
          binsider
          gdb
          frida-tools

          # Cryptography tools
          sage
          singular
          (packages.${system}.flatter)
          flint3

          # Utilities
          cmake
          unzip
          p7zip

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
              sage.lib
              packages.${system}.RsaCtfTool
              packages.${system}.cuso
            ]
          ))
        ];
        shellHook = ''
          # Find CTF directory with matching .envrc
          function find_ctf_dir() {
            local dir="$PWD"
            while [ "$dir" != "/" ]; do
              if [ -f "$dir/.envrc" ]; then
                echo "$dir"{a}
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
