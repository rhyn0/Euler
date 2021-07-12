CCFLAGS		= -pedantic -Wall -Werror -g -std=c99

all: main tests

main: objects
	gcc -o main $(CCFLAGS) euler.o

objects:
	gcc -c $(CCFLAGS) C/euler.c

tests:
	gcc -o tests $(CCFLAGS) C/euler_test.c

clean:
	rm -f *.o main tests