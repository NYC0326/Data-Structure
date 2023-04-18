# Practice 4. Palindromes and Balance
import sys
from collections import deque

def isPalindrome(string):
    stack = []
    for s in string:
        stack.append(s) # 입력받은 string을 스택으로 바꿔줌
    for s in string:
        if stack.pop() != s: # 뒤에꺼랑 앞에께 다르면
            return False # 팰린드롬이 아니므로 False
    return True # 맞으니까 True

def balance(string):
    opening = ['(', '[', '{'] # 여는 괄호
    closing = [')', ']', '}'] # 닫는 괄호
    match = {}
    for i, ch in enumerate(closing): # 괄호와 그 인덱스를 묶어서 ch, i로 부를꺼임
        match[ch] = opening[i] # ch는 그 닫는 괄호, i는 ):0, ]:1, }:2 임
    stack = []
    for ch in string:
        if ch in opening: # 만약 여는 괄호가 string에 있다면
            stack.append(ch) # stack에 여는 괄호 추가
        elif ch in closing: # 만약 닫는 괄호가 string에 있다면
            if len(stack) == 0 or stack[-1] != match[ch]: # 만약 스택에 여는 괄호가 없거나 젤 최근에 연 괄호랑 닫는괄호가 안받는다면
                return False # 틀리니까 False 반환
            stack.pop() # 그게 아니라면 여는 괄호를 스택에서 제거
    return len(stack) == 0 # 완벽히 닫히는 문자열이라면 스택에서 여는괄호가 다 제거 됐을것이므로 True, 아니면 False 반환

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

        
