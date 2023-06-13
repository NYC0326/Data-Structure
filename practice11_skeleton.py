# Practice 10. Graph Representation 
import sys
from collections import deque
CONSTRUCT = 'C'
BFS = 'B'
DFS = 'D'
TOPOLOGICAL_SORT = 'T'

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

    def BFS(self, v):
        result = []
        q = deque()
        visited = {}
        for i in self.graph.keys():
            visited[i] = 0
            for j in self.graph[i]:
                visited[j[0]] = 0
        q.append(v)

        while q:
            v = q.popleft()
            if not visited[v]:
                visited[v] = 1
                result.append(v)
            if v in self.graph.keys():
                for node in self.graph[v]:
                    if not visited[node[0]]:
                        q.append(node[0])
        return result

    def DFS(self, v):
        result = []
        stk = deque()
        visited = {}
        for i in self.graph.keys():
            visited[i] = 0
            for j in self.graph[i]:
                visited[j[0]] = 0
            stk.append(v)

        while stk:
            v = stk.pop()
            if not visited[v]:
                visited[v] = 1
                result.append(v)
            if v in self.graph.keys():
                for node in self.graph[v]:
                    if not visited[node[0]]:
                       stk.append(node[0])
        return result

    def TopologicalSort(self):
        result = []
        q = deque()
        indegree = {}
        for i in self.graph.keys():
            indegree[i] = 0
            for j in self.graph[i]:
                indegree[j[0]] = 0
        
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                indegree[j[0]] += 1

        for i in indegree.keys():
            if not indegree[i]:
                q.append(i)
        
        while q:
            curr = q.popleft()
            result.append(curr)
            
            if curr in self.graph.keys():
                for i in self.graph[curr]:
                    indegree[i[0]] -= 1
                    if indegree[i[0]] == 0:
                        q.append(i[0])
        return result

        
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

            elif op == BFS:
                if len(words) != 2:
                    raise Exception("BFS: invalid input")
                v = int(words[1])
                ans = g.BFS(v)
                for a in ans:
                    outFile.write(str(a) + " ")
                outFile.write("\n")     

            elif op == DFS:
                if len(words) != 2:
                    raise Exception("DFS: invalid input")
                v = int(words[1])
                ans = g.DFS(v)
                for a in ans:
                    outFile.write(str(a) + " ")
                outFile.write("\n")
                
            elif op == TOPOLOGICAL_SORT:
                if len(words) != 1:
                    raise Exception("Topological sort: invalid input")
                ans = g.TopologicalSort()
                for a in ans:
                    outFile.write(str(a) + " ")
                outFile.write("\n")

            else:
                raise Exception("Undefined operator")
            i += 1
    for v in g.graph:
        print("%s: " % v, end = '')
        for j in g.graph[v]:
            print(j, end = ' ')
        print()