# Problem 1

def displayFraction(n):
    ''' The function will have one parameter integer n
     and will display fractions with 4 decimal places.'''

    formatStr = '{}/{} = {:.4f};' 
    
    for i in range(2, n+1):
        print(formatStr.format(i ,n, i/n) , end=' ')

        
'''
>>> displayFraction(6)
2/6 = 0.3333; 3/6 = 0.5000; 4/6 = 0.6667; 5/6 = 0.8333; 6/6 = 1.0000;

'''
