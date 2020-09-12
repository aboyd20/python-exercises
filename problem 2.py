
def avgScore(fname):

    ''' function will read the file contents and sorts and averages students' grades.
    This function will create a outputfile. '''

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


    

