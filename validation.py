# Hannah Peluso
# PA 3 Part 2 - Validation problem
# Dec. 9, 2022

def main():
    # assign the input and output files
    print("enter the graph input file name: ")
    fileName = input()
    inputFile = open(fileName, "a+")
    print("enter the proposed coloring file name: ")
    output = open(input(), "r")
    
    # copy all contents of the output file to the bottom of the input file
    with inputFile as f:
        f.write(output.read())
    print("file write complete")
    
    f = open(fileName, "r")
    #call the validate function
    validate(f)

def validate(inputFile):
    
    # assign v and e variables 
    ve = inputFile.readline()
    v = int(ve.split()[0])
    e = int(ve.split()[1])
    
    edges = []
    # while the input file lines are splittable, read in the edges pairs 
    for i in range(e):
        edge = inputFile.readline()
        v1 = int(edge.split()[0])
        v2 = int(edge.split()[1])
        edges.append((v1, v2))
    print(edges)
    # make a set of colorings containing the vertex and its color
    colorings = []
    # for the number of vertices, read in the colorings as a pair with the vertex
    for i in range(v):
        # add the vertex and its color to the set
        colorings.append((i, int(inputFile.readline())))
        # print the vertex and its color
        
    # for each edge in the set of edges, check if the vertices have the same color, if they do, print invalid
    for edge in edges:
        e1 = colorings[edge[0]]
        e2 = colorings[edge[1]]
        if (e1[1] == e2[1]):
            print("INVALID")
            return
    # otherwise, if the coloring is valid, print valid
    print("VALID")
    return

main()