'''
Yaeesh Mukadam
EECS 210 Assignment 4
Description: Python code that will be able to find reflexive, symmetric, and transitive closures and determine if relations
logical equivalences and posets.
Date: Oct 11, 2023
Inputs: None
Output: Print relation properties and closures if needed.
Collaborators: None
'''
#problem 1
def is_reflexive(relation,given_set):
    #function to see if relation is reflexive or not
    for val in given_set:
        #iterate through the set
        if (val,val) not in relation:
            #if (val,val) is not in domain even once, then relation is not reflexive
            return False
    #if func reaches here, then relation is reflexive
    return True

def reflexive_closure(relation, given_set):
    #will find reflexive closure
    my_set = set()
    #initialize empty set
    for val in given_set:
        #iterate through the given set
        my_set.add((val,val))
        #add all reflexive ordered pairs to the set
    return sorted(my_set)
    #return sorted set which is the reflexive closure

def func_one(relation, given_set):
    #creates template for the problem
    print(f'a) R = {sorted(relation)}')
    #prints relation R
    if is_reflexive(relation,given_set):
        #checks to see if it is reflexive
        print("b) R is reflexive")
        #prints if so
    else:
        #if not reflexive, then it will print not reflexive and also print the reflexive closure
        print("b) R is not reflexive")
        print(f'c) R* = {reflexive_closure(relation,given_set)}')

def output_one():
    #prints output for problem 1 where it will show the code works for the 2 given examples
    print('For relation {(1,1),(4,4),(2,2),(3,3)} on the set {1,2,3,4}: ')
    #prints given relation and set
    func_one({(1,1),(4,4),(2,2),(3,3)}, {1,2,3,4})
    #runs the code defined above that will determine if relation is reflexive and print closure accordingly
    print("")
    print('For relation {(a,a),(c,c)} on the set {a,b,c,d}: ')
    #prints given relation and set
    func_one({('a','a'),('c','c')}, {'a','b','c','d'})
    #runs the code defined above that will determine if relation is reflexive and print closure accordingly
    print("")

def is_symmetric(relation):
    #function to determine if relation is symmetric
    for elem in relation:
        #iterate through relation
        if (elem[1],elem[0]) not in relation:
            #if the symmetric ordered pair is not in the relation, then the relation must not be symmetric
            return False
    #relation is symmetric
    return True

def symmetric_closure(relation):
    #func to find symmetric closure
    my_set = set()
    #initialize empty set to store closure
    for elem in relation:
        #iterate through the relation
        my_set.add(elem)
        #add the corresponding ordered pair to the closure
        my_set.add((elem[1],elem[0]))
        #add it's symmetrical pair to the closure also
    return sorted(my_set)
#return the closure
    

def func_two(relation, given_set):
     #func that creates template for the problem
    print(f'a) R = {sorted(relation)}')
    #prints relation
    if is_symmetric(relation):
        #checks to see if relation is symmetric
        print("b) R is symmetric")
        #if it is it prints so
    else:
        #else it prints its not symmetric and prints the closure
        print("b) R is not symmetric")
        print(f'c) R* = {symmetric_closure(relation)}')
def output_two():
    #prints output for problem 1 where it will show the code works for the 2 given examples    
    print('For relation {(1,2),(4,4),(2,1),(3,3)} on the set {1,2,3,4}: ')
    #prints given relation and set
    func_two({(1,2),(4,4),(2,1),(3,3)}, {1,2,3,4})
    #runs the code defined above that will determine if relation is symmetric and print closure accordingly
    print("")
    print('For relation {(1,2),(2,3)} on the set {1,2,3,4}: ')
    #prints given relation and set
    func_two({(1,2),(3,3)}, {1,2,3,4})
    #runs the code defined above that will determine if relation is symmetric and print closure accordingly
    print("")

def is_transitive(relation):
    #function to check if relation is transitive or not
    for elem_1 in relation:
        #iterate through R
        for elem_2 in relation:
            #nested for loop, iterate through R again. now we will have 2 values of the relation to compare
            if elem_1[1] == elem_2[0]:
                #testing to see if the tail of elem1 and head of elem2 are equal because if they are, then an ordered pair in the form of (head of elem1, tail of elem2) must exist for the
                #relation to be transitive
                if (elem_1[0], elem_2[1]) not in relation:
                    #if the above mentioned ordered pair is not in R, then R can not be transitive
                    return False
                    #return false, ending function
    #if func reaches this point, then r must have been transitive
    return True
    #return true

