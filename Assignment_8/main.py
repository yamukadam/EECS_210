'''
Yaeesh Mukadam
EECS 210 Assignment 8
Description: program 
Date: Dec 7, 2023
Inputs: None
Output: prints various answers to euler/hamilton circuits and nim game.
Collaborators: None
'''
from graph import Graph
#import graph class to represent graphs from questions

def euler_g1():
    #creates the g1 graph for euler and runs the function that will print whether or not it is a euler circuit and if so finds it
    euler_g1 = Graph()
    euler_g1.add_edge('a','e')
    euler_g1.add_edge('b','a')
    euler_g1.add_edge('b','e')
    euler_g1.add_edge('e','d')
    euler_g1.add_edge('e','c')
    euler_g1.add_edge('d','c')
    euler_g1.find_euler_circuit()

def euler_g2():
    #creates the g2 graph for euler and runs the function that will print whether or not it is a euler circuit and if so finds it
    euler_g2 = Graph()
    euler_g2.add_edge('a','b')
    euler_g2.add_edge('a','d')
    euler_g2.add_edge('d','c')
    euler_g2.add_edge('c','b')
    euler_g2.add_edge('e','a')
    euler_g2.add_edge('e','b')
    euler_g2.add_edge('e','c')
    euler_g2.add_edge('e','d')
    euler_g2.find_euler_circuit()

def euler_g3():
    #creates the g3 graph for euler and runs the function that will print whether or not it is a euler circuit and if so finds it
    euler_g3 = Graph()
    euler_g3.add_edge('a','b')
    euler_g3.add_edge('a','c')
    euler_g3.add_edge('a','d')
    euler_g3.add_edge('c','d')
    euler_g3.add_edge('b','d')
    euler_g3.add_edge('b','e')
    euler_g3.add_edge('d','e')
    euler_g3.find_euler_circuit()

def euler_bridge():
    #creates the bridge graph for euler and runs the function that will print whether or not it is a euler circuit and if so finds it
    euler_bridge = Graph()
    euler_bridge.add_edge('a', 'c')
    euler_bridge.add_edge('a', 'c')
    euler_bridge.add_edge('a', 'b')
    euler_bridge.add_edge('a', 'b')
    euler_bridge.add_edge('a', 'd')
    euler_bridge.add_edge('b', 'd')
    euler_bridge.add_edge('c', 'd')
    euler_bridge.find_euler_circuit()

def euler_b():
    #recreates the part b graph for euler and runs the function that will print whether or not it is a euler circuit and if so finds it
    euler_bridge = Graph()
    euler_bridge.add_edge('a','b')
    euler_bridge.add_edge('b','c')
    euler_bridge.add_edge('c','f')
    euler_bridge.add_edge('f','i')
    euler_bridge.add_edge('i','h')
    euler_bridge.add_edge('h','g')
    euler_bridge.add_edge('g','d')
    euler_bridge.add_edge('d','a')
    euler_bridge.add_edge('e','b')
    euler_bridge.add_edge('e','f')
    euler_bridge.add_edge('e','h')
    euler_bridge.add_edge('e','d')
    euler_bridge.add_edge('d','b')
    euler_bridge.add_edge('h','f')
    euler_bridge.find_euler_circuit()


def hamilton_g1():
    #creates g1 graph for hamilton to be used for both dirac and ore theroems
    hamilton_g1 = Graph()
    hamilton_g1.add_edge('a', 'b')
    hamilton_g1.add_edge('b', 'c')
    hamilton_g1.add_edge('c', 'd')
    hamilton_g1.add_edge('d', 'e')
    hamilton_g1.add_edge('e', 'a')
    hamilton_g1.add_edge('a', 'c')
    hamilton_g1.add_edge('b', 'e')
    hamilton_g1.add_edge('e', 'c')
    return hamilton_g1

def hamilton_g2():
    #creates g2 graph for hamilton to be used for both dirac and ore theroems
    hamilton_g2 = Graph()
    hamilton_g2.add_edge('a', 'b')
    hamilton_g2.add_edge('b', 'c')
    hamilton_g2.add_edge('c', 'd')
    hamilton_g2.add_edge('d', 'b')
    return hamilton_g2

def hamilton_g3():
     #creates g3 graph for hamilton to be used for both dirac and ore theroems
    hamilton_g3 = Graph()
    hamilton_g3.add_edge('a', 'b')
    hamilton_g3.add_edge('b', 'g')
    hamilton_g3.add_edge('g', 'e')
    hamilton_g3.add_edge('e', 'c')
    hamilton_g3.add_edge('c', 'd')
    hamilton_g3.add_edge('e', 'f')
    hamilton_g3.add_edge('b', 'c')
    return hamilton_g3

def hamilton_b():
     #recreates part b graph for hamilton to be used for both dirac and ore theroems
    ham_b = Graph()
    ham_b.add_edge('a','b')
    ham_b.add_edge('a','c')
    ham_b.add_edge('c','b')
    ham_b.add_edge('c','f')
    ham_b.add_edge('f','d')
    ham_b.add_edge('d','e')
    ham_b.add_edge('f','d')
    return ham_b
    



def dirac_g1():
    #will get graph from hamilton_g1 func and run func to see whether or not dirac theorem applies
    my_graph = hamilton_g1()
    if my_graph.dirac():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def dirac_g2():
    #will get graph from hamilton_g2 func and run func to see whether or not dirac theorem applies
    my_graph = hamilton_g2()
    if my_graph.dirac():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def dirac_g3():
    #will get graph from hamilton_g3 func and run func to see whether or not dirac theorem applies
    my_graph = hamilton_g3()
    if my_graph.dirac():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def dirac_b():
    #will get graph from hamilton_b func and run func to see whether or not dirac theorem applies
    my_graph = hamilton_b()
    if my_graph.dirac():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def ore_g1():
    #will get graph from hamilton_g1 func and run func to see whether or not ore theorem applies
    my_graph = hamilton_g1()
    if my_graph.ore():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def ore_g2():
    #will get graph from hamilton_g2 func and run func to see whether or not ore theorem applies
    my_graph = hamilton_g2()
    if my_graph.ore():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")

def ore_g3():
    #will get graph from hamilton_g3 func and run func to see whether or not ore theorem applies
    my_graph = hamilton_g3()
    if my_graph.ore():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")
def ore_b():
    #will get graph from hamilton_b func and run func to see whether or not ore theorem applies
    my_graph = hamilton_b()
    if my_graph.ore():
        print("This graph is a hamilton circuit.")
    else:
        print("This may or may not be a hamilton circuit.")


def main():
    #prints all the answers with proper formatting
    print("Question 1 Part A Graph G1:")
    euler_g1()
    print("")
    print("Question 1 Part A Graph G2:")
    euler_g2()
    print("")
    print("Question 1 Part A Graph G3:")
    euler_g3()
    print("")
    print("Question 1 Part A Graph: Bridge:")
    euler_bridge()
    print("")
    print("Question 1 Part B:")
    euler_b()
    print("")
    print("Question 2 Part A Graph G1:")
    dirac_g1()
    print("")
    print("Question 2 Part A Graph G2:")
    dirac_g2()
    print("")
    print("Question 2 Part A Graph G3:")
    dirac_g3()
    print("")
    print("Question 2 Part B")
    dirac_b()
    print("")
    print("Question 3 Part A Graph G1:")
    ore_g1()
    print("")
    print("Question 3 Part A Graph G2:")
    ore_g2()
    print("")
    print("Question 3 Part A Graph G3:")
    ore_g3()
    print("")
    print("Question 3 Part B")
    ore_b()
    print("")
    


main()
    

