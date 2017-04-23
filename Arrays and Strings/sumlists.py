import linkedlist

def SumLists(l1, l2):
  return ConvertListToNumber(l1) + ConvertListToNumber(l2)

def ConvertListToNumber(l):
  base = 10
  multiplier = 1
  number = 0
  current = l.head
  while current:
    number += current.value * multiplier
    multiplier *= base
    current = current.next
  return number

def SumLists2(l1, l2):
  base = 10
  quotient = 0
  modulo = 0
  curr1 = l1.head
  curr2 = l2.head
  result = linkedlist.LinkedList()
  while curr1 and curr2:
    sum_pos = curr1.value + curr2.value + quotient
    quotient = sum_pos / base
    modulo = sum_pos % base
    result.add(modulo)
    curr1 = curr1.next
    curr2 = curr2.next
  curr_longer_list = curr1 or curr2
  while curr_longer_list:
    result.add(curr_longer_list.value + quotient)
    modulo = 0
    curr_longer_list = curr_longer_list.next
  if quotient:
    result.add(quotient)
  return result

def AddListsRecursively(n1, n2, modulo):
  if n1 == None and n2 == None and modulo == 0:
    return None
  
  base = 10
  value = modulo
  if n1:
    value += n1.value
  if n2:
    value += n2.value
  result = linkedlist.Node(value % base)

  if n1 != None or n2 != None:
    digit = AddListsRecursively(None if n1 == None else n1.next,
                                None if n2 == None else n2.next,
                                value / base)
    result.setNextNode(digit)
  return result


l1 = linkedlist.CreateList([7, 1, 6])
l2 = linkedlist.CreateList([5, 9, 2])
l3 = linkedlist.CreateList([1, 5, 6])
l4 = linkedlist.CreateList([2, 3, 6, 7])
l5 = linkedlist.CreateList([9, 7, 8])
l6 = linkedlist.CreateList([6, 8, 5])

print SumLists(l1, l2), SumLists(l3, l4), SumLists(l5, l6)
print SumLists2(l1, l2), SumLists2(l3, l4), SumLists2(l5, l6)

res = AddListsRecursively(l1.head, l2.head, 0)
res_list = linkedlist.LinkedList()

res_list.setHead(res)
print res_list

res = AddListsRecursively(l3.head, l4.head, 0)
res_list.setHead(res)
print res_list

res = AddListsRecursively(l5.head, l6.head, 0)
res_list.setHead(res)
print res_list
