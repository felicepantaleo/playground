CFLAGS= -std=c++14 -ftree-vectorize -march=native -O3 -mtune=native 
LIBS = -ltbb


CC=g++
all: ticl

ticl: 
	$(CC) main.cc $(CFLAGS)  -o ticl $(LIBS) 

clean:
	rm -rf *.o ticl



