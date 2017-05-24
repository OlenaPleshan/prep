import linkedlist

def ReturnKthToLast(l, k):
  n = CalculateLenght(l) - k + 1
  return FindNth(l, n)
  
def CalculateLenght(l):
  curr = l.head
  length = 0
  while curr:
    length += 1
    curr = curr.next
  return length

def FindNth(l, n):
  curr = l.head
  pos = 0
  while curr:
    pos += 1
    if pos == n:
      return curr.value
    curr = curr.next

def ReturnKthToLast2(l, k):
  values = []
  curr = l.head
  while curr:
    values.append(curr.value)
    curr = curr.next
  return values[-1*k]

l = linkedlist.CreateList(["a", "b", "c", "d", "e", "f"])
print ReturnKthToLast(l, 2)
print ReturnKthToLast2(l, 2)
