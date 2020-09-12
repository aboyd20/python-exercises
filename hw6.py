# hw6.py due 2/22/2017
# Alicia Boyd

#problem 1

def openFile():
    'open hambone.txt and read content'
    infile = open( 'hambone.txt', 'r' )
    content = infile.read()
    infile.close()

def tryOpenFile():
 ''' this function is an try and except as an alterative for not finding a particular file.'''
    try:
        openFile()
    except:
        print("hambone.txt file could not be found")

'''

=== RESTART: E:/Winter Quarter 2017/CSC401/Week 7/Homework 6/problem 1.py ===
>>> tryOpenFile()
hambone.txt file could not be found
>>> 

'''


# Problem 2

def x( a ):
    print( 'x() local vars:', vars() ) #a is local to x(a) 
    print()
    return a+c

def y( b ):
    c = 5 # c is local to y(b)
    print( 'y() local vars:', vars() ) # b is local to y(b)
    print()
    return b*c


c = 4 # c is global
res = x(2) + y(3)  #res is global
print( 'res = {0}'.format( res ) )
