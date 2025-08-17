common/public/libov.so: common/override/lib.c
	gcc -shared -fPIC $< -o $@ -Wl,-soname,libov.so
all: common/public/libov.so