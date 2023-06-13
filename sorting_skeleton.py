# Practice 13. Sorting
import sys
MERGE_SORT = 'M'
QUICK_SORT = 'Q'

def readInput(line, size):
    words = line.split()
    assert(len(words) == size)
    arr = [int(word) for word in words]
    return arr

def msort(val):
    if len(val) < 2:
        return val
    mid = len(val) // 2
    left = msort(val[:mid])
    right = msort(val[mid:])
    merged_val = []

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            merged_val.append(left.pop(0))
        else:
            merged_val.append(right.pop(0))
    
    if len(left) > 0:
        merged_val += left
    if len(right) > 0:
        merged_val += right

    return merged_val

def qsort(val):
    if len(val) < 2:
        return val
    pivot = val[0]
    left = []
    right = []
    piv = []
    for i in val:
        if i > pivot:
            left.append(i)
        elif i < pivot:
            right.append(i)
        else:
            piv.append(i)
    return qsort(left) + piv + qsort(right)

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

