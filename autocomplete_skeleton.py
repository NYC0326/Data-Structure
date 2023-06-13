# Practice 15. Autocomplete system
import sys
BUILD_TRIE = 'T'
AUTOCOMPLETE = 'A'
ENDS_HERE = '#'

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head

        for c in string:
            if c not in node.child:
                node.child[c] = Node(c)
            node = node.child[c]
        node.data = string
    
    def starts_with(self, prefix):
        node = self.head
        words = []

        for c in prefix:
            if c in node.child:
                node = node.child[c]
            else:
                return None

        node = [node]
        next_node = []
        while True:
            for n in node:
                if n.data:
                    words.append(n.data)
                next_node.extend(list(n.child.values()))
            if len(next_node) != 0:
                node = next_node
                next_node = []
            else:
                break
                
        return words

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
                trie = Trie()
                for s in strings:
                    trie.insert(s)
            elif op == AUTOCOMPLETE:
                if len(words) != 2:
                    raise Exception("AUTOCOMPLETE: invalid input")
                prefix = words[1]
                ans = trie.starts_with(prefix)
                for a in ans:
                    outFile.write(a + " ")
                outFile.write("\n")
            else:
                raise Exception("Undefined operator")
            i += 1
