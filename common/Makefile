all:

public/libov.so: override/lib.c
	gcc -shared -fPIC override/lib.c -o public/libov.so
all: public/libov.so

clean:
	rm -f public/libov.so