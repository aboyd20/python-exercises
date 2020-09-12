
def slicer(word):
    ''' this function accepts one parameter as a string and will
       perform the various slicing functions.:
'''
    
    print(word[:6], end = '\n') # displays the first five characters of word

    print(word[3:7], end ='\n')# displays the fourth through the seventh characters of word   

    print(word[-3:], end ='\n')# displays the last three characters of word using negative index

    print(word[1:],  end ='\n' ) # displays characters starting with second character and going all they way to end
        
    
'''
= RESTART: G:/Winter Quarter 2017/CSC401/Week 3/Homwork week 3/problem 3.py =
>>> slicer('supercalifragilisticexpialidocious')
superc
erca
ous
upercalifragilisticexpialidocious
'''
