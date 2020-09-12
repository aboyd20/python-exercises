
def fibonacci( bound ):
    'return first Fibonnaci greater than bound'
    # Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34,...

    prev = 1
    curr = 1

    while curr <= bound:
        # prev becomes curr
        # curr becomes prev+curr
        prev, curr = curr, prev+curr
        #print('prev={0}, curr={1}'.format( prev, curr ) )
        
    return curr

'''
>>> fibonacci( 2 )
3
>>> fibonacci( 13 )
21
>>>
'''


def nextSquare( bound ):
    'return first square greater than bound'

    index = 0
    curr = 0
    
    while curr <= bound:
        index += 1
        curr = index**2

    return curr

'''
>>> nextSquare( 17 )
25
>>> nextSquare( 16 )
25
>>> nextSquare( 0 )
1
'''