def transitive_closure(relation, given_set):
    matrix = [[0]*len(given_set)]
    #initialize a list with 0's across equal to length of given set
    for i in range(len(given_set)-1):
        #append to the list in a for loop to make a (length of given_set) x (length of given_set) sized 2d list/matrix completely filled with 0's
        matrix.append([0]*len(given_set))

    # fill the matrix with 1's corresponding to the relation
    for i in range(1,len(matrix)+1):
        #iterate through matrix row
        for j in range(1,len(matrix)+1):
            #iterate through matrix col
            if (i,j) in relation:
                #if (i,j) are in the relation then that given index will be a 1 in the matrix
                matrix[i-1][j-1] = 1
    #Warshall's algorithm from the powerpoint on canvas
    for k in range(len(given_set)):
        #iterate through matrix length of matrix times
            for i in range(len(given_set)):
                #iterate through matrix row
                for j in range(len(given_set)):
                    #iterate through matrix col
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
                    #warshalls algorithm- Wij OR (Wik AND Wkj)
    #matrix is now filled with the transitive closure
    #now we must extract data from the matrix and put the closure into a set form.
    closure = set()
    #initial empty set to store closure in
    set_list = list(given_set)
    #convert the given set into a list for indexing purposes
    for i in range(len(matrix)):
        #iterate through matrix rows
        for j in range(len(matrix)):
            #iterate through matrix cols
            if matrix[i][j] == 1:
                #if the matrix at that index has a 1
                closure.add((set_list[i],set_list[j]))
                #add the corresponding ordered pair to the closure set
    return sorted(closure)
#return transitive closure



def func_three(relation,given_set):
    #creates template for the problem
    print(f'a) R = {sorted(relation)}')
    #prints relation R
    if is_transitive(relation):
        #checks to see if it is transitive
        print("b) R is transitive")
        #prints if so
    else:
        #else it prints not transitive and prints closure
        print("b) R is not transitive")
        print(f'c) R* = {transitive_closure(relation,given_set)}')

def output_three():
    #prints output for problem 3 where it will show the code works for the 2 given examples
    print("For relation {('a','b'), ('d','d'), ('b','c'), ('a','c')} on the set {'a','b','c','d'}: ")
    #prints given relation and set
    func_three({("a","b"), ('d','d'), ('b','c'), ('a','c')}, {"a",'b','c','d'})
    #runs the code defined above that will determine if relation is transitive and print closure accordingly
    print("")
    print('For relation {(1,1),(1,3),(2,2),(3,1),(3,2)} on the set {1,2,3}: ')
    #prints given relation and set
    func_three({(1,1),(1,3),(2,2),(3,1),(3,2)}, {1,2,3})
    #runs the code defined above that will determine if relation is transitive and print closure accordingly
    print("")

def is_equivalence(relation, given_set):
    #func to see if relation is logical equivalence
    print(f'a) R = {relation}')
    #prints relation
    if is_reflexive(relation, given_set) and is_symmetric(relation) and is_transitive(relation):
        #checks to see if the relation is reflexive, and symmetric, and transitive
        print("b) R is an equivalence relation")
        # if it passes all the checks, then prints it is an equivalence relation
        return True
    else:
        #else prints its not equivalence
        print("b) R is not an equivalence relation because:")
        if not is_reflexive(relation, given_set):
            #checks if its not reflexive, if so prints as such
            print("Relation is not reflexive")
        if not is_symmetric(relation):
            #checks if its not symmetric, if so prints as such
            print("Relation is not symmetric")
        if not is_transitive(relation):
            #checks if its not transitive, if so prints as such
            print("Relation is not transitive")
    return False

def output_4():
    #prints output for problem 4 where it will show the code works for the 2 given examples
    print("For relation {(1,1),(2,2),(2,3)} on the set {1,2,3}: ")
    #prints relation and given set
    is_equivalence({(1,1),(2,2),(2,3)}, {1,2,3})
    #runs above defined function which will print whether or not it is a equivalence relation and if not why
    print("")
    print("For relation {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')} on the set {'a','b','c'}: ")
    #prints relation and given set
    is_equivalence({('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}, {'a','b','c'})
    #runs above defined function which will print whether or not it is a equivalence relation and if not why
    print("")


def is_antisymmetric(relation):
    #function to check if relation is antisymmetric
    for elem in relation:
        #iterates through relation
        if (elem[1],elem[0]) in relation:
            #if symmetric pair in relation, then the relation is not antisymmetric
            return False
    return True

def is_poset(relation, given_set):
    #func to check if relation is a partial order
    print(f'a) R = {relation}')
    #prints relation
    if is_reflexive(relation, given_set) and is_antisymmetric(relation) and is_transitive(relation):
        #checks to see if the relation is reflexive, and antisymmetric, and transitive
        print("b) R is a poset.")
        #if it passes all checks, then print R is poset
        return True
    else:
        #else print R is not a poset and why
        print("b) R is not a poset because:")
        if not is_reflexive(relation, given_set):
        #checks if its not reflexive, if so prints as such
            print("Relation is not reflexive")
        if not is_antisymmetric(relation):
        #checks if its not antisymmetric, if so prints as such
            print("Relation is not antisymmetric")
        if not is_transitive(relation):
        #checks if its not reflexive, if so prints as such
            print("Relation is not transitive")
    return False

def output_5():
    #prints output for problem 5 where it will show the code works for the 2 given examples
    print("For relation {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)} on the set {1,2,3,4}: ")
    #prints relation and given set
    is_poset({(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}, {1,2,3,4})
    #runs above defined function which will state if relation is a poset or not and if not why
    print("")
    print("For relation {(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} on the set {0,1,2,3}: ")
    #prints relation and given set
    is_poset({(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}, {0,1,2,3})
    #runs above defined function which will state if relation is a poset or not and if not why

print("1)")
output_one()
print("2)")
output_two()
print("3)")
output_three()
print("4)")
output_4()
print("5)")
output_5()






    






