# Practice 9. Max Heap
import sys
INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize

class MaxHeap:
    def __init__(self, num=MAX_CAPACITY):
        self.elements = [0] * num
        self.count = 0
        self.capacity = num

    # Given the index i of element, return the index of that element's parent in the heap
    def parent(self, i):
        return i // 2
  
    # Given the index i of element, return the index of that element's left child in the heap
    def left(self, i):
        return 2 * i
  
    # Given the index i of element, return the index of that element's right child in the heap
    def right(self, i):
        return 2 * i + 1

    # Insert a given element elem into the heap
    # If the insertion fails, immediately terminate the program with the error message.
    def insertElement(self, elem):
        if self.count >= self.capacity: # 이미 꽉차 있는 경우
            raise Exception("Cannot insert more than max capacity")
        self.count += 1
        self.elements[self.count] = elem
        
        curr = self.count
        while self.parent(curr) > 0 and self.elements[self.parent(curr)] < self.elements[curr]:
            self.elements[self.parent(curr)], self.elements[curr] = self.elements[curr], self.elements[self.parent(curr)]
            curr = self.parent(curr)
        
    # Return the maximum of the heap if it exists
    # Otherwise, terminate program with an error
    def maximum(self):
        if self.count == 0:
            return False
        return self.elements[1]

    # Delete the maximum from the heap and return the maximum
    # If deletion fails, terminate program with an error
    def deleteMaximum(self):
        if not self.maximum():
            return False
        self.elements[1] = self.elements[self.count]
        curr = 1
        while True:
            if self.elements[self.left(curr)] > self.elements[self.right(curr)]:
                swap = self.left(curr)
            else:
                swap = self.right(curr)
            if self.elements[swap] > self.elements[curr]:
                self.elements[swap], self.elements[curr] = self.elements[curr], self.elements[swap]
                curr = swap
            else:
                break
        self.count -= 1
        return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    
    h = MaxHeap()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == INSERT:
                if len(words) != 2:
                    raise Exception("INSERT: invalid input")
                i = int(words[1])
                # TODO. Call the insertion method
                h.insertElement(i)
                for i in range(1, h.count+1):
                    outFile.write(str(h.elements[i]) + " ")
                outFile.write("\n")
            elif op == DELETE:
                ans = h.deleteMaximum()
                if not ans:
                    raise Exception("Deletion Failed! No maximum")
                for i in range(1, h.count+1):
                    outFile.write(str(h.elements[i]) + " ")
                outFile.write("\n")
            elif op == MAXIMUM:
                ans = h.maximum()
                if not ans:
                    raise Exception("No maximum")
                outFile.write(str(ans) + "\n")
            else:
                raise Exception("Undefined operator")
        

