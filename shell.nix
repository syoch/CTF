{ pkgs }:
pkgs.mkShell {
  packages = with pkgs; [
    unzip
    qemu-user
    steam-run-free
    openssl_3_5
    p7zip
    one_gadget
    ropgadget
    rp
    binsider

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
}
