# Practices 6&7. Binary Search Tree Operations
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
SEARCH = 'S'
INSERT = 'I'
DELETE = 'D'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'

# Node implementation
class TreeNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Return True if tree is empty; False otherwise
    def isEmpty(self):
        return self.root == None

    # Given a sequence arr of integers, start index l, the end index r, 
    # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
    # Return the root node of the tree
    def arrayToBST(self, arr, l, r):
        if l>r:
            return None
        if arr != list(sorted(arr)):
            return None
        mid = int((l+r)/2)
        node = TreeNode(arr[mid])
        node.left = self.arrayToBST(arr, l, mid-1)
        node.right = self.arrayToBST(arr, mid+1, r)
        return node

    # Return the node with the minimum value 
    def findMin(self):
        if self.root == None:
            return None
        else:
            node = self.root
            while node.left != None:
                node = node.left
            return node

    # Return the node with the maximum value 
    def findMax(self):
        if self.root == None:
            return None
        else:
            node = self.root
            while node.right != None:
                node = node.right
            return node

    def _getHeight(self, curr):
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

    def _printSpaces(self, n, curr):
        for i in range(int(n)):
            print("  ", end="")
        if not curr:
            print(" ", end="")
        else:
            print(str(curr.key), end="")

    def printTree(self):
        if not self.root:
          return 
        q = deque()
        q.append(self.root)
        temp = deque()
        cnt = 0
        height = self._getHeight(self.root) - 1
        nMaxNodes = 2**(height + 1) - 1
        while cnt <= height:
            curr = q.popleft()
            if len(temp) == 0:
              self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
            else:
              self._printSpaces(nMaxNodes / (2**cnt), curr)
            if not curr:
              temp.append(None)
              temp.append(None)
            else:
              temp.append(curr.left)
              temp.append(curr.right)
            if len(q) == 0:
              print("\n")
              q = temp
              temp = deque()
              cnt += 1

    # Given a query, search for the node whose key is equal to query.
    # If the node exists, return the key
    # Otherwise, return nullptr  
    def search(self, root, query): # Time Complexity: O(N), if balanced, then O(logN)
        if root is None or root.key == query:
            return root
        if root.key < query:
            return self.search(root.right, query)
        else:
            return self.search(root.left, query)

    # Given an output file, write the keys of all the nodes 
    # visited in inorder traversal
    def writeInorder(self, root, outFile): # Time Complexity: O(N), if balanced, then O(logN)
        if root:
            self.writeInorder(root.left, outFile)
            outFile.write(str(root.key) + ' ')
            self.writeInorder(root.right, outFile)

    # Given an output file, write the keys of all the nodes 
    # visited in preorder traversal
    def writePreorder(self, root, outFile): # Time Complexity: O(N), if balanced, then O(logN)
        if root:
            outFile.write(str(root.key) + ' ')
            self.writePreorder(root.left, outFile)
            self.writePreorder(root.right, outFile)
  
    # Given an output file, write the keys of all the nodes 
    # visited in postorder traversal
    def writePostorder(self, root, outFile): # Time Complexity: O(N), if balanced, then O(logN)
        if root:
            self.writePostorder(root.left, outFile) # 일단 왼쪽으로 감
            self.writePostorder(root.right, outFile) # 그런 다음에 오른쪽 봄
            outFile.write(str(root.key) + ' ') # 그런다음에 출력함
  
    # If node with key k alreay exists in the tree, do nothing
    # Otherwise, insert new node with key k  
    def insertNode(self, root, k): # Time Complexity: O(N), if balanced, then O(logN)
        if root == None: # 만약 삽입하는게 첫 데이터라면
            root = TreeNode(k) # k가 root인 새로운 node를 생성
        else:
            if root.key == k: # 만약 탐색해서 root.key == k 이면 이미 있는 것이므로 삽입 하지 말고 그냥 리턴
                return root
            elif root.key < k: # 만약 삽입하고자 하는 값이 현재 root.key 보다 크면 root.right에 삽입해야함
                root.right = self.insertNode(root.right, k) # root.right을 root으로 해서 다시 삽입함
            else: # 만약 삽입하고자 하는 값이 현재 root.key 보다 작으면 root.left에 삽입해야함
                root.left = self.insertNode(root.left, k) # root.left을 root으로 해서 다시 삽입함
        return root # 루트를 반환
    
    # If deletion fails, immediately terminate the program
    # Otherwise, delete the node with key k
    def deleteNode(self, root, k): # Time Complexity: O(N), if balanced, then O(logN)
        if root is None: # 만약 루트가 None임 (삭제할게 없음)
            return root # 그냥 None 반환
        if k < root.key: # 만약 삭제하고자 하는 key값이 root.key보다 작음
            root.left = self.deleteNode(root.left, k) # 그럼 root를 기준으로 왼쪽에 있을테니까 다시 탐색
        elif k > root.key: # 그게 아니라 root.key 보다 크면
            root.right = self.deleteNode(root.right, k) # 오른쪽에 있을테니까 다시 탐색
        else: # 만약 root.key == k 라면 그거 삭제하면 됨
            if root.left is None: # 삭제를 할려고 하는데 왼쪽 자식노드가 None이면
                node = root.right # 일단 right를 node라는 임시 변수에 저장해두고
                root = None # root를 삭제하고
                return node # 그 오른쪽 자식노드를 반환해줌
            elif root.right is None: # 오른쪽이 비었다면 반대로
                node = root.left
                root = None
                return node
            temp = BinarySearchTree() # 자식 노드가 둘 다 있다면 그 successor랑 바꿈
            temp.root = root.right # 오른쪽 서브트리를 BST로 만들어줄려고 오른쪽 서브트리의 노드를 root.node로 만듦
            node = temp.findMin() # 오른쪽 서브트리의 최솟값을 찾으면 그것이 successor임
            root.key = node.key # root.key를 successor랑 바꿔줌
            root.right = self.deleteNode(root.right, node.key) # successor를 삭제
        
        return root

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    
    tree = BinarySearchTree()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == BUILD:
                data = [int(s) for s in words[1:]]
                tree.root = tree.arrayToBST(data, 0, len(data) - 1)
                if tree.root:
                    outFile.write(BUILD + "\n")
                    tree.printTree()
                else:
                    raise Exception("BUILD: invalid input")
            elif op == FIND_MIN:
                found = tree.findMin()
                if not found:
                    raise Exception("FindMin failed")
                else:
                    outFile.write(str(found.key) + "\n")
            elif op == FIND_MAX:
                found = tree.findMax()
                if not found:
                    raise Exception("FindMax failed")
                else:
                    outFile.write(str(found.key) + "\n")
            elif op == SEARCH:
                if len(words) != 2:
                    raise Exception("SEARCH: invalid input")
                k = int(words[1])
                # Practice 5. Call the function for search
                search = tree.search(tree.root, k) 
                if not search:
                    raise Exception("Search failed")
                else:
                    outFile.write(str(search.key) + "\n")
            elif op == INORDER:
                # Practice 5. Call the function for inorder traversal
                tree.writeInorder(tree.root, outFile)
                outFile.write("\n")
            elif op == PREORDER:
                # Practice 5. Call the function for preorder traversal
                tree.writePreorder(tree.root, outFile)
                outFile.write("\n")
            elif op == POSTORDER:
                # Practice 5. Call the function for postorder traversal
                tree.writePostorder(tree.root, outFile)
                outFile.write("\n")
            elif op == INSERT:
                if len(words) != 2:
                    raise Exception("INSERT: invalid input")
                k = int(words[1])
                # TODO. Practice 6. Call the function for insertion
                tree.root = tree.insertNode(tree.root, k)
                outFile.write("I "+ str(k) + "\n")
            elif op == DELETE:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                k = int(words[1])
                # TODO. Practice 6. Call the function for deletion
                if not tree.search(tree.root, k):
                    break
                else:
                    tree.root = tree.deleteNode(tree.root, k)
                outFile.write("D " + str(k) + "\n")
            else:
                raise Exception("Undefined operator")