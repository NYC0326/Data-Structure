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
        return i * 2

    # Given the index i of element, return the index of that element's right child in the heap
    def right(Self, i):
        return i * 2 + 1

    # Insert a given element elem into the heap
    # If the insertion fails, immediately terminate the program with the error message.
    def insertElement(self, elem):
        if self.count >= self.capacity:
            raise Exception("Cannot insert more than max capacity")
        self.count += 1
        self.elements[self.count] = elem

        print("Inserted %d in elements[%d]" % (elem, self.count))
        for i in range(1, self.count+1):
            print("[%d]: %d" % (i, self.elements[i]), end = ' ')
        print()

        curr = self.count
        while self.parent(curr) > 0 and self.elements[curr] > self.elements[self.parent(curr)]:
            self.elements[curr], self.elements[self.parent(curr)] = self.elements[self.parent(curr)], self.elements[curr]
            curr = self.parent(curr)
        print("After heapifying")
        for i in range(1, self.count+1):
            print("[%d]: %d" % (i, self.elements[i]), end = ' ')
        print()

    # Return the maximum of the heap if it exists
    # Otherwise, terminate program with an error

    def maximum(self):
        if self.count == 0:
            return False
        return self.elements[1]

    # Delete the maximum from the heap and return the maximum
    # If deletion fails, terminate program with an error
    def deleteMaximum(self):
        if self.maximum() == False:
            return False
        max = self.elements[1]
        self.elements[0] = self.elements[self.count]
        curr = 0
        while True:
            if self.left(curr) > self.right(curr):
                if self.left(curr) <= self.capacity and self.elements[curr] < self.elements[self.left(curr)]:
                    self.elements[curr], self.elements[self.left(curr)] = self.elements[self.left(curr)], self.elements[curr]
                    curr = self.left(curr)
                elif self.right(curr) <= self.capacity and self.elements[curr] < self.elements[self.right(curr)]:
                    self.elements[curr], self.elements[self.right(curr)] = self.elements[self.right(curr)], self.elements[curr]
                    curr = self.right(curr)
                else:
                    break
            else:
                if self.right(curr) <= self.capacity and self.elements[curr] < self.elements[self.right(curr)]:
                    self.elements[curr], self.elements[self.right(curr)] = self.elements[self.right(curr)], self.elements[curr]
                    curr = self.right(curr)
                elif self.left(curr) <= self.capacity and self.elements[curr] < self.elements[self.left(curr)]:
                    self.elements[curr], self.elements[self.left(curr)] = self.elements[self.left(curr)], self.elements[curr]
                    curr = self.left(curr)
                else:
                    break
        self.count-=1
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
                # If the insertion succeeds, write every element in the array into output file.
                h.insertElement(i)
                for i in range(1, h.count+1):
                    outFile.write(str(h.elements[i]) + " ")
                outFile.write("\n")
            elif op == DELETE:
                # TODO. Call the deletion method
                # If the deletion succeeds, write every element in the array into output file.
                ans = h.deleteMaximum()
                if ans == False:
                    raise Exception("Deletion Failed! No maximum")
                for i in range(1, h.count+1):
                    outFile.write(str(h.elements[i]) + " ")
                outFile.write("\n")
            elif op == MAXIMUM:
                # TODO. Call the function to get the maximum
                # If getting the maximum succeeds, write the maximum into output file.
                ans = h.maximum()
                if ans == False:
                    raise Exception("No maximum")
                outFile.write(str(ans) + "\n")
            else:
                raise Exception("Undefined operator")
