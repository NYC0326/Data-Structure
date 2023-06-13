# Practice 11. Graph Traversals and Topological Sort
import sys
from collections import deque
CONSTRUCT = 'C'
BFS = 'B'
DFS = 'D'
TOPOLOGICAL_SORT = 'T'

class Graph:
    def __init__(self):
        self.graph = {} # adjacent list 방식으로 쓸꺼니까 dictionary로 생성 

    def addEdges(self, vertices, edges, weight): # 새로운 edge 추가
        if vertices not in self.graph.keys(): # 만약 처음 들어온 정점(vertice)라면
            self.graph[vertices] = [] # vertice를 추가해주고, 연결된 vertice는 아직 없으니 빈 list 생성
        self.graph[vertices].append((edges, weight)) # 이미 존재하는 vertice에 연결된 vertice과 weight를 tuple로 추가해줌

    def BFS(self, v):
        result = [] # 방문 순서 저장 list
        q = deque() # Queue Initialize
        visited = {} # 방문한 vertice는 1, 미방문한 vertice는 0으로 저장

        for i in self.graph.keys(): # 존재하는 모든 vertice를 찾아서, 아직 미방문 상태이므로 value를 0으로 초기화
            visited[i] = 0
            for j in self.graph[i]:
                visited[j[0]] = 0
        q.append(v)

        while q: # Connected Graph에서 미방문한 vertice가 있을 때 까지 반복
            v = q.popleft()
            if not visited[v]: # 미방문이면 visited[v] = 0 (False)
                visited[v] = 1 # 방문으로 변경
                result.append(v) # 방문했으므로 결과에 추가
            if v in self.graph.keys(): # outdegree가 0이 아닌 경우 (내가 시작인 edge가 있는 경우)
                for node in self.graph[v]: # set을 쓰면 더 간단하게 추가 가능하지만 그럴려면 가중치를 저장을 못하므로 여기서는 생략
                    if not visited[node[0]]: # 방문 안한 노드가 있을 경우
                        q.append(node[0]) # 큐에 추가 (방문할 노드 목록)
        
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
        result = [] # 결과
        q = deque() # Queue 초기화 (선입선출이라)
        indegree = {} # 방문 여부보다는 indegree가 중요, indegree가 0인 vertice부터 우선 방문하는 것이 Topological Sort
        for i in self.graph.keys(): # 모든 vertice에 대하여 indegree initialize
            indegree[i] = 0
            for j in self.graph[i]:
                indegree[j[0]] = 0
        
        for i in self.graph.keys(): # indegree 계산
            for j in self.graph[i]:
                indegree[j[0]] += 1
        
        for i in indegree.keys():
            if not indegree[i]: # indegree[i] == 0 이면 False니까
                q.append(i)
        
        while q:
            node = q.popleft() 
            result.append(node) # 방문 vertice 기록

            if node in self.graph.keys(): # 해당 vertice와 연결되어 있는 vertice들에 대해
                for i in self.graph[node]:
                    indegree[i[0]] -= 1 # edge를 삭제하므로 indegree를 하나씩 낮춤
                    if indegree[i[0]] == 0: # 만약 indegree를 낮췄는데 0이라면 queue에 추가
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
                # n: number of vertices, m: number of edges
                for j in range(m):
                    i += 1
                    words = lines[i].split()
                    g.addEdges(int(words[0]), int(words[1]), int(words[2]))
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