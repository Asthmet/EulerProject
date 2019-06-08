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
