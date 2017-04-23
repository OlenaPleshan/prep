import linkedlist

def GetIntersectingNode(l1, l2):
  curr1 = l1.head
  curr2 = l2.head
  while curr1:
    while curr2:
      if curr1 == curr2:
        return curr1
      curr2 = curr2.next
    curr1 = curr1.next

n1 = linkedlist.Node(3)
n2 = linkedlist.Node(7)

l1 = linkedlist.CreateList([1, 2, 3])
l1.addNode(n1)

l2 = linkedlist.LinkedList()
l2.addNode(linkedlist.Node(1))
l2.addNode(n1)
l2.addNode(linkedlist.Node(7))
l2.addNode(linkedlist.Node(8))

print n1
print GetIntersectingNode(l1, l2)
