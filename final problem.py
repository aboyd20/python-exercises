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


