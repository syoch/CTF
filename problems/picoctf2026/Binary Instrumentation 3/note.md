
frida-trace -H 192.168.122.2 -f BI3.exe -S a.js -i KERNEL32.DLL\!CreateFileA -i KERNEL32.DLL\!WriteFile -i KERNEL32.DLL\!CreateProcessA | tee dump