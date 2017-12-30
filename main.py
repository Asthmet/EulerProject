# ------------------------------------------------------------------------------
# Modules imports

import math
import array
import time

# ------------------------------------------------------------------------------
# Utility methods

def isPalindrome( number ):
    strNumber = str(number)
    reverseStrNumber = strNumber[::-1]
    if strNumber == reverseStrNumber:
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# Problem methods

def problem1():
    # Find the sum of all the multiples of 3 or 5 below 1000.
    result=0
    for i in range(1000):
        if ( i%3 == 0 ) or ( i%5 == 0 ):
            result += i
    print ('Result to problem #1 is: ' + str(result))

def problem2():
    # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    # print ('plop')
    result = 0
    a1 = 0
    a2 = 1
    while ( (a1 + a2) < 4000000 ):
        if (a1 + a2) % 2 == 0:
            result += a1 + a2
        a2 = a1 + a2
        a1 = a2 - a1
    print ('Result to problem #2 is: ' + str(result))

def problem3():
    # What is the largest prime factor of the number 600851475143 ?
    # debut = time.time()
    maxNumber = 600851475143
    tabPrime = [2, 3, 5]
    root =  math.sqrt( maxNumber )
    for i in range(5, int(float(root)), 2):
        prime = False
        if 600851475143 % i == 0: # if max Number is divisible by i
            for j in tabPrime: # we look in the prime table
                if i%j == 0 and i != j: # if our i number is divisible by a prime, then it isn't a prime itself
                    prime = False
                    break
                prime = True
        if prime == True:
            tabPrime.append(i)

    # The last value in the table should be our answer
    # fin = time.time()
    result = tabPrime[-1]
    print ('Result to problem #3 is: ' + str(result))
    # print('Durée : ' + str(fin - debut))

def problem4():
    # Find the largest palindrome made from the product of two 3-digit numbers.
    result = 0
    for n in range(100, 999, 1):
        for m in range(100, 999, 1):
            if isPalindrome(n * m) == True and result < (n * m):
                result = n * m
    print ('Result to problem #4 is: ' + str(result))

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

    result = 2*2*2*2*3*3*5*7*11*13*17*19
    print ('Result to problem #5 is: ' + str(result))

def problem6():
    # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    sumSquared = 0      # (1 + 2 + ...)^2
    for i in range(1, 101, 1):
        sumSquared += i
    sumSquared = sumSquared * sumSquared

    squareSummed = 0    # 1^2 + 2^2 + ....
    for i in range(1, 101, 1):
        squareSummed += ( i * i )

    result = sumSquared - squareSummed
    print ('Result to problem #6 is: ' + str(result))

def problem7():
    # What is the 10 001st prime number?
    primeTab = [2, 3, 5, 7]
    iteration = 11
    while len(primeTab) <= 10000:
        isPrime = True
        for prime in primeTab:
            if iteration%prime == 0:
                # This iteration is not a prime number
                isPrime = False
                break
        if isPrime == True:
            primeTab.append(iteration)
        iteration += 1

    result = primeTab[-1]
    print ('Result to problem #7 is: ' + str(result))

def problem8():
    pass

# 7316717653133
# 6249192251196744265747423553491949349698352
# 6326239578318
# 18694788518438586156
# 7891129494954595
# 17379583319528532 698747158523863 5 71569329 963295227443 435576689664895 4452445231617318564 3 987111217223831136222989342338 3 81353362766142828 64444866452387493 3589 729629 49156 44 77239 71381 5158593 796 8667 1724271218839987979 87922749219 169972 888 9377665727333  1 5336788122 2354218 975125454 594752243525849 771167 556 13648395864467 632441572215539753697817977846174 6495514929 86256932197846862248283972241375657 56 5749 2614 79729686524145351  4748216637 4844 319989 889524345 6585412275886668811642717147992444292823 863465674813919123162824586178664583591245665294765456828489128831426 769 4224219 22671 556263211111 937 5442175 694165896 4 8 71984 385 96245544436298123 9878799272442849 91888458 1561669 79191338754992  524 6368991256 7176 6 58861164671 94 5 77541  22569831552   559357297257163626956188267 4282524836  82325753 42 75296345


# ------------------------------------------------------------------------------
# Structural method

def startSolution( pbNumber ):
    print ('Running solution for problem #' + str(pbNumber))
    func_name = 'problem' + str(pbNumber)
    if func_name not in globals():
      print ('No solution available for this problem')
    else:
      globals()[func_name]()
    print ('')

def main():
    pbNumber = input("Which problem do you wish to run? ('q' to quit)")
    if pbNumber == "q":
        return
    else:
        startSolution(pbNumber)
        main()

# ------------------------------------------------------------------------------
# Launching happens here

main()
