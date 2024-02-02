'''
Yaeesh Mukadam
EECS 210 Assignment 1
Description: Python code that prints out truth tables to prove the logical equivalence of 6 propositions
Date: Aug 28, 2022
Inputs: None
Output: a truth table for each proposition given (6 total) to show their logical equivalences
Collaborators: None
'''

#De Morgan's First Law

def left_side_DM_1(p,q):
#returns boolean for left side of De morgans first law with given input
    return not (p and q)
def right_side_DM_1(p,q):
#returns boolean for right side of de morgans first law with given input
    return ((not p) or (not q))
def demorgan_1_truth_table():
    inputs = [True, False]
    #list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    #combinations for truth table
    print("P", "\t", "Q", "\t", "!(P * Q)", "\t", "!(P) + !(Q)")
    #printing truth table formatting
    print("----------------------------------------------")
    #truth table formatting

    '''nested for loop because i have 2 inputs. It will go through all possible inputs of True and False for
     both P and Q. I will pass in i and j (which is either True or False) to the left and right side functions defined above in order to generate truth value for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''
    for i in inputs:
        for j in inputs: 
            left_side = left_side_DM_1(i,j)
            right_side = right_side_DM_1(i,j)
            print(f"{i} \t {j} \t {left_side} \t\t {right_side}")

            
#De Morgan's Second Law
def left_side_DM_2(p,q):
    #returns boolean for left side of De morgans second law with given input
    return not (p or q)
def right_side_DM_2(p,q):
    #returns boolean for right side of De morgans second law with given input
    return ((not p) and (not q))
def demorgan_2_truth_table():
    inputs = [True, False]
    '''list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    combinations for truth table
    '''
    print("P", "\t", "Q", "\t", "!(P + Q)", "\t", "(!P) * (!Q)")
    #truth table formatting
    print("----------------------------------------------")
    #truth table formatting

    '''nested for loop because i have 2 inputs. It will go through all possible inputs of True and False for
     both P and Q. I will pass in i and j (which is either True or False) to the left and right side functions defined above in order to generate truth value for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''
    for i in inputs:
        for j in inputs: 
            left_side = left_side_DM_2(i,j)
            right_side = right_side_DM_2(i,j)
            print(f"{i} \t {j} \t {left_side} \t\t {right_side}")


#First Associative Law
def left_side_AL_1(p,q,r):
    #returns boolean for left side of first associative law with given input
    return (p and q) and (r)
def right_side_AL_1(p,q,r):
    #returns boolean for right side of first associative law with given input
    return (p) and (q and r)
def associative_1_truth_table():
    inputs = [True, False]
    '''list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    combinations for truth table
    '''
    print("P", "\t", "Q", "\t", "R" "\t" "(P * Q) * (R)", "\t", "(P) * (Q * R)")
    #truth table formatting
    print("------------------------------------------------------")
    #truth table formatting

    '''triple nested for loop because there are 3 inputs. It will go through all possible inputs of True and False for
     both P, Q, and R. I will pass in i,j, and k (which is either True or False) to the left and right side functions defined above in order to generate truth values for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''
    for i in inputs:
        for j in inputs: 
            for k in inputs:
                left_side = left_side_AL_1(i,j,k)
                right_side = right_side_AL_1(i,j,k)
                print(f"{i} \t {j} \t {k} \t {left_side} \t\t {right_side}")


#Second Associative Law
def left_side_AL_2(p,q,r):
    #returns boolean for left side of second associative law with given input
    return (p or q) or (r)
def right_side_AL_2(p,q,r):
    #returns boolean for right side of second associative law with given input
    return (p) or (q or r)
def associative_2_truth_table():
    inputs = [True, False]
    '''list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    combinations for truth table
    '''
    print("P", "\t", "Q", "\t", "R" "\t" "(P + Q) + (R)", "\t", "(P) + (Q + R)")
    #truth table formatting
    print("------------------------------------------------------")
    #formatting

    '''triple nested for loop because there are 3 inputs. It will go through all possible inputs of True and False for
     both P, Q, and R. I will pass in i,j, and k (which is either True or False) to the left and right side functions defined above in order to generate truth values for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''
    for i in inputs:
        for j in inputs: 
            for k in inputs:
                left_side = left_side_AL_2(i,j,k)
                right_side = right_side_AL_2(i,j,k)
                print(f"{i} \t {j} \t {k} \t {left_side} \t\t {right_side}")

# Question #5: [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
def left_side_5(p,q,r):
    #returns boolean for left side of the 5th proposition with given inputs
    return not((p or q) and ((not p) or r) and ((not q) or r)) or r
def right_side_5():
    #always returns true because right side of the 5th proposition is equal to True
    return True
def truth_table_5():
    inputs = [True, False]
    '''list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    combinations for truth table
    '''
    print("P", "\t", "Q", "\t", "R" "\t" "[(P + Q) * (P -> R) * (Q -> R)] -> R", "\t\t", "T")
    print("-----------------------------------------------------------------------------")
    #truth table formatting above 2 lines

    '''triple nested for loop because there are 3 inputs. It will go through all possible inputs of True and False for
     both P, Q, and R. I will pass in i,j, and k (which is either True or False) to the left and right side functions defined above in order to generate truth values for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''

    for i in inputs:
        for j in inputs:
            for k in inputs:
                left_side = left_side_5(i,j,k)
                right_side = right_side_5()
                print(f"{i} \t {j} \t {k} \t {left_side} \t\t\t\t\t\t {right_side}")

# Question #6: p ↔ q ≡ (p → q) ∧ (q → p)
def left_side_6(p,q):
    #returns boolean for left side of proposition 6 with given inputs
    return (p and q) or ((not p) and (not q))
def right_side_6(p,q):
    #returns boolean for right side of proposition 6 with given inputs
    return ((not p) or q) and ((not q) or p)
def truth_table_6():
    inputs= [True, False]
    '''list of the possible inputs, either true or false, so i can then iterate through the list to generate all possible
    combinations for truth table
    '''
    print("P", "\t", "Q", "\t" "P <-> Q", "\t\t", "(P -> Q) * (Q -> P)")
    print("-----------------------------------------------------------------------------")
    #truth table formatting for above 2 lines

    '''nested for loop because i have 2 inputs. It will go through all possible inputs of True and False for
     both P and Q. I will pass in i and j (which is either True or False) to the left and right side functions defined above in order to generate truth value for
     left and right side. Then it will print it with proper formatting for the truth table in order to compare left and right sides
    '''
    for i in inputs:
        for j in inputs:
            left_side = left_side_6(i,j)
            right_side = right_side_6(i,j)
            print(f"{i} \t {j} \t {left_side} \t\t\t\t {right_side}")


# The rest of the code is to print all the truth tables for the 6 propositions with a space in between each for proper formatting.
print("1st proposition: ")
demorgan_1_truth_table()
print("")
print("2nd Proposition: ")
demorgan_2_truth_table()
print("")
print("3rd proposition: ")
associative_1_truth_table()
print("")
print("4th Proposition: ")
associative_2_truth_table()
print("")
print("5th proposition: ")
truth_table_5()
print("")
print("6th Proposition: ")
truth_table_6()