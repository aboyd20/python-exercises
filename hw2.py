# hw2.py due 1/18/2017
# Alicia Boyd

# Problem 1

import math

def radians_to_degrees(radians):
    '''this function has one parameter, radians,
    which returns the value of an angle in degrees'''


    degrees = ( radians * 180 )/math.pi
    return degrees

'''

>>> radians_to_degrees(1.5708)
90.0002104591497

'''

# Problem 2

def isEligible():
    '  The function displays a message indicating whether or not the person is eligible to play on the team.'

    age = eval(input( 'Enter age: '))

    gender = input(' If you are a male enter m or if you are a female enter f:  ')
    
    if ((gender == 'm' and age == 10) or (gender == 'f' and 9>= age <= 11)):
        print ( 'Congratulations, you are eligible to play on the baseball team!')
    else:
        print( 'Sorry, you are ineligible to play on the baseball team.')

'''
==== RESTART: E:\Winter Quarter 2017\CSC401\Week 2\hw2 (problem2_ ex1).py ====
>>> isEligible()
Enter age: 9
 If you are a male enter m or if you are a female enter f:  f
Congratulations, you are eligible to play on the baseball team!
>>> isEligible()
Enter age: 9
 If you are a male enter m or if you are a female enter f:  m
Sorry, you are ineligible to play on the baseball team.
'''


# Problem 3

def convertCurrency(ccy, amt):
    '''function has two parameters; to calculate the value of a certain
    amount of money in one currency converted to a desired currency and returns the new amount'''

    if ccy == 'EUR':
        rate =.96
        amt = amt * rate
        return amt
    else:
        rate = 1.45
        amt =  amt * rate
        return amt


'''
>>> new_currency = input('Which currency do you want to convert your US dollars into EUR or SGD? ')
Which currency do you want to convert your US dollars into EUR or SGD? 107.80
>>> new_currency = input('Which currency do you want to convert your US dollars into EUR or SGD? ')
Which currency do you want to convert your US dollars into EUR or SGD? EUR
>>> dollars = eval(input('How much money in US dollars do you want to convert? '))
How much money in US dollars do you want to convert? 107.80
>>> new_amount = convertCurrency(new_currency,dollars)
>>> new_amount
103.488
>>> print( 'new amount = ' , new_amount, new_currency)
new amount =  103.488 EUR

>>> new_currency = input('Which currency do you want to convert your US dollars into EUR or SGD? ')
Which currency do you want to convert your US dollars into EUR or SGD? SGD
>>> dollars = eval(input('How much money in US dollars do you want to convert? '))
How much money in US dollars do you want to convert? 86
>>> new_amount = convertCurrency(new_currency,dollars)
>>> new_amount
124.7
>>> print( 'new amount = ' , new_amount, new_currency)
new amount =  124.7 SGD

'''


# Problem 4

def oddNumbers():
    ''' The function iterates over a sequence of numbers generated
    from range() function, starting at 3 and concludes at 23. Then it prints only the odd
    numbers in the list, each on a seperate line. The function does not have have return value.'''

    for i in range(3,24):
        if i % 2 != 0:
            print(i)


'''
========= RESTART: E:/Winter Quarter 2017/CSC401/Week 2/problem 4.py =========
>>> oddNumbers()
3
5
7
9
11
13
15
17
19
21
23


'''
        
