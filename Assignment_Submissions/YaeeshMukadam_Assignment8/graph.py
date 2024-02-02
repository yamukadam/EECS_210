'''
Yaeesh Mukadam
EECS 210 Assignment 8
Description: class to represent undirected graphs
Date: Dec 7, 2023
Inputs: None
Output: no output
Collaborators: Utilized chatGPT for algorithm to find euler circuit.
'''
from collections import defaultdict
#import defaultdict

class Graph:
    #class for graph
    def __init__(self):
        self.graph = defaultdict(list)
        #initialize a dictionary that will have vertice as keys and a list of adjacent vertices as values
        self.remaining_edges = defaultdict(list)
        #same as self.graph initially but will be used to find euler ciruit



    def add_edge(self, u, v):
        self.graph[u].append(v)
        #append the edge vertice
        self.graph[v].append(u)
        #append same edge vice versa
        self.remaining_edges[u].append(v)
        #same as self.graph for now
        self.remaining_edges[v].append(u)
        #same as self.graph for now

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        #to remove edge will remove v from u in dict
        self.graph[v].remove(u)
        #have to also remove u from v in dict
    
    def num_edges(self,a):
        return len(self.graph[a])
        #will return num of edges for given vertice


    def euler_exists(self):
        #func to know whether euler circuit exists or not
        for vertice in self.graph:
            #iterate through each vertice
            if self.num_edges(vertice) % 2 != 0:
                #if any given vertice has an odd number of vertices, return false
                return False
        #if func reaches here, graph is a euler circuit
        return True
    
    def euler_circuit_util(self, v, circuit):
        #recursive function to find euler circuit
        #got this code from help of chat gpt
        for neighbor in self.remaining_edges[v]:
            #will iterate through all neighbors of current vertice
            self.remaining_edges[v].remove(neighbor)
            #will remove the edge to make sure it is only traversed once
            self.remaining_edges[neighbor].remove(v)
            #vice versa, symmetrical removal
            self.euler_circuit_util(neighbor, circuit)
            #recursively call function to go through all edges
        
        circuit.append(v)
        #appends the vertices to circuit list
    
    def find_euler_circuit(self):
        #func to see whther or not euler exists and if it does print circcuit
        list_of_odd = []
        #initialize empty list to store odd vertices for printing purposes
        if not self.euler_exists():
            #if the euler circuit does not exist, then print all the vertices that are odd
            for vertice in self.graph:
                #iterate thorugh all vertices
                if self.num_edges(vertice) % 2 == 1:
                    #if num of edges is odd then append it to the list
                    list_of_odd.append(vertice)
            print(f'Not a euler circuit because the following vertices have a odd number of edges: {list_of_odd}')
            #print why it is not euler circuit
                    
        else:
            #else it is a euler circuit
            start_vertex = next(iter(self.graph.keys()))
            #find starting vertex
            circuit = []
            #initialize empty list to store euler circuit vertices
            self.euler_circuit_util(start_vertex, circuit)
            #call the recrusive func to find euler circuit
            print("Euler circuit:", "-".join(circuit[::-1]))
            #print the circuit with list being backwards as circuit list has the order backwards due to backtracking
    


    def dirac(self):
        #func to use dirac theorem
        if len(self.graph) < 3:
            #if num of vertices is less than 3, return false
            return False
        n_2 = len(self.graph) / 2
        #variable for n/1
        for vertices in self.graph.values():
            #iterate through all vertices the graph
            if len(vertices) < n_2:
                #if any of the vertices are less than n/2 then diracs theroem will be false
                return False
        #if reached this point, then return true as there is a hamilton circuit
        return True

    def ore(self):
        #func to use ore theorem
        if len(self.graph) < 3:
            #if num of vertices is less than 3, return false
            return False
        vertices = list(self.graph.keys())
        #create list of vertices to use for iterating purposes
        for i in vertices:
            for j in vertices:
                #double nested for loop
                if i !=j:
                    #condition to make sure same vertices are not being added together
                    if i not in self.graph[j]:
                        #condition to check if vertices are not adjacent
                        if len(self.graph[i]) + len(self.graph[j]) < len(vertices):
                            #if degree of i + degree of j is less than num of vertices, return false
                            return False
        #if reached this point, then return true as there is a hamilton circuit
        return True



            





