# ------------------------------------------------------------------------------
# Modules imports

import math

# ------------------------------------------------------------------------------
# Utility methods

import utilities as util


# ------------------------------------------------------------------------------
# Problem methods

def problem1():
    # Find the sum of all the multiples of 3 or 5 below 1000.
    result = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            result += i
    print('Result to problem #1 is: ' + str(result))


def problem2():
    # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
    # even-valued terms. print ('plop')
    result = 0
    a1 = 0
    a2 = 1
    while (a1 + a2) < 4000000:
        if (a1 + a2) % 2 == 0:
            result += a1 + a2
        a2 = a1 + a2
        a1 = a2 - a1
    print('Result to problem #2 is: ' + str(result))


def problem3():
    # What is the largest prime factor of the number 600851475143 ?
    # debut = time.time()
    max_number = 600851475143
    tab_prime = [2, 3, 5]
    root = math.sqrt(max_number)
    for i in range(5, int(float(root)), 2):
        prime = False
        if 600851475143 % i == 0:  # if max Number is divisible by i
            for j in tab_prime:  # we look in the prime table
                if i % j == 0 and i != j:  # if our i number is divisible by a prime, then it isn't a prime itself
                    prime = False
                    break
                prime = True
        if prime:
            tab_prime.append(i)

    # The last value in the table should be our answer
    # fin = time.time()
    result = tab_prime[-1]
    print('Result to problem #3 is: ' + str(result))
    # print('Duree : ' + str(fin - debut))


def problem4():
    # Find the largest palindrome made from the product of two 3-digit numbers.
    result = 0
    for n in range(100, 999, 1):
        for m in range(100, 999, 1):
            if util.isPalindrome(n * m) and result < (n * m):
                result = n * m

    print('Result to problem #4 is: ' + str(result))


def problem5():
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    # --- divisible by all number from 1 to 20
    # 1 - out by definition
    # 2 - out because of 4
    # 3 - out because of 6
    # 4 - out because of 8
    # 5 - out because of 10
    # 6 - out because of 12
    # 7 - out because of 14
    # 8 - out because of 16
    # 9 - out because of 18
    # 10 - out because of 20
    # 11 - ok - 11
    # 12 - ok - 2x3x2
    # 13 - ok - 13
    # 14 - ok - 2x7
    # 15 - ok - 3x5
    # 16 - ok - 2x2x2x2
    # 17 - ok - 17
    # 18 - ok - 2x3x3
    # 19 - ok - 19
    # 20 - ok - 2x2x5

    result = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    print('Result to problem #5 is: ' + str(result))


def problem6():
    # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of
    # the sum.

    sum_squared = 0  # (1 + 2 + ...)^2
    for i in range(1, 101, 1):
        sum_squared += i
    sum_squared = sum_squared * sum_squared

    square_summed = 0  # 1^2 + 2^2 + ....
    for i in range(1, 101, 1):
        square_summed += (i * i)

    result = sum_squared - square_summed
    print('Result to problem #6 is: ' + str(result))


def problem7():
    # What is the 10 001st prime number?
    prime_tab = [2, 3, 5, 7]
    iteration = 11
    while len(prime_tab) <= 10000:
        is_prime = True
        for prime in prime_tab:
            if iteration % prime == 0:
                # This iteration is not a prime number
                is_prime = False
                break
        if is_prime:
            prime_tab.append(iteration)
        iteration += 1

    result = prime_tab[-1]
    print('Result to problem #7 is: ' + str(result))


def problem8():
    # Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    complete_string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478" \
                      "8518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295" \
                      "2274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282" \
                      "8064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792" \
                      "2749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013" \
                      "6048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657" \
                      "0560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171" \
                      "4799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224" \
                      "2190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490" \
                      "9188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005" \
                      "593572972571636269561882670428252483600823257530420752963450 "
    result = 0

    for i in range(0, 987):
        # print(complete_string[i:i+13])
        iter_sum = util.multipleAll13(complete_string[i:i + 13])
        if iter_sum > result:
            result = iter_sum

    print('Result to problem #8 is: ' + str(result))


def problem9():
    # Find the product ( a*b*c ) such as:
    #   a*a + b*b = c*c
    #   a + b + c = 1000
    #   and a < b < c
    result = 0
    for a in range(1000):
        for b in range(a, int((1000 - a) / 2), 1):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                result = a * b * c
                break
    print('Result to problem #9 is: ' + str(result))


def problem10():
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    # Find the sum of all the primes below two million.
    prime_tab = [2, 3, 5, 7]
    iteration = 11
    last_max = 0
    result = 17
    while iteration <= 2000000:
        if iteration % 1000 == 0:
            print('Iteration: ' + str(iteration) + ' - Max prime: ' + str(last_max))
        is_prime = True
        for prime in prime_tab:
            if prime > math.sqrt(iteration):
                break
            if iteration % prime == 0:  # or
                # This iteration is not a prime number
                is_prime = False
                break
        if is_prime:
            prime_tab.append(iteration)
            last_max = prime_tab[-1]
            result += iteration
        iteration += 2

    # for prime in primeTab:
    #     result += prime
    # print(primeTab[0])
    print('Result to problem #10 is: ' + str(result))


def problem11():
    # In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
    # What is the greatest product of four adjacent numbers in the same direction 
    # (up, down, left, right, or diagonally) in the 20x20 grid?

    matrix_table = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
                    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
                    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
                    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
                    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
                    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
                    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
                    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
                    [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
                    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
                    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
                    [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
                    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
                    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
                    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
                    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
                    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
                    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
                    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

    # print( matrix_table[0] )
    result = 0
    for i in range(20):
        for j in range(20):
            if i < 15:
                product = matrix_table[i][j] * matrix_table[i + 1][j] * matrix_table[i + 2][j] * matrix_table[i + 3][j]
                if product > result:
                    result = product
            if j < 15:
                product = matrix_table[i][j] * matrix_table[i][j + 1] * matrix_table[i][j + 2] * matrix_table[i][j + 3]
                if product > result:
                    result = product
            if i < 15 and j < 15:
                product = matrix_table[i][j] * matrix_table[i + 1][j + 1] * matrix_table[i + 2][j + 2] * \
                          matrix_table[i + 3][j + 3]
                if product > result:
                    result = product
            if i < 15 and j > 5:
                product = matrix_table[i][j] * matrix_table[i + 1][j - 1] * matrix_table[i + 2][j - 2] * \
                          matrix_table[i + 3][j - 3]
                if product > result:
                    result = product

    print('Result to problem #11 is: ' + str(result))


def problem12():
    # We can see that 28 is the first triangle number to have over five divisors.
    # What is the value of the first triangle number to have over five hundred divisors?
    i = 1
    divisors_count = 1
    while divisors_count < 500:
        i += 1


# ------------------------------------------------------------------------------
# Structural method

def start_solution(pb_number):
    print('Running solution for problem #' + str(pb_number))
    func_name = 'problem' + str(pb_number)
    if func_name not in globals():
        print('No solution available for this problem')
    else:
        globals()[func_name]()
    print('')


def main():
    pb_number = input("Which problem do you wish to run? ('q' to quit)")
    if pb_number == "q":
        return
    else:
        start_solution(pb_number)
        main()


# ------------------------------------------------------------------------------
# Launching happens here

main()
