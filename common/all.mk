common/public/libov.so: common/override/lib.c
	gcc -shared -fPIC $< -o $@

all: common/public/libov.so