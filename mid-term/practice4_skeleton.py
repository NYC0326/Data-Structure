# Practice 4. Palindromes and Balance
import sys
from collections import deque

# Return True if str is a palindrome; False otherwise
def isPalindrome(string):
    stk = deque(string)
    q = deque(string)
    while stk:
        if stk.pop() != q.popleft(): 
            return False
    return True

# Return true if brackets are balanced in str; false otherwise
def balance(string):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    match = {}
    stk = deque()
    for i, c in enumerate(closing):
        match[c] = opening[i]
    for c in string:
        if c in opening:
            stk.append(c)
        elif c in closing:
            if len(stk) == 0 or stk[-1] != match[c]:
                return False
            stk.pop()
    return len(stk) == 0

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

        
