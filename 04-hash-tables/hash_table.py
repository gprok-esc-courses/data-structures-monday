"""
A simple implementation of a Hash Table to 
store names. 
Size of the table will be 10, just for simplicity
"""

from singly_linked_list import SinglyLinkedList

class HashTable:
    def __init__(self) -> None:
        self.hash_table = [None] * 10

    def display(self):
        for entry in self.hash_table:
            if entry is None:
                print(entry)
            else:
                entry.display()
                print()

    def hash_function(self, s: str) -> int:
        total = 0
        for c in s:
            total += ord(c)
        return total % 10

    def insert(self,name: str) -> None:
        # find the hash value of the name
        hash_value = self.hash_function(name)
        # go to the hasv value position of the table
        # if None create a new SinglyLinkedList
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = SinglyLinkedList()
        # add name to the list on that position
        self.hash_table[hash_value].insert_front(name)    




ht = HashTable()
ht.insert("George")
ht.insert("Mike")
ht.insert("Ann")
ht.insert("Kathy")
ht.insert("John")
ht.insert("Paul")
ht.insert("William")
ht.display()