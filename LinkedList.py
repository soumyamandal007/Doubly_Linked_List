from Node import Node

class LinkedList():
   def __init__(self):
      self.head_node = None
   
   def get_head(self):
      return self.head_node
   
   def is_empty(self):
      if (self.head_node is None):
         return True
      else:
         return False
      
   def insert_at_head(self,value):
      temp = Node(value)
      if self.is_empty():
         self.head_node = temp
         return self.head_node
      
      temp.next_element = self.head_node
      self.head_node.prev_element = temp
      self.head_node = temp
      return self.head_node
   
   def print_list(self):
      if self.is_empty():
         print("List is empty")
         return False
      
      curr = self.head_node
      while curr.next_element is not None:
         print(curr.data , end="-->")
         curr = curr.next_element
      print(curr.data , end="-->None")
      return True
   