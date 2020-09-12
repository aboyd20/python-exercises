
def juggle(num):
    ''' this function prints the numbers, each one on a line by itself
    including the starting value of num and the ending value of 1.  This
    is a function using recursion.'''

    print(num) # print all values of num; including the last value of 1

    if num ==1: #base case
        return

    elif num%2 != 0: #recursive case odd
        return juggle( int(num**1.5) )

    else: #second recursive case even
        return juggle( int(num**0.5) )
    

'''

== RESTART: E:/Winter Quarter 2017/CSC401/Week 8/Homework 7/extracredit.py ==
>>> juggle(8)
8
2
1
>>> juggle(17)
17
70
8
2
1

''''
