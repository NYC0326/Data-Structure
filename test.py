class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
node1 = node(1)
node2 = node(2)
node3 = node(3)
node1.next = node2
node2.next = node3

n = node1

while n.next != None:
    print(n.data)
    n = n.next