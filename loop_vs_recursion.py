
def sumEvenLoop( n ):
    '''
    return sum of even numbers from 0 to n;
    return 0 for n < 1
    '''
    total = 0 # identity for addition
    for i in range( 0, n+1, 2 ):
        total += i
        
    return total

def sumEvenRecursive( n ):
    '''
    return sum of even numbers from 0 to n;
    return 0 for n < 1
    '''
    print(n)
    if n < 1: # base case
        return 0

    elif n%2 != 0: # recursive case
        return sumEvenRecursive( n-1 )

    else:
        # recursive case: total = current n + remaining even integers < n
        return n + sumEvenRecursive( n-2 )


def prodLoop( lst ):
    '''
    return product of numbers in lst;
    return 1 if lst is empty
    '''
    prod = 1
    for num in lst:
        prod *= num

    return prod


def prodRecursive( lst ):
    '''
    return product of numbers in lst;
    return 1 if lst is empty
    '''
    if not lst: # lst == [] base case
        return 1

    elif len( lst ) == 1: # base case
        return lst[ 0 ]

    else:
        # recursive case: prod = next item * product of remaining items
        return lst[0] * prodRecursive( lst[ 1: ] )


def factorialLoop( n ):
    '''
    return factorial of number >= 0
    '''
    if n < 0:
        print( 'n must be a number >= 0' )
        return
    
    fact = 1
    for i in range( 2, n+1 ):
        fact = fact * i
            
    return fact
			
        
def factorialRecursive( n ):
    'return factorial of number >= 0'
	
    if n < 0:
        print( 'n must be a number >= 0' )
        return
    
    if n == 0: # base case 0! = 1
        return 1

    else:
        # recursive case: n! = n * (n-1)!
        return n * factorialRecursive( n - 1 )
            
    
def palindromeLoop( word ):
    '''
    return True if word is a palindrome;
    otherwise False
    '''
    for i, char in enumerate( word ):
        if char != word[ -i-1 ]:
            return False

    return True


def palindromeRecursive( word ):
    '''
    return True if word is a palindrome;
    otherwise False
    '''
    if len( word ) < 1: # word == '' base case
        return True

    else:
        if word[ 0 ] == word[ -1 ]:
            # recursive case: if first and last character match, is middle a palindrome
            return palindromeRecursive( word[ 1:-1 ] )

        else:
            # if first and last character do not match, return false
            return False


        
