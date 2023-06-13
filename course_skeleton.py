import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
    def __init__(self, i, n, p=None): # 초기값 세팅, p는 넣어주지 않으면 default로 None으로 저장됨
        self.ID = i
        self.name = n
        self.next = p

class Course:
    def __init__(self, l=[]):
        self.tail = Student(None, None)
        self.head = Student(None, None, self.tail)

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def addStudent(self, newID, newName):
        node = self.head
        if node.next.ID == None:
            self.head.next = Student(newID, newName, self.tail)
            return True
        else:
            while True:
                if node.next.ID == newID:
                    return False
                elif node.next.ID == None:
                    node.next = Student(newID, newName, node.next)
                    return True
                elif node.next.ID < newID:
                    node = node.next
                else:
                    node.next = Student(newID, newName, node.next)
                    return True

    def deleteStudent(self, queryID):
        node = self.head.next
        while node.ID != None:
            if node.next.ID == queryID:
                node.next = node.next.next
                return True
            else:
                node = node.next
        return False

    def find(self, queryID):
        node = self.head
        while node.next.ID != None:
            if node.ID == queryID:
                return node
            else:
                node = node.next
        return False

    def write(self, outFile):
        node = self.head.next
        while node.ID != None:
            outFile.write(str(node.ID) + " " + node.name + " ")
            node = node.next
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
                    outFile.write(str(found.ID) + " " + found.name + "\n")
            else:
                raise Exception("Undefined operator")