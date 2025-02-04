class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(4)

node1.next = node2
node2.next = node3

currentNode = node1

while currentNode:
    print(currentNode.data, end="")
    currentNode = currentNode.next
    if currentNode:  # Only print '->' if there's a next node
        print("->", end="")

# Output: 1->3->4
