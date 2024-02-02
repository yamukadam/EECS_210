'''
Yaeesh Mukadam
EECS 210 Assignment 5
Description: Python code that will be able to determine function properties and find gcd and linear combinations using euclidean algorithms.
logical equivalences and posets.
Date: Oct 25, 2023
Inputs: None
Output: Print function properties, gcd, and linear combinations
Collaborators: Humza Qureshi, Omar Mohammed, Arnav Jain for the linear_combo_method1 function for part 3.
'''
A = {'a','b','c','d'}
B = {'v','w','x','y','z'}
f = {('a','z'),('b','y'),('c','x'),('d','w')}
def is_func(f):
    #function to see if relation is a function or not
    my_dict = {}
    #create a dict to test, as in dictionaries each key can only be paired to one value, closely resembling a function
    for elem in f:
        #iterate through the relation
        if elem[0] in my_dict:
            #check if the element is already in mapping
            if my_dict[elem[0]] != elem[1]:
                #if the x value of elem is paired with another value, then the relation is not a function
                return False
        else:
            my_dict[elem[0]] = elem[1]
            #map x value to y value in dict for future testing purposes
    #if func reaches here, then f is a function
    return True

def is_injective(f):
    #func to see if f is injective or not
    my_list = []
    #create list to store the outputs of f
    for elem in f:
        #iterate through f
        if elem[1] in my_list:
            #if the output of f is already in my_list, then return False
            return False
        else:
            #else add the output to my_list for future testing purposes
            my_list.append(elem[1])
    #if code reaches here then return f is injective
    return True

def is_surjective(B,f):
    my_set = set()
    #create set that will have all the outputs in it
    for elem in f:
        #add all the outputs in to the set
        my_set.add(elem[1])
    # if my_set is equal to the set of B, then return True, else return False
    return B == my_set

def find_inverse(f):
    inverse = set()
    #create empty set where the inverse will be stored
    for elem in f:
        #iterate through function
        inverse.add((elem[1], elem[0]))
        #reverse input and output which gives inverse, and add to the set containing the inverse pairs
    return inverse
    #return the inverse set

def part_one(A,B,f):
    #create template to test various inputs for part one of the assignment
    print(f'A = {sorted(A)}, B = {sorted(B)}, f = {sorted(f)}')
    #print sets A, B and relation f
    if is_func(f):
        #check to see if the relation is a function, if so print and test rest of the if statements in the body
        print("The relation is a function.")
        if is_injective(f) and is_surjective(B,f):
            #check to see if func is bijective
            print("The function is bijective.")
            inverse_func = find_inverse(f)
            #print the inverse if it is bijective
            print(f"The inverse function is: {inverse_func}")
        elif is_injective(f):
            #if func is not bijective then check to see if it is injective
            print("The function is injective.")
        elif is_surjective(B,f):
            #elif check to see if it is surjective
            print("The function is surjective.")
        else:
            #else print it is not none of them
            print("The function is not injective nor surjective nor bijective.")
        
    else:
        #if not function, then print the statement
        print("The relation is not a function")


def find_gcd(a,b):
    x = max(a,b)
    #make x the greater of a and b
    y = min(a,b)
    #make y the lesser of a and b
    while y!=0:
        #the body of this loop is the euclidean algorithm gotten from the lecture slides
        r = x%y
        #remainder is stored in r
        print(f'{x}/{y} = {x//y} R {r}')
        #print division with remainder in specified format
        x=y
        #change x value to y
        y=r
        #change y to the remainder and loop back through
    #print the gcd in proper format
    print(f'gcd({a},{b}) = {x}')

