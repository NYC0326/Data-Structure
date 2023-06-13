# Practice 13. Sorting 
MERGE_SORT = 'M';
QUICK_SORT = 'Q';

def readInput(line, size):
  words = line.split()
  assert(len(words) == size)
  arr = [int(word) for word in words]
  return arr

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  S = Stack()
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
        # TODO
      elif op == QUICK_SORT:
        if len(words) != 2:
          raise Exception("QUICK_SORT: invalid input")
        # TODO
      else:
        raise Exception("Undefined operator")
      i += 1

