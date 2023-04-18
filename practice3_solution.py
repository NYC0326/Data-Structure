import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
  def __init__(self, i, n, p=None):
    self.id = i
    self.name = n
    self.next = p

class Course:
  def __init__(self, l=[]):
    if not l: # 초기값이 없으면 새로운 Course 객체를 만들고 head와 size를 초기화해둠
        self.head = None
        self.size = 0
    else: # 초기값을 준다면, 첫번째 요소인 l[0]을 head로, size는 l의 길이인 len(n)으로 지정 한 후, 하나씩 탐색하면서 node를 연결해줌
      self.head = Node(l[0]) # 그러나 이 코드에선 Course 객체를 선언할 때, 초기값을 주는 경우도 없을 뿐더러 Node라는 객체 또한 없음
      self.size = len(l) # 그래서 이 코드가 실행되는 경우가 없어서 에러가 안남. 굳이 바꿔주자면 self.head = Student(l[0][0], l[0][1])로..?
      curr = self.head
      for x in l[1:]:
        curr.next = Node(x)
        curr = curr.next

  def __len__(self): # 그냥 linked list 길이 반환하는 함수
    return self.size

  def isEmpty(self): # 비어있으면 True, 차있다면 False를 반환하는 함수
    return self.size == 0 # 비어있으면 self.size == 0 이 True일 것이니 그냥 이렇게 짜면 됨 if문으로 나누지 말고

  def addStudent(self, newID, newName):
    if self.isEmpty(): # 만약에 Course가 없다면 새로 입력된 것을 head로 넣어주고, size는 하나 키우면 됨
      self.head = Student(newID, newName)
      self.size += 1
      return True # 그리고 그냥 main 함수 보면 True/False 반환해야해서 True 반환해주면 됨
    # Add a node at the beginning
    if newID < self.head.id: # 만약 삽입하고자 하는 Student의 ID가 head보다 작다면
      temp = self.head # 원래 head인 Student 객체를 temp에 복사한 후
      self.head = Student(newID, newName, temp) # 새로운 Student 객체를 head로 바꿔주고 노드에 temp(바뀌기 전 head)를 연결해줌
      self.size += 1 # 사이즈 하나 키워주고
      return True
    else: # 삽입하고자 하는 Student의 ID가 head보다 작지 않다면, 그냥 뒤에 넣으면 되니까 탐색하다가 끼워 넣어주면 됨
      prev = None # 이전 노드, 시작은 None으로
      curr = self.head # 현재 노드, 시작은 head로
      while curr: # 만약 현재 노드가 있을 때
        if curr.id == newID: # 만약에 현재 노드의 id랑 newID가 같다면 삽입하면 안되니까 False를 반환함
          return False
        if (not prev or prev.id < newID) and (newID < curr.id): # 이전 노드가 없거나, 이전 노드의 id보다 newID가 더 크고, newID가 현재 노드의 id보다 작으면
          newNode = Student(newID, newName, curr) # 그 두 노드 사이에 삽입을 해야하니 새로운 노드를 만들어주고 (다음 노드는 curr)
          # Add a node in the middle
          prev.next = newNode # 이전 노드의 다음 노드는 새로운 노드를 가르키게끔 만들어 주면 끝
          self.size += 1
          return True
        prev = curr # 그 외의 경우에는 다음꺼 탐색해야하니까 이전노드를 현재노드로,
        curr = curr.next # 현재 노드는 다음 노드로 바꿔줌
      # Add a node at the end
      prev.next = Student(newID, newName)
      # 만약 위에서 삽입이 안됐다면, 맨 마자막에 삽입해줘야하는 경우이므로 이전 노드에 (그게 while문 끝나면 맨 마지막 노드임) 다음 노드로 연결해줌
      self.size += 1
      return True

  def deleteStudent(self, queryID): # 학생 삭제
    if self.isEmpty(): # 만약에 비어 있으면 삭제할게 없으므로
      print("DELETE: no element exists")
      return False
    curr = self.head # 현재 노드를 시작은 head로 지정
    prev = None # 이전 노드를 시작은 None으로 지정
    while curr: # 현재 노드가 있을 때 동안
      if curr.id == queryID: # 만약에 현재 노드의 id가 삭제하고자 하는 학생의 id랑 같다면
        if not prev: # 삭제하고자 하는 노드의 이전 노드가 없다면 (== head라면)
          self.head = curr.next # head를 다음 노드로 바꿔줌
        else: # 그 외의 경우에는 이전 노드의 다음 노드를 현재 노드의 다음 노드로 지정해줌
          prev.next = curr.next
        self.size -= 1 # 사이즈 하나 줄이고
        return True # 삭제 됐으니까 True 반환
      elif curr.id > queryID: # 만약에 계속 탐색했는데 삭제하고자 하는 학생의 id보다 큰 id가 나타났다면 (해당 학생의 id와 일치하는 노드가 없다면)
        return False # 삭제할 수 없으므로 False 반환
      prev = curr # 삭제된 경우가 아니라면 이전 노드를 현재 노드로
      curr = curr.next # 현재 노드를 다음 노드로 바꿔줌
    return False

  def find(self, queryID): # 찾는거
    if self.isEmpty(): # 리스트가 비어있으면 검색 결과 없다고 반환
      print("FIND: no such element exists")
      return None
    curr = self.head # 탐색할꺼니 시작은 head로
    while curr: # 노드가 있으면
      if curr.id == queryID: # 만약 현재 노드랑 찾는게 같다
        return curr # 현재 노드 반환
      elif curr.id > queryID: # 만약 현재 노드의 id값이 찾고자 하는 id보다 크다면 (찾는 id값을 가진 노드가 없다면)
        return None # 없으니까 None 반환
      curr = curr.next # 그 외의 경우에는 다음꺼 탐색해야하니까 현재 노드를 다음 노드로 변경
    return None # 검색이 안됐다면 None 반환
  
  def print(self):
    curr = self.head
    while curr:
      print(str(curr.id) + " " + str(curr.name) + " ", end="")
      curr = curr.next
    print()

  def write(self, outFile):
    curr = self.head
    while curr:
      outFile.write(str(curr.id) + " " + str(curr.name) + " ")
      curr = curr.next
    outFile.write("\n")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  course = Course()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == ADD:
        if len(words) != 3:
          raise Exception("ADD: invalid input")
        i, n = int(words[1]), words[2]
        if course.addStudent(i, n):
          course.write(outFile)
        else:
          outFile.write("Addition failed\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        if course.deleteStudent(i):
          course.write(outFile)
        else:
          outFile.write("Deletion failed\n")
      elif op == FIND:  
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.id) + " " + found.name + "\n")
      else:
        raise Exception("Undefined operator")
        