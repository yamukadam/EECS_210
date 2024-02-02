'''
Yaeesh Mukadam
EECS 210 Assignment 2
Description: Python code that finds truth values for various assertions.
Date: Sep 11, 2022
Inputs: None
Output: True/False values for various assertions proofs for the truth value
Collaborators: None
'''

domain_1 = [0,1,2,3,4,5,6,7,8,9,10]
# list of the domain values given for problem 1 so i can iterate through it for each problem

def one_a():
    #problem 1a
    for num in domain_1:
        #iterate through domain
        if num <2:
            #if a number in the domain is less than 2, then the assertion will be proven true.
            print(f"x = {num} makes this true.")
            #print what number made assertion true
            return True
            #returns true ending the function
    #if code reaches this point, that means no number was found in the domain that made the assertion true, therefore the assertion was false
    print("False as there is no such value in the domain that will make the assertion true.")
    #print that assertion was false
    return False
    #return false



def one_b():
    #problem 1b
    for num in domain_1:
        #iterate through domain
        if num >=2:
            #if a number is found in the domain greater than or equal to 2, then the assertion will be proven false
            print(f"x = {num} makes this false.")
            #print what number made assertion false
            return False
            #return False ending the function
    #if code reaches this point, then that means no number was found in the domain that made the assertion false, therefore the assertion was true.
    print("The assertion is true for all values in the domain.")
    #print assertion was true
    return True
    #return true


def one_c():
    #problem 1c
    def left_side(x):
        #returns left side which is p(x)
        return x < 2
    def right_side(x):
        #returns right side which is q(x)
        return x>7
    for num in domain_1:
        #iterate through domain
        if left_side(num) or right_side(num):
            #if either p(x) or q(x) are true, then the assertion will be true
            print(f"x = {num} makes this assertion true")
            #print what number in domain made it true
            return True
            #return true ending the function
    #if code reaches this point, then no number was found in the domain that makes the assertion true, therefore the assertion was false
    print(f"False because no value of x in the domain makes this assertion true")
    return False



def one_d():
    #problem 1d
    def left_side(x):
        #returns left side which is p(x)
        return x < 2
    def right_side(x):
        #returns right side which is q(x)
        return x>7
    for num in domain_1:
        #iterate through domain
        if (left_side(num) or right_side(num)) == False:
            #if either p(x) or q(x) are false, then the assertion will be false
            print(f"x = {num} makes this assertion false.")
            #print what number in domain made it false
            return False
            #return false
    #if code reaches this point, then no number was found in the domain that makes the assertion false, therefore the assertion was true
    print(f"True because no value of x in the domain makes this assertion false")
    return True

def one_e():
    #problem 1e
    #What I am proving ->    ∃x¬P(x)≡¬∀xP(x)
 
    def p(x):
        #returns p(x)
        return x<5
    def not_p(x):
        #returns not p(x)
        return x>=5
    def left_side():
        #finds whether or not left side is false or true
        for num in domain_1:
            #iterate through domain
            if not_p(num):
                #if there exists a num where not p is true, then the left side is true
                print(f"x = {num} makes the left side true")
                #print what num made left side true
                return True
                #return true and end function
        #if code reached this point then left side was false
        return False
        #return false
    def right_side():
        #finds whether or not right side is true or false
        for num in domain_1:
            #iterate through domain
            if not p(num):
                #if there exists at least one time where p(x) is not true, then the right side is true
                print(f"x = {num} makes the right side true")
                #print what num made right side true
                return True
                #returns true and ends function
        #if code reached this point then right side was false
        return False
    
    if left_side() == right_side():
    #if left and right side are equal then the law is true
        print("Both left and right sides are true, therefore the law is proven true.")
        #print law is true
        return True
        #return true
    else:
    #else law is false
        print("Both sides were not equal, therefore the law was incorrect")
        #print law is false
        return False
        #return false



def one_f():
     #problem 1f
    #What I am proving ->     ∀x¬P(x)≡¬∃xP(x)
    def p(x):
        #returns p(x)
        return x<5
    def not_p(x):
        #returns not p(x)
        return x>=5
    def left_side():
        #finds whether or not left side is false or true
        for num in domain_1:
            #iterate through domain
            if not not_p(num):
                #if there exists a num where not not p is true, then the left side is true
                print(f"x = {num} makes the left side false.")
                #print what num made left side true
                return False
                #return false and end function
        #if code reached this point then left side was true
        return True
    def right_side():
        #finds whether or not right side is false or true
        for num in domain_1:
            #iterate through domain
            if p(num):
                #if there exists a num where p is true, then the left side is false
                print(f"x = {num} makes the right side false")
                #print what num made left side true
                return False
                #return false and end function
        #if code reached this point then left side was true
        return True
    
    if left_side() == right_side():
    #if left and right side are equal, then law is true
        print("Both left and right sides are true, therefore the law is proven true.")
        #print law is true
        return True
        #return law
    else:
    #else law is false
        print("Both sides were not equal, therefore the law was incorrect")
        #print law is false
        return False
        #return false




#make list of domain for problem 2 so i can iterate it through for the problems
#only one domain because x and y have the same domain
domain_2 = [1,2,4,5,10,.5,.25,.2,.1]

