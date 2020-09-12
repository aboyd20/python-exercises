# sets contains an unordered collection of unique and immutable objects

# set_a = { [1,2,3], 'a', 'b', 'c', 'a' } # list is mutable so gives error
'''
Traceback (most recent call last):
  File "C:\CSC 401 WQ2016\examples\week5\set.py", line 3, in <module>
    set_a = { [1,2,3], 'a', 'b', 'c', 'a' } # list is mutable so gives error
TypeError: unhashable type: 'list'
'''

set_b = { (1,2,3), 'a', 'b', 'c', 'a', (1,2,3), (4,5,6) }
print( 'set_b: ', set_b )
print()
# set_b:  {'a', 'b', (4, 5, 6), 'c', (1, 2, 3)}


set_c = { 'a', 'b', 'c', 'a' }
print( 'set_c: ', set_c )
print()
# set_c:  {'a', 'b', 'c'}


# create an empty set
set_d = set()
print( 'type set_d: ', type( set_d ) )
# type set_d:  <class 'set'>
print( 'len set_d: ', len(set_d) )
# len set_d:  0
print()


# even though set objects must be immutable, set is mutable
set_d.add( 4 )
set_d.add( 4 )
set_d.add( 'hello' )
print( 'set_d after changes: ', set_d )
# set_d after changes:  {'hello', 4}
print( 'set_d length after changes: ', len(set_d) )
# set_d length after changes:  2
print()


# set constructor to remove duplicates from a list
nums = [ 10, 20, 30, 10, 10, 20, 20, 34, 46 ]
nums = list( set ( nums ) )
print( 'nums list: ', nums )
# nums list:  [10, 34, 20, 30, 46]
