import math
import datetime
import functools


def euler1(n=1000):
    """
    Multiples of 3 and 5. ProjectEuler defaults to 1000
    """
    # brute force
    # sum = 0
    # for i in range(3, n, 3):
    #     sum += i
    # for i in range(5, n, 5):
    #     if i % 3 != 0:
    #         sum += i
    # return sum

    # can do by using math
    # sum of arithmetic progression floor(n / d)/2[a + z],
    # where d - difference between terms, a - first term, z - last term
    n -= 1
    return int(
        (n // 3) / 2 * (3 + n - (n % 3))
        + (n // 5) / 2 * ((n - n % 5) + 5)
        - (n // 15) / 2 * ((n - n % 15) + 15)
    )


def euler2(n=4000000):
    """
    Even Fibonacci numbers. ProjectEuler defaults to 4 million
    """
    t1 = t2 = 1
    c = t1 + t2
    total = 0
    while c < n:
        total += c
        t1 = t2 + c
        t2 = t1 + c
        c = t1 + t2
    return total


def euler3(n=600851475143):
    """
    Largest Prime Factor for 600851475143
    """

    factor = 0
    count = 2
    while count ** 2 <= n:
        if n % count == 0:
            n /= count
            factor = count
        else:
            count += 1
    if n > factor:
        return int(n)
    return int(factor)


def euler4():
    """
    Largest Palindrome Product of 2 three digit numbers
    """

    biggest = 0
    for i in range(999, 100, -1):
        for j in range(990, 100, -11):
            x = str(i * j)
            if int(x) > biggest and x == x[::-1]:
                # print(x, i, j)
                biggest = int(x)
    return biggest


def is_prime(n: int):
    """
    checks if a number is prime, only need to check up to square root of n (inclusive)
    """

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def euler5(n=20):
    """
    Smallest multiple of all numbers 1 to n, euler default 20
    """

    # Brute force
    # i = n * 2
    # while 1:
    #     for j in range(2, n + 1):
    #         if i % j != 0:
    #             break
    #         else:
    #             if j == n:
    #                 return i
    #     i += n
    # find prime factorization of all terms up to n
    l = [0] * n
    for i in range(2, n + 1):
        num = i
        div = 2
        count = 0
        while num != 1:
            if num % div == 0:
                count += 1
                num = num // div
            else:
                if l[div - 1] < count:
                    l[div - 1] = count
                div += 1
                count = 0
        if l[div - 1] < count:
            l[div - 1] = count
    out = 1
    for i in range(len(l)):
        out *= (i + 1) ** l[i]
    return out


def euler6(n=100):
    """
    Difference of sum of squares and square of sum, default 100
    """

    sum_square = n * (n + 1) * (2 * n + 1) / 6
    square_sum = (n * (n + 1) / 2) ** 2
    return int(square_sum - sum_square)


def euler7(n=10001):
    """
    Ten Thousandth and first prime number, default 10001

    By allocation some memory for your 10001 primes and storing them as you find them
    test every odd number after the last calculated prime against
    all previous calculated primes that are below sqrt(n) for the number you are testing.
    able to calculate the first 1 000 000 primes in 20 seconds
    """
    # brute force
    # count = 6
    # i = 13
    # while count != n:
    #     i += 2
    #     if is_prime(i):
    #         count += 1
    # return i
    # possibly more elegant ?
    prime_list = [None] * n
    prime_list[0] = 2
    prime_list[1] = 3
    index = 2
    while index < n:
        i = (
            prime_list[index - 1] + 2
        )  # start at most recent prime, increase by 2 to check only odds
        while 1:
            prime = True
            for j in range(1, index):
                if prime_list[j] > int(i ** 0.5):
                    break
                elif i % prime_list[j] == 0:
                    prime = False
                    break
            if prime:
                prime_list[index] = i
                index += 1
                break
            else:
                i += 2
    return prime_list[n - 1]


def euler8(n=13):
    """
    Greatest product of n adjacent integers, default 13
    """

    given = (
        "73167176531330624919225119674426574742355349194934"
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
        "71636269561882670428252483600823257530420752963450"
    )
    maximum = 0
    for i in range(len(given) - n):
        product_list = [int(char) for char in given[i : i + n]]
        product = 1
        for j in product_list:
            product *= j
        if product > maximum:
            maximum = product

    return maximum


def euler9(num=1000):
    """
    Special Pythagorean triplet, a^2 + b^2 = c^2, default case a + b + c = 1000
    """

    # brute force, don't need to double check previous (a,b) combos
    # for a in range(1, num):
    #     for b in range(a, num):
    #         c = (a ** 2 + b ** 2) ** 0.5
    #         if c % 1 == 0:
    #             c = int(c)
    #             if a + b + c == num:
    #                 print(a, b, c)
    #                 return a * b * c

    # math it a bit, can manipulate starter info a + b + c = 1000 into
    # (500000 - 1000 * b) / (1000 - b) = a; thus can just check a
    # for b in range(1, num):
    #     a = ((num ** 2) / 2 - num * b) / (num - b)
    #     if a % 1 == 0:
    #         a = int(a)
    #         # print("testing", a, b, int(a * a + b * b) ** 0.5)
    #         return a * b * int((a * a + b * b) ** 0.5)

    # using Euclid Algorithm, where all pythagorean triples are in relation to integers m, n, k
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    # b = 2mn; a = m^2 -n^2; c = m^2 + n^2;
    # a + b + c = num
    # 2mn + 2m^2 = num
    for m in range(1, num):
        for n in range(1, m):
            if m * (m + n) == num / 2:
                return 2 * m * n * (m ** 2 - n ** 2) * (m ** 2 + n ** 2)


def euler10(n=2000000):
    """
    Summation of primes, default below 2 million
    """

    # brute force first
    # sum = 2
    # for i in range(3, n, 2):
    #     if is_prime(i):
    #         sum += i
    # return sum
    # Sieve Mk1
    sieve = [0] * math.ceil(n / 2)
    sieve[0] = 1  # the number 1 isn't prime
    bound = (n - 1) // 2
    limit = (math.floor(math.sqrt(n)) - 1) // 2
    for i in range(1, limit + 1):
        if (
            sieve[i] == 0
        ):  # sieve range is cut in half, so this actually corresponds to the number 2*i + 1
            for j in range(2 * i * (i + 1), bound + 1, 2 * i + 1):
                sieve[j] = 1
    return 2 + sum([(2 * x) + 1 for x in range(len(sieve)) if sieve[x] == 0])


def euler11():
    """
    Largest product in a grid,
    """
    # fmt: off
    given = [
        8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,
        49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00,
        81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,
        52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,
        22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,
        24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,
        32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,
        67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,
        24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,
        21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95,
        78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,
        16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57,
        86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,
        19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,
        4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,
        88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,
        4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,
        20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,
        20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,
        1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,
    ]
    # fmt: on

    dimension = 20
    grid = [given[dimension * i : dimension * i + dimension] for i in range(20)]
    multiply = lambda x, y: x * y
    horiz_max = max(
        [
            functools.reduce(multiply, grid[i][j : j + 4])
            for i in range(dimension)
            for j in range(dimension - 3)
        ]
    )
    vert_max = max(
        [
            functools.reduce(multiply, [grid[i + i_hat][j] for i_hat in range(4)])
            for i in range(dimension - 3)
            for j in range(dimension)
        ]
    )
    diag_r_max = max(
        [
            functools.reduce(multiply, [grid[i + d][j + d] for d in range(4)])
            for i in range(dimension - 3)
            for j in range(dimension - 3)
        ]
    )
    diag_l_max = max(
        [
            functools.reduce(multiply, [grid[i + d][j - d] for d in range(4)])
            for i in range(dimension - 3)
            for j in range(dimension - 1, 2, -1)
        ]
    )

    return max(horiz_max, vert_max, diag_r_max, diag_l_max)


def euler12(n=500):
    """
    Highly divisible triangular number, default 500 divisors
    """

    # brute force
    triangle = 28
    natural = 8
    while 1:
        div = 1
        for i in range(2, int(math.sqrt(triangle)) + 1):
            if triangle % i == 0:
                div += 2
            if triangle == i * i:
                div -= 1
        if div >= n:
            return triangle
        triangle += natural
        natural += 1


def euler13(n=10):
    """
    Large sum, only wants first 10 digits
    """

    given = [
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690,
    ]
    return int(str(sum(given))[:n])


def euler14(n=1000000) -> int:
    """Longest Collatz sequence

    if n is even, n = n / 2
    if n is odd, n = 3 * n + 1
    if n == 1, stop
    So if we start at 13, the sequence would be 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1. Giving length 10

    Parameters
    ----------
    n : int, optional
        starting number must be under this, by default 1000000

    Returns
    -------
    int
        starting number, which is less than n, which produces longest Collatz sequence
    """
    # * Cool Note
    # * if n is a power of 2, it gives us that exponent more in the sequence.
    # * n = 16 (2 ** 4), will give us 4 more terms and then it reaches 1

    # brute force through every number under n
    # max_len = 0
    # max_start: int = -1
    # for i in range(2, n):
    #     length = 1
    #     n: int = i
    #     while n != 1:
    #         if n % 2 == 0:
    #             n = n // 2  # type hinting needs this floor divide
    #         else:
    #             n = 3 * n + 1
    #         length += 1
    #     if length > max_len:
    #         max_len = length
    #         max_start = i
    # print(max_len, max_start)
    # return max_start

    # lets use some extra memory to go faster, with dictionary
    def chain(x):
        if d.get(x, 0):
            return d[x]
        if x % 2 == 0:
            d[x] = 1 + chain(x / 2)
        else:
            # odd number + 1 will create even, so skip a calc
            d[x] = 2 + chain((3 * x + 1) / 2)
        return d[x]

    d = dict()
    d[1] = 1
    longest, ret = 0, -1
    # don't need to check below halfway, since it maps to a number double it
    for i in range(n // 2, n):
        if chain(i) > longest:
            longest = chain(i)
            ret = i
    return ret


def euler15(n=20) -> int:
    """Lattice paths

    Starting in the top left corner of a n x n grid
    Only being able to move right or down, find total number of routes
    In simpler terms: choose the rth term of the n-th row of Pascal's triangle

    Parameters
    ----------
    n : int, optional
        size of square grid, by default 20

    Returns
    -------
    int
    """
    # recursive answer
    # def routes(row, col):
    # if row == 0 or col == 0:
    # return 1
    # if d.get((row, col), 0):
    # return d[(row, col)]
    # d[(row, col)] = routes(row - 1, col) + routes(row, col - 1)
    # return d[(row, col)]
    # d = dict()
    # return routes(20, 20)

    # iterative answer, essentially dynamic programming tabulation
    # grid = [[0] * n for _ in range(n)]
    # for i in range(len(grid)):
    #     for j in range(len(grid)):
    #         if i == 0:
    #             grid[i][j] = 1
    #         elif j == 0:
    #             grid[i][j] = 1
    #         else:
    #             grid[i][j] = grid[i - 1][j - 1]
    # return grid[n][n]
    # simple math
    """since there are a total of 2n instructions, we do permutation(2n, 2n) == 2n!
    but the instructions aren't unique (any right could be replaced with another right)
    so we should be doing combinations, with 2n choosing n, since the remaining must take the open spots
    Think of it like choosing which spots the Right's will go, the Down's must take the remaining with no choice
    """
    return math.comb(2 * n, n)


def euler16(n=1000) -> int:
    """Power digit sum

    Return the sum of digits that comprise the power of 2^n

    Parameters
    ----------
    n : int, optional
        exponent, by default 1000

    Returns
    -------
    int
    """
    return sum([int(c) for c in str(2 ** n)])


def euler17(n=1000) -> int:
    """Number letter counts

    Return the number of letters (ignore whitespace/special characters)
    That are used when creating the English versions of the numbers 1 to n, inclusive
    Returns 0 if n < 1
    Will raise IndexError for numbers greater than 999 billion
    Example: euler17(5) == 19 # one (3) two (3) three (5) four (4) five (4)

    Parameters
    ----------
    n : int, optional
        number to count up to inclusive, by default 1000

    Returns
    -------
    int
    """
    # no super elegant way of doing this

    words_dict = dict(
        [
            (0, 0),
            (1, 3),
            (2, 3),
            (3, 5),
            (4, 4),
            (5, 4),
            (6, 3),
            (7, 5),
            (8, 5),
            (9, 4),
            (10, 3),
            (11, 6),
            (12, 6),
            (13, 8),
            (14, 8),
            (15, 7),
            (16, 7),
            (17, 9),
            (18, 8),
            (19, 8),
            (20, 6),
            (30, 6),
            (40, 5),  # note: this problem is in American english, forty
            (50, 5),
            (60, 5),
            (70, 7),
            (80, 6),
            (90, 6),
        ]
    )
    thousands = [0, 8, 7, 7]

    def helper(n):
        if n == 0:
            return 0
        elif n < 20:
            return words_dict[n]
        elif n < 100:
            return words_dict[n - n % 10] + helper(n % 10)
        else:
            return (
                words_dict[n // 100]
                + 7
                + ((3 + helper(n % 100)) if n % 100 != 0 else 0)
            )

    if n < 1:
        return 0

    ans = 0
    for num in range(n + 1):
        i = 0
        while num > 0:
            if num % 1000 != 0:
                ans += helper(num % 1000) + thousands[i]
            i += 1
            num //= 1000

    return ans


def euler18() -> int:
    """Maximum path sum I

    Starting at the top of the given triangle
    Find the path that yields the maximum sum of numbers
    while only able to move to adjacent numbers on the row below.
    For any index j in a row, can go to either j or j+1 in the row below.

    Returns
    -------
    int
    """
    given = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    def helper(i, j, memo=None):
        if memo is None:
            memo = dict()
        if i >= len(given) or j >= len(given[i]):
            return 0
        elif (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = given[i][j] + max(
            helper(i + 1, j, memo), helper(i + 1, j + 1, memo)
        )
        # print(f"level{i} returning {memo[(i,j)]}")
        return memo[(i, j)]

    return given[0][0] + max(helper(1, 0), helper(1, 1))


def euler19(n: int = 2000) -> int:
    """Counting Sundays

    Given that Jan 1 1900 was a Monday, find the number of
    Sundays that occurred on the first of the month from Jan 1 1901 up to end of year n.

    Parameters
    ----------
    n : str, optional
        string of format 'YYYY' to represent date, by default "2000"

    Returns
    -------
    int
    """

    # just use a datetime module to find what weekday the first of each month was
    return sum(
        [
            datetime.date(year, month, 1).isoweekday() == 7
            for year in range(1901, n + 1)
            for month in range(1, 13)
        ]
    )


def euler20(n=100) -> int:
    """Factorial digit sum

    Factorial of n! returns an int, return the sum of the digits of that int
    For n = 10, euler20(n) -> 27

    Parameters
    ----------
    n : int, optional
        by default 100

    Returns
    -------
    int
    """
    return sum([int(s) for s in str(math.factorial(n))])


def euler21(n=10000) -> int:
    """Amicable numbers

    Let d(n) be defined as the sum of proper divisors of n.
    If d(a) = b, d(b) = a, and a != b, then a and b are an amicable pair, or each are an amicable number.
    Return the sum of all amicable numbers less than n
    For n = 10, euler21(n) -> 0

    Parameters
    ----------
    n : int, optional
         by default 10000

    Returns
    -------
    int
    """
    # have to find sum of all the divisors of each number that we stop at
    # 1 is not a proper divisor of itself, since they are equal
    memo = {1: 0}

    def sum_divisors(num):
        start = 1
        if num not in memo:
            # everything is divisible by 1, but can not include n in proper divisors
            root = int(math.sqrt(num))
            if num % root == 0:
                # if perfect square, can only count its divisor once
                start += root
                root -= 1
            memo[num] = start + sum(
                [
                    s + num // s
                    for s in range(2, int(math.sqrt(num)) + 1)
                    if num % s == 0
                ]
            )
        return memo[num]

    # for each number, we find the sum of the divisors
    # then if the sum of the divisors of that sum is equal to the number we store them
    # d(d(a)) = a and we want all 'a' that satisfy that
    return sum(
        [
            a
            for a in range(2, n)
            if sum_divisors(sum_divisors(a)) == a and sum_divisors(a) != a
        ]
    )


def euler22() -> int:
    """Names Scores

    Using the provided text file '../data/p022_names.txt' read in the names, sort the names
    obtain the alphabetical value for a name and multiply by its index. Return the sum of all the name scores
    e.g. the name 'ALONSO' at index 938, would have alphabetical value 76 and then be multiplied by 938
    ALONSO - 1 + 12 + 15 + 14 + 19 + 15 = 76

    Returns
    -------
    int
    """

    def name_val(s: str) -> int:
        # all names are capital, so use 64 in ascii value
        return sum([ord(c) - 64 for c in s if c != '"'])

    with open("data/p022_names.txt", "r") as f:
        data = f.read()  # it is one line
    data = sorted(data.split(","))
    return sum([i * name_val(name) for i, name in enumerate(data, start=1)])


def euler23(n=28123) -> int:
    """Non-abundant sums

    Return the sum of all positive integers, less than equal to n, which cannot be written as the sum of two abundant numbers
    An abundant number is one whose proper divisors sum to a value greater than the number. e.g. 12 is abundant, 1 + 2 + 3 + 4 + 6 = 16
    Mathematical analysis show that all integers greater than 28123 can be written as a sum of two abundant numbers
    ### https://mathschallenge.net/full/sum_of_two_abundant_numbers
    Find all abundant numbers up to n, then create sums of those abundant numbers. Then for i up to n, if it is not a sum, add it to total

    Parameters
    ----------
    n : int, optional
        limit to find abundant number up to (inclusive), by default 28123

    Returns
    -------
    int
    """

    def is_abundant(num):
        copy = num
        total, p = 1, 2
        while 1 < p * p <= num:
            if num % p == 0:
                j = p * p
                num = num // p
                while num % p == 0:
                    j *= p
                    num //= p
                total *= j - 1
                total //= p - 1
            if p == 2:
                p = 3
            else:
                p += 2
        if num > 1:
            total *= num + 1
        # sum of all divisors - n = sum of proper divisors
        # rewritten: sum of all divisors = sum of proper divisors + n
        return total > 2 * copy

    abundant = [i for i in range(2, n + 1) if is_abundant(i)]
    abundant_sum = set(
        [abundant[i] + abundant[j] for i in range(len(abundant)) for j in range(i + 1)]
    )

    return sum([s for s in range(n + 1) if s not in abundant_sum])


def euler24(n=1000000) -> int:
    """Lexicographic Permutations

    Return the nth lexicographic permutation of the digits 0 thru 9.
    In this case I believe lexicographic to also mean increasing.

    Parameters
    ----------
    n : int, optional
        term to be returned, by default 1000000

    Returns
    -------
    int
    """
    """
    creating all 3.6 million permutations seems a little troublesome for a computer
    return int(
        "".join(sorted(list(itertools.permutations([c for c in "0123456789"])))[n - 1])
    )

    # this method might use less memory, but it shows that with lexicographic input to permutations
    # there is no need to sort the output of it
    perm_count = 0

    def filter_helper(num):
        nonlocal perm_count
        if perm_count == (n - 1):
            return True
        else:
            perm_count += 1
            return False

    return int(
        "".join(
            next(
                filter(filter_helper, itertools.permutations([c for c in "0123456789"]))
            )
        )
    )
    lets make a method to actually develop the permutations
    """
    # other implementations above
    def permute(num_list, left, right):
        """Will add all results to an existing list
        Switch the leftmost available spot with the next one, recurse, then reset to previous state"""
        if left == right:
            results_list.append("".join(num_list))
        else:
            for i in range(left, right + 1):
                num_list[left], num_list[i] = num_list[i], num_list[left]
                permute(num_list, left + 1, right)
                num_list[left], num_list[i] = num_list[i], num_list[left]

    results_list = []
    permute(list("0123456789"), 0, 9)
    results_list.sort()
    return int(results_list[n - 1])


def euler25(n: int = 1000) -> int:
    """1000 Digit Fibonacci number

    Fibonacci sequence defined as F(1) = 1, F(2) = 1, find the index of the first Fibonacci number to have 1000 digits.

    Parameters
    ----------
    n : int, optional
        number of digits to have, by default 1000

    Returns
    -------
    int
    """
    f_i, f_j = 1, 1
    index = 1  # corresponds to f_i
    while len(str(f_i)) < n:
        index += 1
        f_i, f_j = f_j, f_j + f_i
    return index


def euler26(n: int = 1000) -> int:
    """Reciprocal cycles

    A unit fraction is one with a one in the numerator. Find d, d < n, such that the unit fraction of d has the longest repeating cycle
    A repeating cycle like 1 / 7 = 0.(142857)... where repeats infinitely.

    Parameters
    ----------
    n : int, optional
        Limit to find denominator under, by default 1000

    Returns
    -------
    int
    """
    """
    # idea is that we keep doing long division until a value repeats itself
    longest_cycle, cycle_num = 0, 0
    for i in range(n - 1, 1, -1):
        # since i is decreasing, can't create longer cycles later on
        if longest_cycle >= i:
            break
        remainder_list = [0] * i
        # start at 1 because unit fraction, the first remainder is always 1
        numerator_val = 1
        position = 0
        while remainder_list[numerator_val] == 0 and numerator_val != 0:
            remainder_list[numerator_val] = position
            numerator_val = (numerator_val * 10) % i
            position += 1
        # comparison isn't just position > longest_cycle
        # because the repetition might not start at 0
        if position - remainder_list[numerator_val] > longest_cycle:
            longest_cycle = position - remainder_list[numerator_val]
            cycle_num = i

    return cycle_num
    """
    # less memory intensive method
    def recurring_cycle(d):
        # solve 10^s % d == 10^(s+t) % d
        # where t is length and s is start
        # signifies how many times do we multiply by 10 until we reach a repeating val
        for s in range(d - 1):
            for t in range(1, d):
                if 10 ** s % d == 10 ** t % d:
                    return t
        return 0

    longest = max(recurring_cycle(i) for i in range(2, n))
    return [i for i in range(2, n) if recurring_cycle(i) == longest][0]


def euler27(num: int = 1000) -> int:
    """Quadratic Primes

    Using a quadratic formula of format n^2 + an + b, find the product of the coefficients (a * b) for the pairing
    that creates the maximum number of consecutive primes starting at n = 0. abs(a) must be less than value of num while abs(b) less than equal to num.
    E.g. n^2 + n + 41 yields primes for 0 <= n <= 39

    Parameters
    ----------
    num : int, optional
        Limit to the coefficients, by default 1000

    Returns
    -------
    int
    """
    # brute force very fast since is_prime is somewhat optimized
    consec_prime = 0
    coeff_prod = 0
    # easiest base cases are that when n = 0, b must be prime
    # a must be odd for n = 1, e.g. 1^2 + a + b = prime number, where we know b is a prime
    # b is odd as prime numbers > 2 are odd
    num = abs(num)
    offset = 1 if num % 2 == 0 else 0
    # make sure we start at an odd number and go thru every odd
    for a in range(-num + offset, num + (1 - offset), 2):
        # negative numbers are not prime so can shorten this range
        for b in [i for i in range(2, num + 1) if is_prime(i)]:
            n = 0
            while is_prime(int(n ** 2 + a * n + b)):
                n += 1
                if b == n:
                    break
            if n > consec_prime:
                consec_prime = n
                coeff_prod = a * b
    return coeff_prod


def euler28(n: int = 1001) -> int:
    """Number spirals diagonals

    Starting with the number 1 and moving clockwise to the right, can create a number spiral.
    A 3 x 3 grid would look like:
        7 8 9
        6 1 2
        5 4 3
    And the sum across the diagonals would be 25. For a n x n grid, find the sum of the diagonals

    Parameters
    ----------
    n : int, optional
        size of grid n x n, by default 1001

    Returns
    -------
    int
        sum of both diagonals
    """
    # * should be a simple mathematical way of doing
    # top right diagonal to center is sum of the dimension squared for odds from 3 to n
    # can use dimension of that point to find the other 3 corners.
    total = 1
    for dim in range(3, n + 1, 2):
        for i in range(4):
            total += dim * dim - i * (dim - 1)
    return total
