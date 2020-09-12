#problem 1

def movie_tix(age, num_ppl):

    "this program will compute and return the cost of the tickets"

    if age < 2:
        tix_cost = print("Your tickets are free!")

    elif 2<= age <= 12:
        tix_cost = num_ppl * 11.00
        
    elif age <= 60:
        tix_cost = num_ppl * 10.00

    else: # between ages of 13 and greater45 
        tix_cost = num_ppl * 14.00

    return tix_cost

'''

>>> movie_tix(1, 2)
Your tickets are free!


>>> movie_tix(12, 3)
33.0

>>> movie_tix(12, 3)
33.0

>>> movie_tix(60, 5)
50.0

'''


#Problem 2

def trace(matrix):
    ''' this function has one input parameter, matrix.  The matrix is assumed it is n x n.
        The function will calculate the trace of a square matrix by calculating the sum
        of its diagonal elements and finally return the sum. '''

    vector =[] 

    mySum = 0 # initializing the accumulator
    
    for i in range(len(m)):  
        for j in range(len(m[i])):
            # print(m[i][j])
            if i == j:
                vector.append(m[i][j])
                # print(vector) this prints vector for checking the diagonal 

    for num in vector:
        mySum += num #adding the accumulator

    return mySum # returns the sum of the accumulator

'''
>>> m =[[-7,-5,5], [18,-3,26], [-8,0,17]]
>>> trace(m)
7

'''


#Problem 3

def getEvenTuples(lst1,lst2):

    ''' This function accepts two lists as parameters, which contain nonnegative integers.
        The function will return a list of tuples where each tuple contains a value
        from lst1 and a value from lst2 where the sum of those values is an even number.
        This program will print a final statement when done iterating over both loops.
        '''
    
    new = []  #accumulator for the list

    for i in lst1:
        for j in lst2:
            if (i + j) % 2 == 0: # check to see if the two values sum to an even number
                new.append((i,j)) # creating a tuple then appending it to a list
    print("Done checking!")

    return new
'''
>>> a = [5,40,6]
>>> b = [4,7,25,1,18]
>>> getEvenTuples(a,b)
Done checking!
[(5, 7), (5, 25), (5, 1), (40, 4), (40, 18), (6, 4), (6, 18)]

'''

# Problem 4

def countdownWhile(n, max_repeat):

   '''display countdown form n to 1 on seperate lines;
    after display 1, print "blast off" on seperate lines; stop printing after having countdown
    max_repeat times.'''
   
    i = 0
    
    while  i < max_repeat:

        counter = n

        while counter > 0:
            print(counter)
            if counter == 1:

                print("blast off")
            counter -= 1
        i += 1
''''
>>> countdownWhile(5,2)
5
4
3
2
1
blast off
5
4
3
2
1
blast off
>>> 
'''

#problem 5


def avgScore(fname):

    ''' function will read the file contents and sorts and averages students' grades.
    This function will create a outputfile. '''

    infile = open(fname, 'r') # open the file and read it
    listoflines= infile.readlines() # into a list of lines
    listoflines.sort() # list of lines in alphabetical order

    outputfile = open('outfile.txt', 'w') # creates file in current working directory

    new =[]

    for line in listoflines:
        new = eval(line) # its evaluating line which is a string class into a list class
        student_name =new[0].capitalize() #now a list there are two elements within the list new[0] and new[1]
        average_score = sum(new[1])/ len(new[1]) # new[1] are the scores which already have been evaluated from earlier

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


    


