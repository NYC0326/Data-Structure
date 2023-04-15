# Practice 4. Palindromes and Balance
import sys
from collections import deque

def isPalindrome(string): # Time Complexity: O(n)
    # each operation of popleft and pop has time complexity of O(1), so if we do that for all, it would be O(n)
    q = deque(string) # make string as a queue
    stk = deque(string) # also a stack too
    while q and stk: # while elements are left on the queue and the stack
        if q.popleft() != stk.pop(): # popleft means the first element of the queue, pop means the last element of the queue
            return False # so if those two are different, it means the string isn't a palindrome, so return False
    return True # if all elements were removed, it means the string is a palindrome
    
def balance(string): # Time Complexity: O(n)
    # also for this, operation append in deque has time complexity of O(1), so it would be O(n) if we do that for all of the elements in the string
    stk = deque() # make a empty stack
    for i in string:
        if i in ['(', '[', '{']: # if i is one of the opening brackets
            stk.append(i) # append on the stack
        # following codes are for when if i is the closing bracket and the same bracket type as the last element, then remove the last element 
        elif i == ')':
            if not stk or stk[-1] != '(':
                return False
            else:
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] != '[':
                return False
            else:
                stk.pop()
        elif i == '}':
            if not stk or stk[-1] != '{':
                return False
            else:
                stk.pop()
    if stk: # if stack is not empty, which means there are brackets left in the stack, it isn't a balanced bracket
        return False
    return True # if stack is empty, it means the string is a balanced bracket

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == 'P':
                if len(words) != 2:
                    raise Exception("PALINDROME: invalid input")
                ret = "T" if isPalindrome(words[1]) else "F"
                outFile.write(ret+"\n")
            elif op == 'B':
                if len(words) != 2:
                    raise Exception("BALANCE: invalid input")
                ret = "T" if balance(words[1]) else "F"
                outFile.write(ret+"\n")
            else:
                raise Exception("Undefined operator")

        
