def problem1():
    sum = 0
    for i in range(1000):
        if ( i%3 == 0 ) or ( i%5 == 0 ):
            sum += i
    print ('Result to problem #1 is: ' + str(sum))

def problem2():
    print ('plop')

def startSolution( pbNumber ):
    # print 'Running solution for problem #' + pbNumber
    func_name = 'problem' + self.pbNumber
    func = getattr( self, func_name )
    func()

startSolution(1)
