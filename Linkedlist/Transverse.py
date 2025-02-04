class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1= Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

currentNode=node1
current=currentNode
print(current)
# while currentNode is not None:
new_node=Node(50)
while current.next is not None:
    current=current.next
current.next=new_node

# new_node.next=currentNode
# currentNode=new_node

while currentNode:
    print(currentNode.data,end="")
    currentNode=currentNode.next
    if currentNode:
        print("->", end="")
