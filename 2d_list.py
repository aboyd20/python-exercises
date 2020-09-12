t = [ [3,5,7], [0,2,1], [3,8,3] ]
m = [ [3,5,7,9], [0,2,1,6], [3,8,3,1] ]

# print each row of 2-D list
for lst in t:
    print( lst )

print()
print( 't[0][2]: {0}'.format( t[0][2] ) )
print( 't[-1][-2]: {0}'.format( t[-1][-2] ) )
print()
print( 't[0][2] old: {0}'.format( t[0][2] ) )
t[0][2] = t[0][2] + 3
print( 't[0][2] new: {0}'.format( t[0][2] ) )
print()

# print each col of 2-D list (transpose of matrix)
def transpose( m ): 
    print( m )
    transpose = [] # initialize matrix
    for j in range(len(m[0])): # number of rows = number of columns
        transpose.append([]) # create empty list to hold column values
        for k in range(len(m)): # number of columns = number of rows
            transpose[j].append(m[k][j]) # add t[col][row] to current row of transpose
        print('col {0} at index {1} is {2}'.format( j+1, j, transpose[j] ) )
    print()
    print('transpose matrix = {0}'.format( transpose ) )


# nested loop and 2-D list using iteration loop pattern
def print2D( twod_lst ):
    'print twod_lst so that it looks like a table'
    for row in twod_lst: # outer loop generates rows
        for col in row: # inner loop generates columns
            print( col, end= ' ' )

        print()


# Practice Problem 5.9
# nested loop and 2-D list using counter loop pattern
def add2D( t1, t2 ):
    '''increment every entry in first matrix with value
    of corresponding entry in the second matrix. display
    updated first matrix. matrices t1 and t2 same size.'''

    for i in range( len( t1) ): # outer loop generates row indexes
        for j in range( len( t1[i] ) ): # inner loop generates column indexes
            t1[i][j] += t2[i][j]

    for row in t1:
        print( row )

a = [ [4,2,5], [1,5, 2], [8, 6,3] ]
b = [ [0,1,2], [1,3,-1], [4,-2,0] ]
      
'''
>>> add2D( a, b )
[4, 3, 7]
[2, 8, 1]
[12, 4, 3]
'''


'''
pixels() takes as input a 2D list of non-negative integer
(representing the values of pixels of an image) and returns
the number of entries that are positive (not dark). function
should work on 2D list of any size.
'''
def pixels( t ):
    'return number of entries that are positive (not 0)'
    numPos = 0
    for row in t:
        for entry in row:
            if entry > 0:
                numPos += 1

    return numPos

lst1 = [ [0,156,0,0], [34,0,0,0], [23,123,0,34] ]
lst2 = [ [123,56,255], [34,0,0,0], [23,123,0], [3,0,0] ]

'''
>>> pixels( lst1 )
5
>>> pixels( lst2 )
7
'''
