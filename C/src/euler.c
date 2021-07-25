#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

#include "euler.h"

bool isPrime(int num)
{
  int i, sqt = (int)sqrt(num);
  if (num <= 1) // there are no conventional prime negative numbers
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
 * Brute forces through all numbers in the range twice, double checking on
 * second pass that numbers are not counted twice.
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
  // return (int)(floor(n / 3) / 2 * (3 + n - (n % 3)) + floor(n / 5) / 2 * ((n
  // - n % 5) + 5) - floor(n / 15) / 2 * ((n - n % 15) + 15));
}

/**
 * @brief Sum of Even Fibonacci numbers
 *
 * Create each term in the fibonacci sequence under the value of n
 * Add to the running sum only terms of that are even, where 0th and 1st term
 * are 1.
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
 * Starting at divisor = 2, divide num until num mod divisor != 0, then
 * increase divisor by 1
 *
 * @param num number to find the largest factor of
 * @return int
 */
// TODO: test case 60085147514312458
long int
euler3(long long int num)
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

/**
 * @brief Smallest multiple of all numbers 1 to n
 *
 * If the number is divisible by all numbers [1, n] return, if not increase it
 * by n.
 *
 * @param num - default 20
 * @return int
 */
int euler5(int num)
{
  if (num < 0)
  {
    num = 20;
  }
  int multiple = num, j;
  while (1)
  {
    // need to keep the <= case for edge case like 1
    for (j = 1; j <= num; j++)
    {
      // if a number doesn't evenly divide, need a different multiple
      if (multiple % j != 0)
      {
        break;
      }
      else
      {
        // if all numbers evenly divide then return
        // guaranteed to be divisible by num
        // >= operator due to edge case of num = 1
        if (j >= num - 1)
        {
          return multiple;
        }
      }
    }
    // add num, thus guaranteeing that num divides it
    multiple += num;
  }
}

/**
 * @brief Difference of sum of squares and square of sum, for 1 to n
 *
 * Implemented a math equation hack, since O(1) time for same O(1) space
 *
 * @param num - default 100
 * @return int
 */
int euler6(int num)
{
  // check for input args, default 100
  if (num < 0)
  {
    num = 100;
  }
  /**
   * Makes use of the math equation for sum of i^2 for i in [1, n]
   *      n(n + 1)(2n + 1)/6
   * and the equation for sum of i for i in [1, n]
   *      n(n + 1)/2
   *
   * A code implementation would look like:
   *
   * int sum_square = 0, square_sum = 0, i;
   * for (i = 0; i <= num; i++)
   * {
   *      sum_square += (int)pow(i, 2);
   *      square_sum += i;
   * }
   * return sum_square - (int)pow(square_sum, 2);
   *
   */
  int sum_square = num * (num + 1) * (2 * num + 1) / 6;
  int square_sum = pow(num * (num + 1) / 2, 2);
  return (int)(square_sum - sum_square);
}

/**
 * @brief Ten Thousandth and First prime number
 * 
 * Iteratively find each prime number until we reach the nth one.
 * Stores all previous prime numbers which speeds up calculations a bit.
 * 
 * @param num - default 10001
 * @return int 
 */
int euler7(int num)
{
  if (num <= 0)
  {
    num = 10001;
  }
  /**
   * An alternative being 
   * 
   * int primeCount = 2;
   * int i = 3;
   * while (primeCount < num)
   * {
   *  i += 2;
   *  if (isPrime(i))
   *  {
   *    primeCount++;
   *  }
   * }
   * return i;
   */
  // variable based static allocation not allowed in previous standards
  int primeList[num], index;
  int i, j;
  bool prime = true;
  // keeps track of all primes encountered, so just return last one at end
  primeList[0] = 2; // keep this line, even though never used, makes things simpler
  primeList[1] = 3;
  index = 2; // pre-entered first 2 primes, start here
  while (index < num)
  {
    i = primeList[index - 1] + 2; // only check odd numbers
    while (true)
    {
      prime = true;
      for (j = 1; j < index; j++) // start at 1, since odds aren't divisible by 2
      {
        if (primeList[j] > sqrt(i)) // ! pow(i, 0.5) causes bad behavior, same for 1/2
        {
          break; // missed the proper divisor on lesser end, which means prime
        }
        else if (i % primeList[j] == 0)
        {
          prime = false; // divisible by any number, so composite (not prime)
          break;
        }
      }
      if (prime)
      {
        primeList[index] = i;
        index++;
        break;
      }
      else
      {
        i += 2;
      }
    }
  }
  return primeList[num - 1];
}

/**
 * @brief Greatest number of n adjacent integers.
 * 
 * Given a 1000 digit number, find the greatest product of n adjacent digits.
 * Note: Returns a number that exceeds 32 bytes, check your long long widths
 * 
 * @param num - default 13
 * @return long long int 
 */
long long int euler8(int num)
{
  if (num <= 0)
    num = 13;
  const char *given = "73167176531330624919225119674426574742355349194934"
                      "96983520312774506326239578318016984801869478851843"
                      "85861560789112949495459501737958331952853208805511"
                      "12540698747158523863050715693290963295227443043557"
                      "66896648950445244523161731856403098711121722383113"
                      "62229893423380308135336276614282806444486645238749"
                      "30358907296290491560440772390713810515859307960866"
                      "70172427121883998797908792274921901699720888093776"
                      "65727333001053367881220235421809751254540594752243"
                      "52584907711670556013604839586446706324415722155397"
                      "53697817977846174064955149290862569321978468622482"
                      "83972241375657056057490261407972968652414535100474"
                      "82166370484403199890008895243450658541227588666881"
                      "16427171479924442928230863465674813919123162824586"
                      "17866458359124566529476545682848912883142607690042"
                      "24219022671055626321111109370544217506941658960408"
                      "07198403850962455444362981230987879927244284909188"
                      "84580156166097919133875499200524063689912560717606"
                      "05886116467109405077541002256983155200055935729725"
                      "71636269561882670428252483600823257530420752963450";
  long long int max = 0, product; // answer exceeds 32 bytes
  int i, j;
  for (i = 0; i < (int)strlen(given) - num; i++)
  {
    product = 1;
    for (j = 0; j < num; j++)
    {
      product *= (given[i + j] - '0');
    }
    max = (product > max) ? product : max;
  }
  return max;
}
