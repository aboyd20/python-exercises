
def p1( lst ):
    'return sorted list of lst with all duplicate words removed'

    # accumulator variable
    new_lst = []

    # iterate over lst and only add unique word to new list
    for item in lst:
        if item not in new_lst:
            new_lst.append( item )
            
    # sort new_list, then return
    new_lst.sort()
    
    return new_lst


def p2( dct_grades ):
    'return list of all students who received a grade above 90'

    # accumulator variable
    over_ninety = []

    # iterate over dictionary key, value pairs to get students w/ grade > 90
    for name, grade in dct_grades.items():
        if grade > 90:
            over_ninety.append( name )
    
    # return final list
    return over_ninety

grades = {
    'dave matthews': 75,
    'natalie merchant': 95,
    'lauren hill': 80,
    'donnie hathaway': 100,
    'eddie vedder': 91,
    'ed kowalczyk': 83,
    'jimi hendrix': 89,
    'donald fagen': 88,
    'minnie ripperton': 95}
    
