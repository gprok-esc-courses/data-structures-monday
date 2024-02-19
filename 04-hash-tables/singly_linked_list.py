
class Node:
    def __init__(self) -> None:
        self.element = None
        self.next = None

    def get_element(self):
        return self.element
    
    def set_element(self, value):
        self.element = value

    def get_next(self):
        return self.next
    
    def set_next(self, ref):
        self.next = ref

    def __str__(self) -> str:
        return self.get_element()

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None
    
    def insert_front(self, value):
        # create new node
        new_node = Node()
        # set the element of the new node to value
        new_node.set_element(value)
        # set the next of the new node to head
        new_node.set_next(self.head)
        # set head to the new node
        self.head = new_node
        # if tail is none, set tail also to the new node
        if self.tail is None:
            self.tail = new_node

    def remove_front(self):
        if self.is_empty():
            print("Nothing to remove")
            return None
        elif self.head == self.tail:    # one node in the list
            self.tail = self.tail.get_next()
        value = self.head.get_element()
        self.head = self.head.get_next()
        return value

    def display(self):
        # set an iterator to head
        iterator = self.head
        # while iterator is not None
        #   print iterator's element
        #   iterator goes to iterator's next
        while iterator is not None:
            print(iterator, end=' ')
            iterator = iterator.get_next()

    def insert_back(self):
        # EXERCISE: implement this, pretty easy
        pass

    def remove_back(self):
        if self.is_empty():
            print("Noting to remove")
            return None
        if self.head == self.tail:        # Only one node in the list
            value = self.head.get_element()
            self.head = None
            self.tail = None
        else:
            iterator = self.head
            while iterator.get_next() != self.tail:
                iterator = iterator.get_next()
            value = self.tail.get_element()
            self.tail = iterator
            self.tail.set_next(None)
        return value

    def insert_after(self, existing_element, new_element):
        iterator = self.head
        while (iterator is not None) and \
                (iterator.get_element() != existing_element):
            iterator = iterator.get_next()
        if iterator is None:
            print(existing_element, "not found")
        else:
            new_node = Node()
            new_node.set_element(new_element)
            new_node.set_next(iterator.get_next())
            iterator.set_next(new_node)

    def remove(self, element):
        # EXERCISE: remove the given element
        # NOTE: Two exceptions, element is in the first or last node
        pass

class Stack(SinglyLinkedList):
    def __init__(self) -> None:
        super().__init__()

    def push(self, value):
        self.insert_front(value)

    def pop(self, value):
        return self.remove_front(value)
    

# EXERCISE: Implement a Queue class
# a queue is a FIFO data structure
# functions:
# enqueue -> inserts an element
# dequeue -> removes and returns the first inserted element


if __name__ == '__main__':
    simple_list = SinglyLinkedList()
    simple_list.insert_front("Athens")
    simple_list.insert_front("Paris")
    simple_list.insert_front("Madrid")
    simple_list.insert_front("Tirana")
    simple_list.insert_front("Prague")
    simple_list.insert_front("Rome")
    simple_list.insert_after("Prague", "London")
    simple_list.display()


