# node for a singly linked list.
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None

  def setNextNode(self, node):
    self.next = node

class LinkedList:

  def __init__(self):
    self.head = None

  # appends to head.
  def add(self, value):
    node = Node(value)
    #node.next = self.head
    #self.head = node
    if not self.head:
      self.head = node
      return True
    curr = self.head
    while curr:
      if curr.next == None:
        curr.next = node
        return True
      curr = curr.next

  def addNode(self, node):
    node.next = self.head
    self.head = node

  def setHead(self, node):
    self.head = node
  
  def remove(self, value):
    current = self.head
    previous = current
    if current.next == None:
      self.head = None
    while previous and previous.next != None:
      if current.value == value:
        previous.next = current.next
      previous = current
      current = current.next

  def __str__(self):
    values = []
    node = self.head
    while node and node.next != None:
      values.append(str(node.value))
      node = node.next
    if node:
      values.append(str(node.value))
    return ", ".join(values)

def CreateList(vals):
  l = LinkedList()
  for v in vals:
    l.add(v)
  return l
