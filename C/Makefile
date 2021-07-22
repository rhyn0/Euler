CC 			= gcc
CCFLAGS		= -pedantic -Wall -Werror -g -std=c99

all: main tests

main: objects
	$(CC) -o main $(CCFLAGS) *.o

objects:
	$(CC) -c $(CCFLAGS) C/main.c C/euler.c

tests:
	$(CC) -o tests $(CCFLAGS) C/euler_test.c

clean:
	rm -f *.o main tests