def two_a():
    #problem 2a
    for x in domain_2:
        #iterate through domain for x values
        for y in domain_2:
            #nested for loop to iterate domain for y values
            if x * y != 1:
                #if x * y is not equal to 1, then the assertion will be false
                print(f'x = {x} and y = {y} make the assertion false.')
                #print what values of x and y make assertion false
                return False
                #return false ending function
    #if function reaches this point, then no numbers were found in domain that prove assertion false, therefore the assertion was true
    return True

def two_b():
    #problem 2b
    for x in domain_2:
        #iterate through domain for x values
        check = False
        #create a check value to assess situation after every y loop and set it to false every time x loop starts again
        for y in domain_2:
            #nested for loop to iterate domain for y values
            if x * y == 1:
            #checks if x * y = 1
                check= True
                #change check to true because a y value was found that made the predicate true for the given x value
                print(f"For x = {x}, y = {y} makes the assertion true.")
                #print what value of x and y make the assertion true
                break
                #break so the y loop ends
        if not check:
            #if the check variable was not changed to true, then that means no value of y was found that made the predicate true, therefore the assertion was false
            print(f"For x = {x}, there is no y value to make the assertion true. Therefore the assertion is false.")
            #print no y value worked with the specific x value to make the assertion true
            return False
            #return false and end function
    #if code reaches this point, that means the assertion was true.
    return True
    #return true


def two_c():
    #problem 2c
    for y in domain_2:
        #iterate through domain for y values
        check = False
        #create a check value to assess situation after every y loop and set it to false every time x loop starts again
        for x in domain_2:
            #nested for loop to iterate domain for y values
            if x * y == 1:
            #checks if x * y = 1
                check= True
                #change check to true because a y value was found that made the predicate true for the given x value
                print(f"For y = {y}, x = {x} makes the assertion true.")
                #print what value of x and y make the assertion true
                break
                #break so the y loop ends
        if not check:
        #if the check variable was not changed to true, then that means no value of y was found that made the predicate true, therefore the assertion was false
            print(f"For y = {y}, there is no x value to make the assertion true. Therefore the assertion is false.")
             #print no y value worked with the specific x value to make the assertion true
            return False
            #return false and end function
    #if code reaches this point, that means the assertion was true.
    return True
    #return true
def two_d():
    #problem 2d
    temp_domain = [1,2,4,5,10,.5,.25,.2,.1]
    #make a copy of domain_2 and call it temp domain
    for x in temp_domain:
        #iterate through domain for x values
        for y in temp_domain:
            #iterate through y values in domain
            if x*y != 1:
                #check if x*y does not equal 1, if it does that means not all y values worked for that given x value
                print(f'for x = {x}, y = {y} makes it false')
                #print the values of x and y that made it false
                temp_domain = temp_domain[1:]
                #pop index 0 from the temp domain
                break
                #break the y loop
    #after the nested for loop ends, check if temp_domain has any values inside it. If it does that means that value didn't get popped which means it went through the entire y loop without x*y != 1 a single time which means the assertion was true for that given x value.
    if temp_domain:
        #check if temp domain has values inside, if so, the assertion is true
        print(f"for x = {x}, all y-values are true")
        #print for what given x value, the assertion was true for
        return True
        #return true ending function
    #if function reaches this point, then nothing was inside temp domain, therefore no x values were found and the assertion was false
    return False


def two_e():
    #problem 2e
    temp_domain = [1,2,4,5,10,.5,.25,.2,.1]
    #make a copy of domain_2 and call it temp domain
    for y in temp_domain:
        #iterate through domain for y values
        for x in temp_domain:
            #iterate through domain for x values
            if x*y != 1:
                #check if x*y does not equal 1, if it does that means not all y values worked for that given x value
                print(f'for y = {y}, x = {x} makes it false')
                #print the values of x and y that made it false
                temp_domain = temp_domain[1:]
                #pop index 0 from the temp domain
                break
                #break the y loop
    #after the nested for loop ends, check if temp_domain has any values inside it. If it does that means that value didn't get popped which means it went through the entire y loop without x*y != 1 a single time which means the assertion was true for that given x value.
    if temp_domain:
        #check if temp domain has values inside, if so, the assertion is true
        print(f"for y = {y}, all x-values are true")
        #print for what given y value, the assertion was true for
        return True
        #returns true
    #if function reaches this point, then nothing was inside temp domain, therefore no x values were found and the assertion was false
    return False

def two_f():
    #problem 2f
    def p(x,y):
        #returns p(x,y)
        return x*y == 1
    for x in domain_2:
        #iterates through the domain for x values
        for y in domain_2:
            #iterates through the domain for y values
            if p(x,y):
                #if p(x,y) is true, then the assertion is true
                print(f"x = {x} and y = {x} make this assertion true.")
                #prints what values of x and y that can make this assertion true
                return True
                #returns true ending function
    #if function reaches this point, then no values of x and y make assertion true
    print("There are no such values of x and y that make this assertion true.")
            
    return False
    #return false

#The rest of the code is formatting and calling all the functions
print("1a")
print(one_a())
print("")
print("1b")
print(one_b())
print("")
print("1c")
print(one_c())
print("")
print("1d")
print(one_d())
print("")
print("1e")
print(one_e())
print("")
print("1f")
print(one_f())
print("")
print("2a")
print(two_a())
print("")
print("2b")
print(two_b())
print("")
print("2c")
print(two_c())
print("")
print("2d")
print(two_d())
print("")
print("2e")
print(two_e())
print("")
print("2f")
print(two_f())
print("")






