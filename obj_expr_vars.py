# objExprVars.py

##### IDLE #####

two modes:
    interactive shell
    file editor


##### expressions #####

use IDLE like a calculator

operations:  (in order of operation)

    () 
    **  power
    *,/
    //,%  div and mod
    +,-

functions:

    round()
    abs()
    max()
    min()
    
>>> 
>>> 55+33
88

>>> 2*4
8

>>> 2.3**3
12.166999999999998

>>> 2.3**3.1
13.22380059125472

>>> 55+33
88

>>> 2+3*4
14

>>> (2+3)*4
20

>>> 4/3
1.3333333333333333

>>> 4//3
1

>>> 15//4
3

>>> 15%4
3

>>> 132//60
2

>>> 132%60
12

>>> # use %2 to test odd even
>>> 133%2
1

>>> 130%2
0

>>> # get final digit of a decimal number
>>> 4327%10
7

>>> 4327//10
432

>>> abs(-33.2)
33.2

>>> max(-5,-3,-2)
-2

>>> # convert fahrenheit to celcius
>>> 10-32*5/9
-7.777777777777779

>>> (10-32)*5/9
-12.222222222222221

>>> (32-32)*5/9
0.0

>>> (212-32)*5/9
100.0
>>> 

##### variables #####

variables are names used
to remember objects (e.g. numbers)
so that they can be used again later

variable = expression

    1) expression is evaluated, result produced
    2) variable now refers to that result
       in all subsequent calculations

variables do not exist until they are
assigned to

variables can be reused to hold
different objects (even of different types)

variables names:
    use a..z A..Z 0..9 _
    cant start with digit
    cAse SensITive
    use short and meaningful names
    use camelcase - joeTheRobot
    dont use reserved words or core language

vars()
    shows current namespace, i.e. variables
    and the objects they refer to
    
    not in the book


>>> f = 10
>>> f
10

>>> c
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c
NameError: name 'c' is not defined

>>> f
10

>>> (f-32)*5/9
-12.222222222222221

>>> c=(f-32)*5/9
>>> c
-12.222222222222221

>>> f=32
>>> c=(f-32)*5/9
>>> c
0.0
>>> f
32

>>> f='apple'
>>> f
'apple'

>>> f+f
'appleapple'

>>> x
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x
NameError: name 'x' is not defined


##### bool(ean) expressions #####

boolean expressions
    mathematical expressions
    where the answer is either True or False

operations
    ==,!=   equals, not equals
    <,>,<=,>=

compound booleans
    and, or, not

    expr1 and expr2  - true only if both are true
    expr1 or expr2 - true if either is true
    
>>> x=2
>>> y=3
>>> x<=2 and y<3
False

>>> x<=2 or y<3
True
>>> not(x<7) and y>1
False
>>> x
2
>>> # very common mistake
>>> # you probably dont mean to say this
>>> x==3 or 5
5
>>> # what you probably meant was
>>> x==3 or x==5
False

>>> # this works in python, not in other languages
>>> 1<x<5
True

>>> 4-5.2==-1.2
False 

##### type #####

variables dont have a type, objects do

type( expr ) - will tell you the type
of the result of the expression

>>> type(3)
<class 'int'>

>>> type('apple')
<class 'str'>

>>> type(2*3.0)
<class 'float'>

>>> type( 4<5 )
<class 'bool'>

>>> type(3.0)
<class 'float'>

>>> 3==3.0
True

>>> type( 12/3 )
<class 'float'>

