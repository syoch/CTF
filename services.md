```bash
#!/bin/bash
win_vm_ip = `tailscale ip -4 win-vm`
syoch_nix_ip = `tailscale ip -4 syoch-nix`

ssh win-vm &
  curl $syoch_nix_ip:30000/utils/peb-inspect/daemon.py -o daemon.py
  python daemon.py -b $win_vm_ip -p 31000 -s $syoch_nix_ip:30000

python3 -m http.server 30000 -b $syoch_nix_ip &

python3 -m jupyter server &
```