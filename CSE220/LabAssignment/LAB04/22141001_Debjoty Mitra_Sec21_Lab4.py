class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p


class DoublyList:
  
  def __init__(self, a):
    self.head = Node(a[0], None, None)
    h = self.head
    h.prev = self.head
    for i in range(1, len(a)):
        n = Node(a[i], None, None)
        n.next = self.head
        n.prev = self.head.prev
        self.head.prev.next = n
        self.head.prev = n
  
  # Counts the number of Nodes in the list and return the number
  def countNode(self):
    begin = self.head
    cnt = 1
    while begin.next != self.head:
        begin = begin.next
        cnt+=1
    return cnt
  
  # prints the elements in the list
  def forwardprint(self):
    begin = self.head
    while begin.next != self.head:
        print(begin.element, end=',')
        begin = begin.next
    print(begin.element, end='.\n')
    

  # prints the elements in the list backward
  def backwardprint(self):
    begin = self.head.prev
    while begin != self.head:
      print(begin.element, end=",")
      begin = begin.prev
    print(f"{begin.element}.")


  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
     # To Do
    begin = self.head 
    c = 0
    while begin.next!=self.head:
      if c == idx:
        return begin
      begin = begin.next
      c += 1
    if c == idx:
      return begin
    return "index error"
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    begin = self.head
    cnt = 0
    while begin.next!=self.head:
        if begin.element == elem:
            return cnt
        begin = begin.next
        cnt+=1
    if begin.element == elem:
        return cnt
    return -1

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    if idx==0:
        n = Node(elem, None, None)
        n.next = self.head
        n.prev = self.head.prev
        self.head.prev.next = n
        self.head.prev = n
        self.head = n
    else:
        n1 = self.nodeAt(idx-1)
        n2 = n1.next
        n = Node(elem, None, None)
        n.next = n2
        n.prev = n1
        n1.next = n
        n2.prev = n
        
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    result = None
    if idx==0:
        result = self.head.element
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next
    else:
      n = self.nodeAt(idx - 1)
      result = n.next.element
      n.next = n.next.next
      n.next.prev = n
    return str(result)
    
print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  
print('------------')
# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  


# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.