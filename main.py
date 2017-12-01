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
        if (a1 + a2)%2 == 0:
            result += a1 +a2
        a2 = a1 + a2
        a1 = a2 - a1
    print ('Result to problem #2 is: ' + str(result))

def problem3():
    # What is the largest prime factor of the number 600851475143 ?

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
