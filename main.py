# ------------------------------------------------------------------------------
# Modules imports

import math
import array

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
            result += a1 +a2
        a2 = a1 + a2
        a1 = a2 - a1
    print ('Result to problem #2 is: ' + str(result))

def problem3():
    # What is the largest prime factor of the number 600851475143 ?
    maxNumber = 600851475143
    tabPrime = [2, 3, 5]
    root =  math.sqrt( maxNumber )
    for i in range(5, int(float(root))):
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
    result = tabPrime[-1]
    print ('Result to problem #3 is: ' + str(result))

def problem4():
    # Find the largest palindrome made from the product of two 3-digit numbers.
    result = 0
    for n in range(100, 999, 1):
        for m in range(100, 999, 1):
            if isPalindrome(n * m) == True and result < (n * m):
                result = n * m
    print ('Result to problem #4 is: ' + str(result))

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
    pbNumber = input("Which problem do you wish to run? ('exit' to quit)")
    if pbNumber == "exit":
        return
    else:
        startSolution(pbNumber)
        main()

# ------------------------------------------------------------------------------
# Launching happens here

main()
