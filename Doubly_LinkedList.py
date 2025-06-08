class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        curr = self.head

        while curr.next:
            curr = curr.next
        node = Node(data = data)
        curr.next = node
        node.prev = curr

    def remove_at_beginning(self):
        curr = self.head
        if curr.next:
            curr.next.prev = None
            self.head = curr.next
            return 
        
    def remove_at_end(self):
        curr = self.head
        
        # Edge-case If only one node available
        if curr.next is None:
            self.head = None

        while curr.next.next:
            curr = curr.next
        curr.next = None
    
    def insert_after_value(self, value, data):
        curr = self.head

        while curr.data != value:
            curr = curr.next

        node = Node(data = data)
        if curr.next:
            curr.next.prev = node
            node.next = curr.next

        curr.next = node
        node.prev = curr


    def display(self):
        curr = self.head
        print("None", end = " ⇄ ")

        while curr:
            print(curr.data, end = " ⇄ ")
            curr = curr.next

        print("None")


if __name__ == '__main__':

    dll = DoublyList()

    # Insert data at Beginning
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(2)
    
    # Insert data at ending
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.insert_at_end(6)
    dll.insert_at_end(7)
    dll.insert_at_end(8) 

    # Remove at beginning 
    dll.remove_at_beginning()

    # Remove at ending
    dll.remove_at_end()
    dll.remove_at_end()
    
    # Insert data after particular value
    dll.insert_after_value(4, 7)
    dll.insert_after_value(6, 8)
    # Display your list
    dll.display()