def linear_combo_method1(a,b):
    x = max(a,b)
    #set x as the max of a and b
    y = min(a,b)
    #set y as the min of a and b
    first_pass = []
    #initialize list to store data from first pass
    print("First Pass: ")
    #clarify first pass
    while y!=0:
        #euclidean algorithm, first pass.
        r = x%y
        #set remainder
        print(f'{x} = {y} * {x//y} + {r}')
        #print in product and sum format
        first_pass.append([x,y,x//y,r])
        #append info in first pass list
        x=y
        #set x equal to y
        y=r
        #set y equal to r
    gcd = x
    #gcd = x
    first_pass.pop()
    #remove the last step in the first pass as it is not needed
    first_pass = first_pass[::-1]
    #reverse the first pass list as we are doing a back pass
    last = first_pass[0]
    #set last to the first index
    s =1 
    result = last[3]
    #result is the 3rd index
    last_a = last[0]
    #a is in the 0 index
    last_b = last[1]
    #b is in the 1st index
    last_q = last[2]
    #q is in the 2nd index
    print("Back Pass: ")
    #indicate back pass is starting
    for a,b,q,r in first_pass[1:]:
        #iterate through the first_pass from 1st index onwards
        print(f"{result} = {s} * {last_a} - {last_q}*{last_b}")
        #print result in product sum format 
        index  =1  if last_b == r else 0 if last_a == r else -1
        #set index = 1 if b is equal to r, else set it = 0
        if index ==1:
            #if index is 1
            print(f"{result} = {s} * {last_a}-{last_q} * ({a} - {q}*{b})")
            #print the corresponding result
            s = last_q*q +s
            #s is equal to given formula
            last_b =a 
            #b is equal to a
        elif index == 0:
            #else
            print(f"{result} = {s} *({a} - {q}*{b}) - {last_q}*{last_b}")
            #print result in sum product format
            last_q = s*q +last_q
            #q is equal to given formula
            last_a = a 
            #last a is equal to a
    print(f"{result} = {s} *{last_a} + {-(last_q)}*{last_b}")
    #print the linear combination
    return s, -last_q


    
    

def linear_combo_method2(a,b):
    s0, s1, t0, t1 = 1,0,0,1
    #initialize s0,s1,t0,t1 as equal to 1,0,0,1 respectively
    x = max(a,b)
    #set x as the max of a and b
    y = min(a,b)
    #set y as the min of a and b
    q_list =[]
    #initialize a list to store the quotients
    while y!=0:
        #loop while y is not equal to 0, runs the euclidean algorithm to get the gcd
        r = x%y
        #remainder is stored in r
        q_list.append(x//y)
        #add the quotients to the quotient list
        x=y
        #change x value to y
        y=r
        #set y value to the remainder
    gcd = x
    #after loop finishes, the x value is the gcd
    s_list = [1,0]
    #initialize the s_list with the already given values of s
    t_list = [0,1]
    #initialize the t_list with the already given values of t
    for i in range(len(q_list)-1):
        #iterates through len of q_list - 1
        tempS = s1
        #store s1 value in temp as s1 will change values soon
        s1 = s0-s1*q_list[i]
        #formula for s1
        s_list.append(s1)
        #add new value of s1 in s_list
        s0=tempS
        #s0 now is the old value of s1 stored in the temp variable
        tempT = t1
        #store t1 value in temp as t1 will change values soon
        t1 = t0-t1*q_list[i]
        #formula for t1
        t_list.append(t1)
        #add new value of t1 in t_list
        t0=tempT
        #t0 now is the old value of t1 stored in the temp variable
    for i in range(1,len(q_list)+1):
        #iterate from 1 to length of q_list + 1 so i corresponds to quotient value as q1 is the first q value not q0
        print(f'q{i} = {q_list[i-1]}, ', end="")
        #print the q values
    print("")
    #formatting
    print("s0= 1, s1= 0, ", end="")
    #print the s values given
    for i in range(2,len(s_list)):
        #first two s values already printed so we start from index 2 and iterate through the len of s_list
        print(f's{i} = s{i-2} - s{i-1}*q{i-1} = {s_list[i-2]} - {s_list[i-1]}*{q_list[i-2]} = {s_list[i]}, ', end="")
        #print s values, and the calculations for each s value
    print("")
    #formatting

    print("t0= 0, t1= 1, ", end="")
    #print the t values given
    for i in range(2,len(t_list)):
        #first two t values already printed so we start from index 2 and iterate through the len of t_list
        print(f't{i} = t{i-2} - t{i-1}*q{i-1} = {t_list[i-2]} - {t_list[i-1]}*{q_list[i-2]} = {t_list[i]}, ', end="")
        #print s values, and the calculations for each s value
    print("")
    #formatting

    if s1*a + t1*b == x:
        #check if that specific combo of s and t satisfies the linear combination
        print(f"gcd({a}, {b}) = {s1}*{a} + {t1}*{b}")
        #print the linear combination
    else:
        print(f"gcd({a}, {b}) = {t1}*{a} + {s1}*{b}")
        #if not, swap s and t and then print linear combination

def part_one_input():
    print("Part 1: ")
    #print part 1
    test_inputs = [
        ({"a","b","c","d"}, {"v","w","x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","w")}),
        ({"a","b","c","d"}, {"x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","z")}),
        ({"a","b","c","d"}, {"w","x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","w")}),
        ({"a","b","c","d"}, {1,2,3,4,5}, {("a",4),("b",5),("c",1),("d",3)}),
        ({"a","b","c"}, {1,2,3,4}, {("a",3),("b",4),("c",1)}),
        ({"a","b","c","d"}, {1,2,3}, {("a",2),("b",1),("c",3),("d",2)}),
        ({"a","b","c","d"}, {1,2,3,4}, {("a",4),("b",1),("c",3),("d",2)}),
        ({"a","b","c","d"}, {1,2,3,4}, {("a",2),("b",1),("c",2),("d",3)}),
        ({"a","b","c"}, {1,2,3,4}, {("a",2),("b",1),("a",4),("c",3)})
    ]
    #include all the test inputs

    for elem in test_inputs:
        #loop through all inputs and run part 1 function
        part_one(elem[0],elem[1],elem[2])
        print("")

def part_two_input():
    print("Part 2: ")
    #print part 2
    test_inputs = [(414,662), (6,14), (24,36), (12,42), (252,198)]
    #include all the test inputs

    for elem in test_inputs:
        #loop through all inputs and run part 3 function
        find_gcd(elem[0], elem[1])
        print("")

def part3_input():
    print("Part 3: ")
    #print part 3
    test_inputs = [(414,662), (6,14), (24,36), (12,42), (252,198)]
    #include all the test inputs

    for elem in test_inputs:
        #loop through all inputs and run part 3 function
        linear_combo_method1(elem[0], elem[1])
        print("")

def part4_input():
    print("Part 4 ")
    #print part 4
    test_inputs = [(414,662), (6,14), (24,36), (12,42), (252,198)]
    #include all the test inputs

    for elem in test_inputs:
        #loop through all inputs and run part 4 function
        linear_combo_method2(elem[0], elem[1])
        print("")


part_one_input()
part_two_input()
part3_input()
part4_input()


















