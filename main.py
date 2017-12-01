def problem1():
    sum = 0
    for i in range(1000):
        if ( i%3 == 0 ) or ( i%5 == 0 ):
            sum += i
    print ('Result to problem #1 is: ' + str(sum))

def problem2():
    print ('plop')

def startSolution( pbNumber ):
    print ('Running solution for problem #' + str(pbNumber))
    func_name = 'problem' + str(pbNumber)
    globals()[func_name]()

def main():
    bNumber = input("Which problem do you wish to run?")
    if pbNumber != "exit":
        startSolution(pbNumber)
