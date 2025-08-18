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

          one_gadget
          ropgadget
          rp
          binsider

          # Utilities
          cmake
          unzip
          p7zip

          # Windows Integration
          pkgsCross.mingwW64.buildPackages.gcc
          powershell

          # Python things
          ruff
          python313
          (python313.withPackages (
            ps: with ps; [
              jupyter
              numpy
              matplotlib
              pwntools
              fastecdsa
            ]
          ))
        ];
      };
    };
}
