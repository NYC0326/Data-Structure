# Practice 12. Search
import sys
BINARY_SEARCH = 'B'
PERFECT_SQUARE = 'P'

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      line = lines[i]
      words = line.split()
      op = words[0]
      if op == BINARY_SEARCH:
        if len(words) != 3:
          raise Exception("BINARY_SEARCH: invalid input")
        size, x = int(words[1]), int(words[2])
        # TODO
      elif op == PERFECT_SQUARE:
        if len(words) != 2:
          raise Exception("PERFECT_SQUARE: invalid input")
        x = int(words[1])
        # TODO
      else:
        raise Exception("Undefined operator")
      i += 1

        
