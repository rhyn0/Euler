#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "euler.h"

void showUsage()
{
    printf("main [-h]\n");
    printf("main problem_num [n]\n");
}

void showHelp()
{
    printf("Euler Problems:\n\t"
           "1 - Sum of multiples of 3 and 5, default 1000\n\t"
           "2 - Sum of even Fibonacci, default 4 million\n\t"
           "3 - Largest Prime factor of N, default 600851475143\n\t"
           "4 - Largest Palindrome Product of 3 digit numbers\n\t"
           "5 - Smallest multiple of all numbers 1 to n, default 20.\n");
    exit(0);
}

int checkArgs(int argc, char **argv, long long int *n)
{
    int i;
    if (argc == 1 || argc > 3)
    {
        fprintf(stderr, "Incorrect Euler function specified.\n");
        showUsage();
        exit(-1);
    }
    // if help flag is suppplied, print help and then quit
    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-h") == 0)
            showHelp();
    }
    // if user passes additional args, set. Otherwise set to -1
    if (argc > 2)
    {
        *n = atoll(argv[2]);
        if (*n < 0)
            fprintf(stderr, "Functions do not take in negative input.\n");
    }
    else
        *n = -1;
    return atoi(argv[1]);
}

int main(int argc, char **argv)
{
    int prob;
    long long int addlArgs;
    prob = checkArgs(argc, argv, &addlArgs);
    switch (prob)
    {
    case 1:
        printf("Euler 1 is %d\n", euler1(addlArgs));
        break;

    case 2:
        printf("Euler 2 is %d\n", euler2(addlArgs));
        break;

    case 3:
        printf("Euler 3 is %ld\n", euler3(addlArgs));
        break;

    case 4:
        printf("Euler 4 is %d\n", euler4(addlArgs));
        break;

    case 5:
        printf("Euler 5 is %d\n", euler5(addlArgs));
        break;

    case 6:
        printf("Euler 6 is %d\n", euler6(addlArgs));
        break;

    case 7:
        printf("Euler 7 is %d\n", euler7(addlArgs));
        break;

    case 8:
        printf("Euler 8 is %lld\n", euler8(addlArgs));
        break;

    default:
        printf("That problem is not available yet.");
        break;
    }
}