'''
Yaeesh Mukadam
EECS 210 Assignment 7
Description: Python program solves different types of combination questions regarding objects and boxes
Date: Nov 28, 2023
Inputs: None
Output: solving various combinatorial questions
Collaborators: ChatGPT/Google
'''
import math
#import math to use combination function

def distO_distB(a,b):
    #uses the formula given in the slides for distinguishable object and distinguishable box and returns answer
    return math.comb(a,b)

def indistO_distB(a,b):
    #uses the formula given in the slides for indistinguishable object and distinguishable box and returns answer
    return math.comb(a+b-1,a)

def distO_indistB(a,b):
    #function to find combinations for distinguishable object and indistinguishable box
    
    def stirling(a,b):
        #function find stirling number of second kind
        #got this code from help of google
        a1 = a
        #set a1 as a to store for future purposes
        b1 = b
        #set b1 as b to store for future purposes

        if a <= 0:
            #base case situation
            return 1
        elif b <= 0:
            #base case
            return 0
        elif (a == 0 and b == 0):
            #base case
            return -1
        elif a !=0 and a ==b:
            #base case
            return 1
        elif a<b:
            #base case
            return 0
        else:
            #recursion part here
            temp1 = stirling(a1-1, b1)
            #set temp 1 to value of stirling(a1-1,b1)
            temp1 *= b1
            #multiply temp by value of b1
            return (b1*(stirling(a1-1, b1))) + stirling(a1-1, b1-1)
            #will recursively call stirling and will return stirling value for given a and b value
    total = 0
    #initialize total variable
    for i in range(1,b+1):
        #because stirling function gives all combinations at given b value, but we want to add up all the stirling values for b = b all the way down to 1, we use a loop
        total += stirling(a,i)
        #get stirling value for each i value of loop and add to total
    return total
    #return total which will be all the combinations

def indistO_indistB(a,b):
    #function for finding total # of combinations of indistinguishable objects and boxes
    #formula given on slide wasn't working, so got some help from chatgpt and modified given formula
    if a == 0:
        #base case
        return 1
    elif a <= 0 or b <= 0:
        #base case
        return 0
    else:
        #uses recursive formula- p(k-n,n) + p(k,n-1)
        return indistO_indistB(a-b,b) + indistO_indistB(a,b-1)
        #returns the total number of combinations
    
def q1():
    print("Question 1a: How many ways are there to deal 5-card poker hands from a 52-card deck to each of four players?")
    #print question
    ans_1a = distO_distB(52,5) * distO_distB(47,5) * distO_distB(42,5) * distO_distB(37,5)
    #first player will pick 5 cards from pile of 52, second player has pile of 47, 3rd has 42, and 4th player has a pile of 37.
    #store ans in variable
    print(f'The answer is {ans_1a} ways.')
    #print answer
    print("")
    #formatting
    print("""Question 1b: 'A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box. 
How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?' """)
    ans_1b = distO_distB(40,10) * distO_distB(30,10) * distO_distB(20,10) * distO_distB(10,10)
    #after the first box is distributed to, there will only be 30 issues left, and then 20, and then 10
    print(f'The answer is {ans_1b} ways')
    #print answer
    print("")
    #formatting


def q2():
    print("Question 2a: How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?")
    #print question
    print(f'The answer is {indistO_distB(10,8)} ways.')
    #print answer
    print("")
    #formatting
    print("Question 2b: How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins? ")
    #print question
    print(f'The answer is {indistO_distB(12,6)} ways.')
    #print answer
    print("")
    #formatting


def q3():
    print("Question 3a: How many ways can Anna, Billy, Caitlin, and Danny be placed into three indistinguishable homerooms?")
    #print question
    print(f'The answer is {distO_indistB(4,3)} ways.')
    #print answer
    print("")
    #formatting
    print("Question 3b: How many ways are there to put five temporary employees into four identical offices?")
    #print question
    print(f'The answer is {distO_indistB(5,4)} ways')
    #print answer
    print("")
    #formatting
def q4():
    print("Question 4a: How many ways can you pack six copies of the same book into four identical boxes?")
    #print question
    print(f'The answer is {indistO_indistB(6,4)} ways.')
    #print answer
    print("")
    #formatting
    print("Question 4b: How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?")
    #print question
    print(f'The answer is {indistO_indistB(5,3)} ways')
    #print answer

#call the functions that solve each question below
q1()
q2()
q3()
q4()



