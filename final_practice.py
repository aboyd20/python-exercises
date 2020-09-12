
def trace():
    lst = list( range (0, 8) )
    print( lst )
    for i in range( 1, len(lst) ):
        print( lst[i], end = "?" )


def trace1():
    '''
    returns largest index of the smaller number
    in consecutive pairs in lst (lst[i-1], lst[i])
    '''
    lst = list( range( 4, -7, -3 ) )
    lst.append( 20 )
    lst.append( -12 )
    lst.append( 5 )
    lst.append( -7 )
    print( lst )
    indexOfLeastPair = -1
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            indexOfLeastPair = i

    print(indexOfLeastPair)

def trace11():
    'returns index of smallest value in lst'
    lst = list( range( 4, -7, -3 ) )
    lst.append( 20 )
    lst.append( -12 )
    lst.append( 5 )
    lst.append( -7 )
    print( lst )
    indexOfLeast = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[indexOfLeast]:
            indexOfLeast = i

    print(indexOfLeast)

def trace2():
    lst = [1,-5,4,2]
    total = sum( lst )
    index = 0
    while index < len(lst):
        index += 1
        print( 'index =', index )
        total += index
        print( 'total =', total )
        if total >= 4: 
            continue
        index += 1

    print(total)

def trace3():
    lst = [1,-5,4,2]
    total = sum( lst )
    index = 0
    while index < len(lst):
        index += 1
        print( 'index =', index )
        total += index
        print( 'total =', total )
        if total >= 4: 
            break
        index += 1

    print(total)

# matrix = [ [1,2,3], [3,13,-7], [2,-5] ]
# matrix[-1][1]


