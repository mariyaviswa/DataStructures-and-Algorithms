class Node:
    # init method or constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
    # init method or constructor
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            cnt += 1

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            return self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                if itr.next.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                break
            itr = itr.next

    def insert_after_values(self, data_after, data_insert):
        if self.head.data == data_after:
            node = Node(data_insert, self.head.next)
            self.head.next = node

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("LinkedList is empty.")

        itr = self.head
        s = ""
        while itr:
            s += f'{itr.data} --> '
            itr = itr.next
        print(s + "None")

if __name__ == '__main__':
    ll = linkedList()
    # Insert at beginning

    ll.insert_at_beginning(4)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    print("After insertion at beginning: ")
    ll.print()

    # Insert at end
    ll.insert_at_end(5)
    print("After insert at index 5: ")
    ll.print()

    # get the linked list length

    length = ll.get_length()
    print("length of linked list: ", length)

    # remove at index
    ll.remove_at_index(1)
    print("After removing the index 1: ")
    ll.print()

    # insert at index
    ll.insert_at_index(1, 2)
    print("After inserting at index 1: ")
    ll.print()

    # insert values as list
    ll.insert_values(["apple", "orange", "banana", "grapes"])
    print("After inserting values: ")
    ll.print()

    # remove by value
    ll.remove_by_value("grapes")
    print("After removing the value: ")
    ll.print()

    # insert after values
    ll.insert_after_values("banana", "mango")
    print("After inserting: ")
    ll.print()