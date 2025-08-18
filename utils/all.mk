utils/peb-inspect/peb-inspect.txt: utils/peb-inspect/build/peb-inspect.exe
	ssh win-vm Powershell -NoProfile '\\host.lan\Data\work\CTF\utils\peb-inspect\build\peb-inspect.exe' > $@

all: utils/peb-inspect/peb-inspect.txt
