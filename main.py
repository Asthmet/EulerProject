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

def multipleAll13( numString ):
    multiplication = 1
    if len(numString) != 13:
        return 0
    for i in range(13):
        if numString[i] == 0:
            multiplication = 0
            break
        else:
            multiplication *= int(numString[i])
    return multiplication

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
    # Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    completeString = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    result = 0

    for i in range(0, 987):
        # print(completeString[i:i+13])
        iterSum = multipleAll13(completeString[i:i+13])
        if iterSum > result :
            result = iterSum

    print ('Result to problem #8 is: ' + str(result))

def problem9():
    # Find the product ( a*b*c ) such as:
    #   a*a + b*b = c*c
    #   a + b + c = 1000
    #   and a < b < c
    for a in range(1000):
        for b in range(a, int((1000-a)/2), 1):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                result = a*b*c
                break
    print ('Result to problem #9 is: ' + str(result))

def problem10():
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    # Find the sum of all the primes below two million.
    primeTab = [2, 3, 5, 7]
    iteration = 11
    lastMax = 0
    result = 0
    while iteration <= 2000000:
        print('iteration: ' + str(iteration) + ' - max prime: ' + str(lastMax))
        isPrime = True
        for prime in primeTab:
            if prime > math.sqrt( iteration ):
                break
            if iteration%prime == 0: # or
                # This iteration is not a prime number
                isPrime = False
                break
        if isPrime == True:
            primeTab.append(iteration)
            lastMax = primeTab[-1]
            result += iteration
        iteration += 2

    # for prime in primeTab:
    #     result += prime
    print(primeTab[-1])
    print ('Result to problem #10 is: ' + str(result))

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
