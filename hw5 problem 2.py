# problem 2

def read_ticker(filename):

    ''' function will read in a file which will store the ticker and name in a dictionary
    and return the resulting dictionary so user can look up what company corresponds to a
    particular ticker symbol.'''

    # read file in

    d = {} # empty dictionary

    infile = open(filename, 'r')
    for line in infile:
        tickers = line.strip().split(',') #strips then splits the line into a list
        d[tickers[0]] = tickers[1]

    infile.close()

    return d


'''
>>> tickers['BJRI']
"BJ's Restaurants Inc."

'''

def ticker(filename):

    d = read_ticker(filename) 

    while True:
        # ask user to enter ticker symbol
        symbol = input('Please enter a ticker symbol:  ')

        #CEM review again the loop and half pattern in nominationsLoopHalf() function
        # in infinite_loop_half.py under week 5
        # you need to test for flag value that indicates user is done entering input
        # before doing anything else, how do you exit a while loop using
        # one of additional control structures

        # if user enters a ticker, then you check if that symbol is in dictionary
        # you have the symbol, so not necessary to iterate over all the dictionary keys
        for key in d.keys():
            if key == symbol:
                print('Company "{1}" has ticker symbol {0}.'. format(key, d[key]))
            if key != symbol:
                print('Ticker symbol "{}" not found.'.format(key))



        
            
        

    
