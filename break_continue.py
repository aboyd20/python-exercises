
def breakOneLoop():
    'prints numbers in list until it encounters first even number'

    lst = [ 1,3,23,8,5,20,17 ]
    for i in lst:
        if i%2 == 0: # if i is even
            break # terminate for loop

        print( i, end=' ')

'''
>>> breakOneLoop()
1 3 23
'''

def breakNestedLoop():
    'prints product of lst1 * lst2 until it encounters value of 6'

    for i in range( 1,5 ): # outer loop
        for j in range( 1, 4 ): # inner loop
            print( 'i={0}, j={1}'.format( i,j ), end=' ' ) # show current values

            prod = i*j
            if prod == 6: # terminate inner loop
                print()
                break

            print( 'prod: {0}'.format( prod ) )

        print() # print new line

'''
>>> breakNestedLoop()
i=1, j=1 prod: 1
i=1, j=2 prod: 2
i=1, j=3 prod: 3

i=2, j=1 prod: 2
i=2, j=2 prod: 4
i=2, j=3 

i=3, j=1 prod: 3
i=3, j=2 

i=4, j=1 prod: 4
i=4, j=2 prod: 8
i=4, j=3 prod: 12

>>>
'''

def continueOneLoop():
    'skip the even numbers in the for loop'

    lst = [ 1,3,23,8,5,20,17 ]

    for i in lst:
        if i%2 == 0: # if i is even
            continue # terminate current iteration

        print( i, end=' ')

'''
>>> continueOneLoop()
1 3 23 5 17 
>>>
'''

def continueWhileLoop():
    'skip the even numbers in the while loop'

    lst = [ 1,3,23,8,5,20,17 ]

    i = 0
    while i < len( lst ):
        if lst[ i ] %2 == 0: # if i is even
            i += 1
            continue # terminate current iteration

        print( lst[ i ], end=' ')
        i += 1   

'''
>>> continueWhileLoop()
1 3 23 5 17 
>>>
'''

def continueNestedLoop():
    'prints products of lst1 * lst2, except when product = 6'

    for i in range( 1,5 ): # outer loop
        for j in range( 1, 4 ): # inner loop
            print( 'i={0}, j={1}'.format( i,j ), end=' ' ) # show current values

            prod = i*j
            if prod == 6: # terminate inner loop
                print()
                continue

            print( 'prod={0}'.format( prod ) )

        print() # print new line

'''
>>> continueNestedLoop()
i=1, j=1 prod=1
i=1, j=2 prod=2
i=1, j=3 prod=3

i=2, j=1 prod=2
i=2, j=2 prod=4
i=2, j=3 

i=3, j=1 prod=3
i=3, j=2 
i=3, j=3 prod=9

i=4, j=1 prod=4
i=4, j=2 prod=8
i=4, j=3 prod=12

>>>
'''