>>> type( 12//3 )
<class 'int'>


##### str(ing) #####

string
    for textual data
    sequence of characters
    delimit with one of '', "" or ''' string '''
    \n is newline character

functions
    len

operators
    in, not in  - test for substrings
    +  concatentation
    str * int, int * str
    <,>,<=,>=  work alphabetically, careful
       all uppercase or less than lowercase
    []

indexing
    a string is a 0-based sequence of characters
    s[i] returns ith character
    s[start:stop] - substring using given range
        includes start, does not include stop
    
    
>>> s = 'apple'
>>> t = "pear"
>>> w = '''triple quotes allow
strings
that run onto
multiple lines
'''
>>> s
'apple'
>>> t
'pear'
>>> w
'triple quotes allow\nstrings\nthat run onto\nmultiple lines\n'
>>> print(w) # makes it pretty
triple quotes allow
strings
that run onto
multiple lines

>>> ww = "\n\nabc\n"
>>> len(ww)
6
>>> ss = "Eric's"
>>> y = 'abc\'\"'
>>> y
'abc\'"'
>>> print(y)
abc'"

>>> s
'apple'
>>> 'ap' in s
True
>>> 'ap' in t
False
>>> t
'pear'
>>> 
>>> s+t
'applepear'
>>> s+' '+t
'apple pear'

>>> s*t
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s*t
TypeError: can't multiply sequence by non-int of type 'str'
>>> 3*s
'appleappleapple'
>>> s*5
'appleappleappleappleapple'
>>> s < t
True
>>> 'Pear' < 'apple'
True

>>> s
'apple'
>>> s[1]
'p'
>>> s[4]
'e'
>>> s[0]
'a'
>>> len(s)
5
>>> s
'apple'
>>> s[1:3]
'pp'
>>> s[1:4]
'ppl'

>>> # empty string
>>> s = ' '  # not empty
>>> len(s)
1
>>> s=''
>>> len(s)
0

>>> t
'pear'
>>> t[3]
'r'
>>> t[len(t)-1]
'r'
>>> t[-1]   # last character
'r'
>>> t
'pear'
>>> t[7]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    t[7]
IndexError: string index out of range
>>> 

##### list #####

list
    sequence of items of any type
    types can be mixed
    indexed, 0-based
    []  empty list

operators
    [i]
    [start:stop] - slice
    in, not in  - check for items (not sub lists)
    + concatentation
    int * list, list*int

functions
    len
    max, min

methods
    append(item)
    pop() - removes and returns item
    count(item)
    index(item)
    remove(item)
    reverse()
    sort()
    

>>> # lists
>>> lst = [2,3,4,5,3<4,'apple',max]
>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>]
>>> lst[2]
4
>>> type( lst[4] )
<class 'bool'>

>>> lst[0]/lst[1]
0.6666666666666666

>>> lst[5][3]
'l'

>>> # in is very useful
>>> 3 in lst
True

>>> 'ap' in lst
False

>>> [3,4] in lst
False

>>> x = 7
>>> x==2 or x==3 or x==5 or x==8
False
>>> x in [2,3,5,8]
False

>>> lst + [0,1]
[2, 3, 4, 5, True, 'apple', <built-in function max>, 0, 1]

>>> len(lst)
7

>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>]

>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>]

>>> # function
>>> len(lst)
7
>>> #method
>>> lst.
SyntaxError: invalid syntax
>>> lst.append( 777 )
>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>, 777]
>>> lst.append( 'banana' )
>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>, 777, 'banana']
>>> lst.append( 3 )
>>> lst
[2, 3, 4, 5, True, 'apple', <built-in function max>, 777, 'banana', 3]
>>> lst.count( 3 )
2
>>> lst.index(3)
1

>>> lst.index(22)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lst.index(22)
ValueError: 22 is not in list

>>> lst.remove(3)
>>> lst
[2, 4, 5, True, 'apple', <built-in function max>, 777, 'banana', 3]
>>> lst.pop()
3
>>> lst
[2, 4, 5, True, 'apple', <built-in function max>, 777, 'banana']
>>> last = lst.pop()
>>> lst
[2, 4, 5, True, 'apple', <built-in function max>, 777]
>>> last
'banana'
>>> lst
[2, 4, 5, True, 'apple', <built-in function max>, 777]
>>> lst.reverse()
>>> lst
[777, <built-in function max>, 'apple', True, 5, 4, 2]
>>> lst.sort()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    lst.sort()
TypeError: unorderable types: builtin_function_or_method() < int()

>>> lst
[777, <built-in function max>, 'apple', True, 5, 4, 2]

>>> # update item in list
>>> lst[1]=999.99

>>> lst
[777, 999.99, 'apple', True, 5, 4, 2]
>>> max(lst)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    max(lst)
TypeError: unorderable types: str() > int()


>>> lst[2] = 0
>>> lst
[777, 999.99, 0, True, 5, 4, 2]
>>> lst.sort()
>>> lst
[0, True, 2, 4, 5, 777, 999.99]
>>> lst.index(5)
4
>>> lst.index(True)
1

>>> 
>>> 
>>> s = 'apple'
>>> s[1] = 'g'
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    s[1] = 'g'
TypeError: 'str' object does not support item assignment
>>> # capitalize a in apple
>>> s[0] = 'A'    # doesnt work
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    s[0] = 'A'    # doesnt work
TypeError: 'str' object does not support item assignment

>>> 5 < 'apple'
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    5 < 'apple'
TypeError: unorderable types: int() < str()

>>> max( [2, 3, 6.1] )
6.1

>>> max( [2, 3, 6.1, True] )
6.1

>>> max( ['apple','pear','kiwi'])
'pear'
>>> max( ['apple','pear','kiwi','pineapple'])
'pineapple'
>>> 'pineapple' > 'pine'
True


    
    



























    

