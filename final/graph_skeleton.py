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
    def __init__(self):
        self.graph = {} # adjacent list 방식으로 쓸꺼니까 dictionary로 생성 

    def addEdges(self, vertices, edges, weight): # 새로운 edge 추가
        if vertices not in self.graph.keys(): # 만약 처음 들어온 정점(vertice)라면
            self.graph[vertices] = [] # vertice를 추가해주고, 연결된 vertice는 아직 없으니 빈 list 생성
        self.graph[vertices].append((edges, weight)) # 이미 존재하는 vertice에 연결된 vertice과 weight를 tuple로 추가해줌

    def checkEdges(self, start, end): # 해당 edge가 있는지 검사
        if start in self.graph.keys(): # 만약 시작 vertice가 존재한다면
            if end in dict(self.graph[start]).keys(): # 시작 vertice와 연결된 vertice에 존재한다면
                return True # 존재한다고 return
        return False # 없으면 존재하지 않는다고 return
    
    def adjacentVertices(self, vertices): # 인접 vertice 반환
        if vertices in self.graph.keys(): # 해당 vertice가 graph에 존재한다면
            return self.graph[vertices] # 인접한 vertices list를 return
        return [] # 없으면 빈 list return

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
                # n: number of vertices, m: number of edges
                for j in range(m):
                    i += 1
                    words = lines[i].split()
                    g.addEdges(int(words[0]), int(words[1]), int(words[2]))

            elif op == IS_ADJACENT:
                if len(words) != 3:
                    raise Exception("IS_ADJACENT: invalid input")
                u, v = int(words[1]), int(words[2])
                if g.checkEdges(u, v):
                    outFile.write("%d %d T\n" % (u, v))
                else:
                    outFile.write("%d %d F\n" % (u, v))
            elif op == GET_NEIGHBORS:
                if len(words) != 2:
                    raise Exception("GET_NEIGHBORS: invalid input")
                u = int(words[1])
                for v in g.adjacentVertices(u):
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