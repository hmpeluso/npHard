# npHard

Your task is to write two programs. The first is a program that takes as input a first line containing two numbers V and E, separated by a space telling you the number of vertices and edges in a graph. The vertices are identified with the indices 0 through V-1. The rest of the file consists of E lines, each of which has two numbers i and j separated by a space representing an undirected edge from vertex i to vertex j. 

For example: 

3 3
0 1
1 2
2 0
Represents a triangle graph with 3 vertices. 

Your program should read the graph in from standard output and produce a coloring with as few colors as you are able to. The output should consist of V lines, one for each vertex, with an index staring at 0 for the first color, 1 for the second color, 2, for the third, etc. For example, for the triangle graph above, an acceptable output would be: 

0
1
2
meaning that vertex 0 is assigned color 0, vertex 1 is assigned color 1, and vertex 2 is assigned color 2. Remember that no two vertices connected by the same edge should be given the same color. 

Your second program should be a verification algorithm. It's input is essentially both the input to the previous program and the output. In other words, the first line should be V E as above, followed by the E lines representing the graph edges, then followed by V additional lines representing a proposed coloring. Your code should output a single line containing either the word Valid or the word Invalid depending on whether the given coloring was valid or invalid. 

