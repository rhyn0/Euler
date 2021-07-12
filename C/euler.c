#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#include "euler.h"

void showUsage()
{
    printf("main [-h] problem_num [n]\n");
}

void showHelp()
{
    printf("Euler Problems:\n\t1 - Sum of multiples of 3 and 5, default 1000\n\t"
           "2 - Sum of even Fibonacci, default 4 million\n\t"
           "3 - Largest Prime factor of N, default 600851475143\n\t"
           "4 - Largest Palindrome Product of 3 digit numbers\n\t"
           "5 - Smallest multiple of all numbers 1 to n, default 20.\n");
    exit(0);
}

int checkArgs(int argc, char **argv, int *n)
{
    int i;
    if (argc == 1 || argc > 3)
    {
        fprintf(stderr, "No Euler function specified.\n");
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
        *n = atoi(argv[2]);
    else
        *n = -1;
    return atoi(argv[1]);
}

bool isPrime(int num)
{
    int i, sqt = (int)sqrt(num);
    if (num == 1)
        return false;
    for (i = 2; i <= sqt; i++)
    {
        if (num % i == 0)
            return false;
    }
    return true;
}

int main(int argc, char **argv)
{
    int prob, addlArgs;
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
        printf("Euler 3 is %d\n", euler3(addlArgs));
        break;

    default:
        printf("That problem is not available yet.");
        break;
    }
}

/**
 * @brief Multiples of 3 and 5. Sum of multiples of 3 or 5 under n
 * 
 * Brute forces through all numbers in the range twice, double checking on second pass
 * that numbers are not counted twice.
 * 
 * @param n limit to sum under
 * @return int 
 */
int euler1(int n)
{
    int sum = 0, i;
    // check if args were passed, if not - default
    if (n == -1)
        n = 1000;
    for (i = 3; i < n; i += 3)
        sum += i;
    for (i = 5; i < n; i += 5)
    {
        if (i % 3 != 0)
            sum += i;
    }
    return sum;
    // math version
    // return (int)((n / 3) / 2) * (3 + n - (n % 3)) + (n / 5) / 2 * ((n - n % 5) + 5) - (n / 15) / 2 * ((n - n % 15) + 15);
}

int euler2(int num)
{
    return -1;
}

int euler3(int num)
{
    return -1;
}