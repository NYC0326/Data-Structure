# Practice 13. Sorting 
import sys
MERGE_SORT = 'M'
QUICK_SORT = 'Q'

def readInput(line, size):
    words = line.split()
    assert(len(words) == size)
    arr = [int(word) for word in words]
    return arr

def msort(arr):
    if len(arr) < 2: # 다 분할이 되어, list에 자기 자신뿐일때
        return arr # 자기 자신을 return
    mid = len(arr) // 2 # mid index
    left = msort(arr[:mid]) # 재귀
    right = msort(arr[mid:]) # 재귀
    merged_arr = [] # 정렬된 list

    while len(left) > 0 and len(right) > 0: # 양쪽 다 요소가 남아있을 때
        if left[0] > right[0]: # 더 큰 요소 먼저 삽입
            merged_arr.append(left.pop(0))
        else:
            merged_arr.append(right.pop(0))

    if len(left)>0: # 왼쪽 배열이 남아있을 때 남아 있는 거 다 추가하기
        merged_arr += left 
    else: # 오른쪽 배열이 남이있을 때 남아 있는 거 다 추가하기
        merged_arr += right

    return merged_arr # 정렬된 배열 반환

def qsort(arr):
    if len(arr) < 2:
        return arr
    piv = arr.pop(0) # pivot은 list의 맨 앞의 요소로 지정
    left = [] # 
    right = []

    for i in arr:
        if i > piv:
            left.append(i) # 내림차순이므로 큰거를 왼쪽 배열에
        else:
            right.append(i) # 작은거를 오른쪽 배열에
    
    return qsort(left) + [piv] + qsort(right) # 재귀로 계속 분할하며 퀵소트 실행

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if len(words) != 2:
                raise Exception("Error: invalid input")
            size = int(words[1])
            i += 1
            arr = readInput(lines[i], size)
            if op == MERGE_SORT:
                if len(words) != 2:
                    raise Exception("MERGE_SORT: invalid input")
                ans = msort(list(map(int, lines[i].split())))
                for a in ans:
                    outFile.write(str(a) + " ")
                outFile.write("\n")
            elif op == QUICK_SORT:
                if len(words) != 2:
                    raise Exception("QUICK_SORT: invalid input")
                ans = qsort(list(map(int, lines[i].split())))
                for a in ans:
                    outFile.write(str(a) + " ")
                outFile.write("\n")
            else:
                raise Exception("Undefined operator")
            i += 1
