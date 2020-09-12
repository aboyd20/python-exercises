
def printHalves( n ):
    '''
    this function calculates of sequence of numbers as follows:
    it starts with n and replaces n with the integer halve. what
    does that mean? if n is odd number, say 9, the integer halve
    is 4, not 4.5.  the function keeps halving until it hits
    n == 1, printing all the values of n it gets along the way.

    instead of while or for loop, we use recursion
    '''

    print( n ) # print all values of n, including last value of 1

    if n == 1: # base case
        return

    else: # recursive step
        return printHalves( n // 2 )

'''test runs
>>> printHalves(8)
8
4
2
1
>>> printHalves( 5 )
5
2
1
>>>
'''
