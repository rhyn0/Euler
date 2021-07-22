#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <stdio.h>

#include "euler.h"

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
    // check if args were passed, if not - default
    if (n < 0)
        n = 1000;
    int sum = 0, i;
    for (i = 3; i < n; i += 3)
        sum += i;
    for (i = 5; i < n; i += 5)
    {
        if (i % 3 != 0)
            sum += i;
    }
    return sum;
    // math version
    // can not include the n term, supposed to be strictly less than n
    // n -= 1;
    // return (int)(floor(n / 3) / 2 * (3 + n - (n % 3)) + floor(n / 5) / 2 * ((n - n % 5) + 5) - floor(n / 15) / 2 * ((n - n % 15) + 15));
}

/**
 * @brief Sum of Even Fibonacci numbers
 * 
 * Create each term in the fibonacci sequence under the value of n
 * Add to the running sum only terms of that are even, where 0th and 1st term are 1.
 * 
 * @param num limit to sum under
 * @return int 
 */
int euler2(int num)
{
    // check for default arg case
    if (num < 0)
        num = 4000000;
    // int t0 = 1, t1 = 1;
    // int evenTerm = t0 + t1, sum = 0;
    // while (evenTerm < num)
    // {
    //     sum += evenTerm;
    //     t0 = t1 + evenTerm;
    //     t1 = t0 + evenTerm;
    //     evenTerm = t0 + t1;
    // }
    // return sum;
    /**
     * Math version
     * 
     * If we look at first few terms of Fibonacci sequence, adding in 'X'
     *      1 '2' 3 5 '8' 13 21 '34'
     *      2 8 34 -> leads us to believe that E(n) = 4 * E(n - 1) + E(n - 2)
     * This breaks down into F(n) = 4 * F(n - 3) + F(n - 6) which does hold
     */
    int t0 = 0, t1 = 0;
    int sum = 0, c = 2;
    while (c < num)
    {
        sum += c;
        t0 = t1;
        t1 = c;
        c = 4 * t1 + t0;
    }
    return sum;
}

/**
 * @brief Largest Prime Factor of num
 * 
 * Doing prime factorization on n directly to find the largest prime factor
 * Starting at divisor = 2, divide num until num mod divisor != 0, then increase divisor by 1 
 * 
 * @param num number to find the largest factor of
 * @return int 
 */
// TODO: test case 60085147514312458
long int euler3(long long int num)
{
    // check for default args
    if (num < 0)
        num = 600851475143;
    long long int largestFactor = 0, divisor = 2;
    while (divisor * divisor <= num)
    {
        if (num % divisor == 0)
        {
            num /= divisor;
            largestFactor = divisor;
        }
        else
        {
            divisor += 1;
        }
    }
    return (num > largestFactor) ? num : largestFactor;
}

/**
 * @brief Returns the value of an int if read backwards
 * 
 * This was implemented as opposed to converting to string and reversing that.
 * 
 * @param n number to reverse
 * @return int 
 */
int reverseNum(int n)
{
    int rev = 0;
    while (n > 0)
    {
        rev = 10 * rev + n % 10;
        n /= 10;
    }
    return rev;
}

/**
 * @brief Largest Palindrome Product of 2 n digit numbers
 * 
 * A palindrome is one that is equivalent reading forwards and backwards.
 * Take 2 n digit integers, multiply them together, see if its a palindrome.
 * Return the largest palindrome found.
 * 
 * @param n length of numbers to multiply, n = 3 means [100, 999]
 * @return int 
 */
int euler4(int n)
{
    if (n < 0)
        n = 3;
    int biggest = 0, i, j, temp;
    int start = pow(10, n) - 1, end = pow(10, n - 1);
    for (i = start; i >= end; i--)
    {
        // only need to compute each pair once
        // e.g. 999 * 100 == 100 * 999
        for (j = start; j >= i; j--)
        {
            temp = i * j;
            // dont bother checking any numbers under biggest
            if (temp <= biggest)
            {
                break;
            }
            else if (reverseNum(temp) == temp)
            {
                biggest = temp;
            }
        }
    }
    return biggest;
}

int euler5(int num)
{
}