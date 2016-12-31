CFLAGS=-Wall -O3 -pedantic

all: example

example: example.o simerr.o

example.o: example.c simerr.h

simerr.o: simerr.c simerr.h

clean:
	rm -f *.o example
