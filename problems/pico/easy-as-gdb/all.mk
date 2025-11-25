pico/easy-as-gdb/build/solve: pico/easy-as-gdb/solve.cpp pico/easy-as-gdb/brute.hpp
	@mkdir -p $(@D)
	g++ -std=c++11 -O2 -o $(@) $<

pico/easy-as-gdb/flag.txt: pico/easy-as-gdb/build/solve
	@$< > $@

all: pico/easy-as-gdb/flag.txt