# Practice 10. Graph Representation 
import sys
from collections import deque
CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'

class Graph:
  # TODO. Define a constructor and proper methods
    def __init__(self):
        self.graph = {}

    def addEdges(self, vertices, edges):
        try:
            self.graph[vertices].append(edges)
        except:
            self.graph[vertices] = []
            self.graph[vertices].append(edges)

    def checkEdges(self, start, end):
        if start in self.graph.keys():
            for i in self.graph[start]:
                if end == i[0]:
                    return True
        return False
    
    def checkAdjacency(self, vertices):
        try:
            return self.graph[vertices]
        except:
            return []




if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    g = Graph()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if op == CONSTRUCT:
                if len(words) != 3:
                    raise Exception("CONSTRUCT: invalid input")
                n, m = int(words[1]), int(words[2])
                cnt, data = m, []
                # TODO. Construct a graph
                for j in range(cnt):
                    i+=1
                    words = lines[i].split()
                    g.addEdges(int(words[0]), (int(words[1]), int(words[2])))

            elif op == IS_ADJACENT:
                if len(words) != 3:
                    raise Exception("IS_ADJACENT: invalid input")
                u, v = int(words[1]), int(words[2])
                # TODO. Check if edge (u, v) exists in the graph
                if g.checkEdges(u, v) == True:
                    outFile.write("%d %d T\n" % (u, v))
                else:
                    outFile.write("%d %d F\n" % (u, v))

            elif op == GET_NEIGHBORS:
                if len(words) != 2:
                    raise Exception("GET_NEIGHBORS: invalid input")
                u = int(words[1])
                # TODO. Get all the neighbors of u
                for v in g.checkAdjacency(u):
                    outFile.write("%d " % v[0])
                outFile.write("\n")


            else:
                raise Exception("Undefined operator")
            i += 1
    for v in g.graph:
        print("%s: " % v, end = '')
        for j in g.graph[v]:
            print(j, end = ' ')
        print()