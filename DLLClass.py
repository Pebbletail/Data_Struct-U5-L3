#Brook Brudnok
#2/4/25

class DoublyLinkedList:

  class DoublyNode:
    def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None

    def set_next(self, node):
      """accepts node object, updates next location"""
      if type(node) == type(self) or type(node) == type(None):
        self.next = node
      else:
        raise ValueError("next must be DoublyNode data type")

    def set_prev(self, node):
      """accepts node object, updates previous location"""
      if type(node) == type(self) or type(node) == type(None):
        self.prev = node
      else:
        raise ValueError("next must be DoublyNode data type")
    
    def __str__(self):
      """displays the Node"""
      return f"|{self.value}|"
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.__size = 0

  def head_insert(self, value):
    """accepts value, insert new node at head"""
    newNode = self.DoublyNode(value)
    if self.__is_empty():
      self.head = newNode
      self.tail = newNode
    else:
      self.head.set_prev(newNode)
      newNode.set_next(self.head)
      self.head = newNode
    self.__size += 1

  def tail_insert(self, value):
    """accepts value, insert new node at tail"""
    newNode = self.DoublyNode(value)
    if self.__is_empty():
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.set_next(newNode)
      newNode.set_prev(self.tail)
      self.tail = newNode
    self.__size += 1

  def head_remove(self):
    """remove and return the head value"""
    if self.__is_empty() == True:
      raise IndexError("cannot remove from an empty list")

    if self.__size == 1:
      old = self.head
      self.head = None
      self.__size -= 1

    else:
      old = self.head
      self.head = old.next
      self.head.set_prev(None)
      self.__size -= 1

    if self.__is_empty() == True:
      self.head = None
      self.tail = None

    return old.value


  def tail_remove(self):
    """remove and return the tail value"""
    if self.__is_empty() == True:
      raise IndexError("cannot remove from an empty list")

    if self.__size == 1:
      old = self.tail
      self.tail = None
      self.__size -= 1

    else:
      old = self.tail
      self.tail = old.prev
      self.tail.set_next(None)
      self.__size -= 1


    if self.__is_empty() == True:
      self.head = None
      self.tail = None

    return old.value

  def __is_empty(self):
   """returns True if list is empty"""
   if self.__size == 0:
      return True
   else:
      return False

  def __len__(self):
    """return size"""
    return self.__size

  def __str__(self):
    """displays the current linked list"""
    out = "HEAD > "

    walk = self.head
    for i in range(self.__size):
      out += f"{walk} "
      walk = walk.next
      if walk != None:
          out += "<-> "

    out += "< TAIL"
    return out
