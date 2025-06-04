class Node:
    # initialize (constructor)
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    # initialize (constructor)
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_after_value(self, value, data):
        itr = self.head

        while itr.data != value:
            itr = itr.next
        node = Node(data)
        node.next = itr.next
        itr.next = node

    def insert_values(self, values):
        # self.head = None  # if want the new linkedlist
        for val in values:
            self.insert_at_end(val)

    def remove_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_at_end(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def insert_at_index(self, index, data):
        # check the index is valid or not 
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            return self.insert_at_beginning(data)
        
        i = 0
        itr = self.head

        while i < index - 1:
            itr = itr.next
            i += 1
        node = Node(data)
        node.next = itr.next
        itr.next = node

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1
        return count
    
    def remove_at_index(self, index):
        if index == 0:
            return self.remove_at_beginning()
        
        elif index == self.get_length() - 1:
            return self.remove_at_end()
        
        else:
            i = 0
            itr = self.head

            while i < index - 1:
                itr = itr.next
                i += 1
            itr.next = itr.next.next

    def remove_by_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
        
        itr = self.head
        while itr.next.data != value:
            itr = itr.next
        
        itr.next = itr.next.next

    def print(self):
        if self.head is None:
            print("Linked List is empty.")
        itr = self.head
        while itr:
            print(f"{itr.data} -> ", end="")
            itr = itr.next

# Initialize the class
ll = LinkedList()

# Insert at beginning
ll.insert_at_beginning(5)
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)

# insert after particular value
ll.insert_after_value(3, 7)

# insert values as bulk(list of values)
ll.insert_values([8, 6, 4, 3])

# remove the value at beginning
ll.remove_at_beginning()

# remove the value at end 
ll.remove_at_end()

# insert at particular index
ll.insert_at_index(3, 6)

# remove value in particular index
ll.remove_at_index(0)

# remove by value
ll.remove_by_value(4)

# print the linked list
ll.print()