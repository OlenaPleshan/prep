import linkedlist

l = linkedlist.LinkedList()
n = linkedlist.Node("c")
l.add("a")
l.add("b")
l.addNode(n)
l.add("d")
l.add("e")
l.add("f")

def RemoveNode(node):
  if node == None or node.next == None:
    return False
  node.value = node.next.value
  node.next = node.next.next
  return True

print l
RemoveNode(n)
print l  

