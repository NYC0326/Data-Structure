# Practice 15. Autocomplete system
import sys
BUILD_TRIE = 'T'
AUTOCOMPLETE = 'A'
ENDS_HERE = '#'

if __name__ == '__main__':
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if op == BUILD_TRIE:
        if len(words) != 2:
          raise Exception("BUILD_TRIE: invalid input")
        n = int(words[1])
        strings = []
        while n:
          i += 1
          strings.append(lines[i].strip())
          n -= 1
        # TODO. Build a trie with "strings"
      elif op == AUTOCOMPLETE:
        if len(words) != 2:
          raise Exception("AUTOCOMPLETE: invalid input")
        prefix = words[1]
        # TODO. Run autocomplete with "prefix" and write results into "outFile"
      else:
        raise Exception("Undefined operator")
      i += 1
