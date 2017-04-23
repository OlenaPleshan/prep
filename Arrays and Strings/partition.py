import linkedlist

def Partition1(l, x):
  left_part = linkedlist.LinkedList()
  right_part = linkedlist.LinkedList()
  last_node_left = None
  current = l.head
  while current:
    if current.value < x:
      left_part.add(current.value)
      if last_node_left:
        last_node_left = last_node_left.next
      else:
        last_node_left = left_part.head.next
    else:
      right_part.add(current.value)
    current = current.next
  if last_node_left:
    last_node_left.next = right_part.head
    return left_part
  else:
   return right_part

def Partition2(l, x):
  last_node_left = l.head
  current = l.head
  previous = l.head
  while current:
    if current.value < x:
      previous.next = current.next
      node = linkedlist.Node(current.value)
      node.next = l.head
      l.head = node
    previous = current
    current = current.next

l = linkedlist.CreateList([9, 7, 3, 6, 9, 1])
print Partition1(l, 6)

l = linkedlist.CreateList([9, 7, 3, 6, 9, 1])
Partition2(l, 6)
print l
