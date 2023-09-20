from LinkedList import LinkedList
from Node import Node

def delete(lst, value):
   deleted = False
   if lst.is_empty():
      print("List is Empty")
      return deleted
   
   curr = lst.get_head()
   
   if curr.data is value:
      lst.head_node = curr.next_element
      if (curr.next_element != None and curr.next_element.prev_element != None ):
         curr.next_element.prev_element = None
         deleted = True
         print(str(curr.data) + " deleted")
      return deleted
   while curr:
      if curr.data == value:
         if curr.next_element != None:
            prev = curr.prev_element
            next = curr.next_element
            prev.next_element = next
            next.prev_element = prev
         else:
            curr.prev_element.next_element = None
         deleted = True
         break
      curr = curr.next_element
   if deleted is False:
        print(str(value) + " is not in the List!")
   else:
        print(str(value) + " Deleted!")
   return deleted


lst = LinkedList()
for i in range(11):
    lst.insert_at_head(i)

lst.print_list()
delete(lst, 5)

lst.print_list()
delete(lst, 10 )

lst.print_list()