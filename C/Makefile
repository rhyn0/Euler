CC 			= gcc
CCFLAGS		= -pedantic -Wall -Werror -g -std=c99
OBJECTS 	= $(wildcard *.o)

all: main tests

main: objects
	$(CC) -o ../main $(CCFLAGS) *.o

objects:
	$(CC) -c $(CCFLAGS) main.c euler.c

tests:
	$(CC) -o ../tests $(CCFLAGS) euler_test.c

clean: clean_main clean_tests

clean_main:
	rm 

clean_tests:
	rm *.o ../tests
