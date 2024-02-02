'''
Yaeesh Mukadam
EECS 210 Assignment 3
Description: Python code that will perform various set and relation operations. Also will prove relation properties for given questions.
Date: Sep 26, 2023
Inputs: None
Output: Resulting set and relations from various operations and booleans for given relation properties.
Collaborators: ChatGPT for the function to take composite of 2 relations. Rest is authored by me
'''
q1_r1 = {(1,1), (2,2), (3,3)}
#relation1 for question 1 in python set
q1_r2 = {(1,1), (1,2), (1,3), (1,4)}
#relation 2 for question 1 in python set

def one_a():
    #problem 1a
    print(q1_r1.union(q1_r2))
    #prints the union between relation 1 and 2

def one_b():
    #problem 1b
    print(q1_r1.intersection(q1_r2))
    #prints the intersection between relation 1 and 2

def one_c():
    #problem 1c
    print(q1_r1 - q1_r2)
     #prints the difference between relation 1 and 2

def one_d():
    #problem 1d
    print(q1_r2 - q1_r1)
     #prints the difference between relation 2 and 1


def find_composite(r1,r2):
    #function to find composite of 2 relations
    #collaborated with chatGPT for the nested for loop part of this function.
    res = set()
    #create empty set to store the result in
    for i in r1:
        #iterate through first relation
        for j in r2:
            #nested for loop. iterate through 2nd relation
            if i[1] == j[0]:
                #if the tail and head of the two ordered pairs are equal, then we can combine the head of the first ordered pair
                # and tail of the 2nd ordered pair to create an ordered pair that is a member of the composition of the relation
                res.add((i[0],j[1]))
                #add the ordered pair to the result set
    return sorted(res)
    #return the result set as sorted for clarity
def problem_2():
    #problem 2
    r = {(1,1),(1,4),(2,3),(3,1),(3,4)}
    #relation r as defined in the question
    s = {(1,0),(2,0),(3,1),(3,2),(4,1)}
    #relation s as defined in the question
    print(find_composite(s,r))
    #input relation s and r into the function defined above that will find the composite of 2 relations and print


def problem_3():
    #problem 3
    r = {(1,1),(1,4),(2,3),(3,1),(3,4)}
    #relation r as defined in the question
    print(find_composite(r,r))
    #input relation r and r into the function defined above that will find the composite of 2 relations

def problem_4_R():
    #create relation R for problem 4 as a set
    domain = []
    #create empty domain list
    for i in range(-10,11):
        #iterate thorugh -10 to 11
        domain.append(i)
        #populate the domain list from values from -10 to 10 inclusive
    res = set()
    #create set for result
    for x in domain:
        #iterate through domain
        for y in domain:
            #nested for loop, iterating through domain
            if x+y == 0:
                #if x+y = 0, then it satisfies condition to be added to set
                res.add((x,y))
                #add x and y to the set as an ordered pair
    return sorted(res)
    #returns result set as sorted for clarity


def four_a():
    #problem 4a
    print(problem_4_R())
    #print result set from function call problem_4_R defined above

def four_b():
    domain = []
    #create empty domain list
    for i in range(-10,11):
        #iterate thorugh -10 to 11
        domain.append(i)
        #populate the domain list from values from -10 to 10 inclusive
    R = problem_4_R()
    #call function problem_4_R and store the set as R
    for num in domain:
        #iterate through the domain
        if (num,num) not in R:
            #if (num,num) is not in relation R, then R is not reflexive
            print(f"({num},{num}) not in R, therefore R is not reflexive.")
            #print which iteration proved R is not refleive
            return False
            #return False and end function
    #if function got to this point, then no values were found that made R not reflexive, therefore R is reflexive
    print("R is reflexive")
    #print R is reflexive
    return True
    #return True



def four_c():
    #problem 4c
    R = problem_4_R()
    #call function problem_4_R and store the set as R
    for elem in R:
        #iterate through R
        if (elem[1],elem[0]) not in R:
            #flip elem around which will give the symmetric pair of elem, if it is not in R, then R is not symmetric.
            print(f'({elem[1]}, {elem[0]}) is not in R, but ({elem[0]}, {elem[1]}) is. Therefore R is not symmetric.')
            #print R is not symmetric and print which values made it not symmetric
            return False
            #return False ending func
    #if func reaches this point, then r must have been symmetric
    print("R is symmetric")
    #print R is symmetric
    return True
    #return true

def four_d():
    #problem 4d
    R = problem_4_R()
    #call function problem_4_R and store the set as R
    for elem in R:
        #iterate through R
        if (elem[1],elem[0]) in R:
            #flip elem around which will give the symmetric pair of elem, if it is in R, then R is not antisymmetric.
            print(f'({elem[1]}, {elem[0]}) and ({elem[0]}, {elem[1]}) are both in R. Therefore R is not antisymmetric.')
            #print R is not antisymmetric and print which values made it not antisymmetric
            return False
            #return false ending func
    #if func reaches this point, then r must have been antisymmetric
    print("R is antisymmetric.")
    #print R is antisymmetric
    return True
#return true


def four_e():
    #problem 4d
    R = problem_4_R()
    #call function problem_4_R and store the set as R
    for elem_1 in R:
        #iterate through R
        for elem_2 in R:
            #nested for loop, iterate through R again. now we will have 2 values of the relation to compare
            if elem_1[1] == elem_2[0]:
                #testing to see if the tail of elem1 and head of elem2 are equal because if they are, then an ordered pair in the form of (head of elem1, tail of elem2) must exist for the
                #relation to be transitive
                if (elem_1[0], elem_2[1]) not in R:
                    #if the above mentioned ordered pair is not in R, then R can not be transitive
                    print(f'{elem_1} and {elem_2} exist, but {elem_1[0], elem_2[1]} does not exist. Therefore R is not transitive.')
                    #print r is not transitive and which ordered pairs prove it to not be.
                    return False
                    #return false, ending function
    #if func reaches this point, then r must have been transitive
    print("R is transitive")
    #print r is transitive
    return True
    #return true
#rest of code is formatting and calling all the functions
print("1a")
one_a()
print("")
print("1b")
one_b()
print("")
print("1c")
one_c()
print("")
print("1d")
one_d()
print("")
print("2")
problem_2()
print("")
print("3")
problem_3()
print("")
print("4a")
four_a()
print("")
print("4b")
four_b()
print("")
print("4c")
four_c()
print("")
print("4d")
four_d()
print("")
print("4e")
four_e()
print("")





        

        



