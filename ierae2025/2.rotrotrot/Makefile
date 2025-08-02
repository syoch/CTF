all:

build/solve: solve.c
	@mkdir -p $(@D)
	gcc -o $@ $<

build/flag.txt: distfiles/flag.enc build/solve
	@mkdir -p $(@D)
	./build/solve $< $@
all: build/flag.txt