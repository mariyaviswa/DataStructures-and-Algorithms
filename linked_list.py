class Node:
    """
     An object for storing a single node of a linked list
     Model two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __int__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data



