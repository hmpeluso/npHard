# Hannah Peluso
# PA 3 Part 1- NP Hard Coloring problem
# Dec. 9, 2022

def main():
    # read in the graph
    print("Enter the graph file name: ")
    print()
    # read in the file given by standard input
    graphIn = open(input(), "r")
    
    # read in the first number of the file
    ve = graphIn.readline()
    # split the first line into two numbers
    if ve == "":
        print("The file is empty.")
        return
    # if the first line is not splittalble into two numbers, return
    if len(ve.split()) != 2:
        print("Please enter a properly formatted file.")
        return
    v = int(ve.split()[0])
    e = int(ve.split()[1])
    
    # label vertices starting at 0
    vertices = []
    for i in range(v):
        vertices.append(i)
        
    # create a set of ordered pairs to store the edges
    edges = []
    # for the rest of the lines of the file, read in the edges
    for i in range(e):
        edge = graphIn.readline()
        # split the edges into two numbers
        v1 = int(edge.split()[0])
        v2 = int(edge.split()[1])
        # store the edges in the set
        edges.append((v1, v2))
        
    #call coloring function
    print("The graph coloring will be printed to the output file.")
    print()
    coloring(vertices, edges)
    print("coloring found in output file!")
    print()
    
def coloring(vertices, edges):
    # define a new list to store the colors
    coloring = []
    colCount = 0
    
    # for each vertex, assign a color
    for v in vertices:
        # make a subset of the edges that are from the vertex
        edgeSet = []
        for e in edges:
            # if the edge is from the vertex, add it to the subset
            if (v == e[0] or v == e[1]):
                edgeSet.append(e)
        
        # if the color is not already assigned to any vertex, assign it to the vertex
        for ed in edgeSet:
            if (v, colCount) in coloring:
                break
            
            # if the colCount is either of the colors in the edge, increment the colCount and assign
            if (v == ed[0]):
                # if coloring contains the opposite vertex, increment the colCount
                if (ed[1], colCount) in coloring:
                    colCount += 1
                    coloring.append((v, colCount))
                else:
                    coloring.append((v, colCount))
            else: 
                if (ed[0], colCount) in coloring:
                    colCount += 1
                    coloring.append((v, colCount))
                else:
                    coloring.append((v, colCount))
                    
    # ask for the name of the output file
    print("Enter the output file name: ")
    outFile = open(input(), "w")
    outFile.truncate()
    
    #print colors into the output file in order of nodes and with a newline after each node
    for c in coloring:
        outFile.write(str(c[1]) + "\n")

    
main()