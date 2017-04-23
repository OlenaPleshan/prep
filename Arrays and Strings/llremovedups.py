import linkedlist


def RemoveDups(l):
  current = l.head
  while current:
    runner = current
    while not runner.next == None:
      if current.value == runner.next.value:
        runner.next = runner.next.next
      else:
        runner = runner.next
    current = current.next

def RemoveDups2(l):
  previous = None
  current = l.head
  unique_els = []
  while current:
    if current.value in unique_els:
      previous.next = current.next
    else:
      unique_els.append(current.value)
      previous = current
    current = current.next
    
l = linkedlist.CreateList(["d", "c", "c", "c", "d", "b"])
#RemoveDups(l)
RemoveDups2(l)
print l
