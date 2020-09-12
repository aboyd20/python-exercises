# hw3.py due 1/25/2017
# Alicia Boyd

# Problem 1

def displayFractions(n):
    ''' The function will have one parameter integer n
     and will display fractions with 4 decimal places.'''

    formatStr = '{}/{} = {:.4f};' 
    
    for i in range(2, n+1):
        print(formatStr.format(i ,n, i/n) , end=' ')

        
'''
>>> displayFractions(6)
2/6 = 0.3333; 3/6 = 0.5000; 4/6 = 0.6667; 5/6 = 0.8333; 6/6 = 1.0000;

'''

# Problem 2

def avgScore(fname):

    ''' function will read the file contents and sorts and averages students' grades.
    This function will create a outputfile titled: outfile.txt . '''

    infile = open(fname, 'r') # open the file and read it
    listoflines= infile.readlines() # into a list of lines
    listoflines.sort() # list of lines in alphabetical order

    outputfile = open('outfile.txt', 'w') # creates file in current working directory


    for line in listoflines:
        new_line = line.strip()
        name, item = new_line.split('|') # not sure what you want for part 2b
        student_name = name.capitalize()
        score = (eval(item))  #not sure what you wanted for part 2c
        average_score = sum(score)/len(score)

        outputfile.write('{}:  avg score = {}\n'.format(student_name, average_score))

    outputfile.close()
           
'''
Albright:  avg score = 84.55555555555556
Barnard:  avg score = 86.44444444444444
Clemente:  avg score = 89.88888888888889
Cortez:  avg score = 83.33333333333333
Daly:  avg score = 86.33333333333333
Edmonds:  avg score = 87.88888888888889
Emehel:  avg score = 88.44444444444444
Hennings:  avg score = 88.0
Inman:  avg score = 87.0
Isaac:  avg score = 85.0
Landen:  avg score = 86.77777777777777
Leisner:  avg score = 83.44444444444444
Loftin:  avg score = 86.33333333333333
Muller:  avg score = 85.66666666666667
Quintero:  avg score = 88.33333333333333
Sanchez:  avg score = 86.33333333333333
Sickler:  avg score = 83.77777777777777
Simons:  avg score = 80.44444444444444
Taliaferro:  avg score = 85.55555555555556
Terry:  avg score = 86.33333333333333

'''

# Problem 3

def slicer(word):
    ''' this function accepts one parameter as a string and will
       perform the various slicing functions.'''
    
    print(word[:6], end = '\n') # displays the first five characters of word

    print(word[3:7], end ='\n')# displays the fourth through the seventh characters of word   

    print(word[-3:], end ='\n')# displays the last three characters of word using negative index

    print(word[1:],  end ='\n' ) # displays characters starting with second character and going all they way to end
        
    
'''
>>> slicer('supercalifragilisticexpialidocious')
superc
erca
ous
upercalifragilisticexpialidocious
'''
