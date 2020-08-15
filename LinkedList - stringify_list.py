# Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    print("new_node.value = {}, new_node.next_node.value = {}, self.head_node.value = {}.".format(new_node.value, new_node.next_node.value, self.head_node.value))
  
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
    
# Test
ll = LinkedList(5)

ll.insert_beginning(70)
# output: new_node.value = 70, new_node.next_node.value = 5, self.head_node.value = 70.

ll.insert_beginning(5675)
# output: new_node.value = 5675, new_node.next_node.value = 70, self.head_node.value = 5675. 

ll.insert_beginning(90)
# output: new_node.value = 90, new_node.next_node.value = 5675, self.head_node.value = 90. 

print(ll.stringify_list())