# hw8.py due 3/8/2017
# Alicia Boyd


# Problem 1
def alt(s1, s2):

    ''' this function has two parameters inputs and will
    return a string that is the result of alternating the letters of s1 and s2'''

    s = ''
    if s1 != '' and  s2 != '': # base case
        s = s1[0] + s2[0] # return empty string
        return s + alt(s1[1:],s2[1:])
    elif len(s1) > len(s2):
        s += s1
        return s
    elif len(s1) < len(s2):
        s += s2
        return s
    else:
        return ''

'''

>>> alt('cat','dog')
'cdaotg'
>>> alt('kitty','dog')
'kdiotgty'
>>> alt('cat','puppy')
'cpautppy'
>>> 

'''
# problem 2

'''
>>> 2 in lst - 5
>>> 80 in lst - 11 (not found in lst)
'''

'''
The command typed in interactive shell to put lst in format for binary
search is lst.sort()

lst displays in interactive shell: [2,5,8,35,50,64,66,77,87,92,97]

'''

'''
First time call binary search
rbinarySearch(lst, 50, 0, 11)
slice: lst[0:11] = [2,5,8,35,50,64,66,77,87,92,97]
mid = (0+11)//2 = 5
lst[5] = 64
50 <64; search lower

Second time call binary search
rbinarySearch(lst, 50, 0, 5)
slice: lst[0:5] = [2,5,8,35,50]
mid = (0+5)//2 = 2
lst[2] = 8
50 > 8; search upper

Third time call binary search
rbinarySearch(lst, 50, 3, 5)
slice: lst[3:5] = [35,50]
mid = (3+5)//2 = 4
lst[4] = 50
50 == 50; found target

'''

