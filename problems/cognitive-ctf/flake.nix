{
  description = "flake that provides a package `source` which downloads a single file from a URL";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        packages.cc-gs-firstgrep = import ./cc-gs-firstgrep.nix { inherit pkgs; };
        packages.cc-be-practive-run-1 = import ./cc-be-practive-run-1.nix { inherit pkgs; };
        packages.cc-be-handy-shellcode = import ./cc-be-handy-shellcode.nix { inherit pkgs; };
        packages.cc-re-vault-door-1 = import ./cc-re-vault-door-1.nix { inherit pkgs; };
        packages.cc-be-overflow-1 = import ./cc-be-overflow-1.nix { inherit pkgs; };
      }
    );
}
