from typing import Union
from package import Package
class HashTable:
    # Initialize the hash table as an array with a length of 40
    def __init__(self):
        self.length = 40
        self.array = [None] * self.length

    # Hash function 
    def hash(self, key: int) -> int:
        return key % len(self.array)
    
    # Function to insert key-value pairs to the hash table 
    def insert(self, package_id: int, package: Package) -> None:
        # Initialize key-value pairs 
        key_hash = self.hash(package_id)
        key_value = [package_id, package]

        # Case 1: Key is not in the hash table 
        if self.array[key_hash] is None:
            # Add the key-value pair to the hash table 
            self.array[key_hash] = list([key_value])
            return None
        # Case 2: Key is already in the hash table 
        else:
            # Loop through the available entries in the hash table 
            for entry in self.array[key_hash]:
                # If the package ID has already been used, update its 
                # corresponding value 
                if entry[0] == package_id:
                    entry[1] = package
                    return None
            # If a hash collision occurs, just add the new key-value pair to
            # the end of the list with the designated hash value 
            self.array[key_hash].append(key_value)

    # Function to get the value of a given key in the hash table 
    def get(self, package_id: int) -> Union[Package, None]:
        key_hash = self.hash(package_id)
        if self.array[key_hash] is not None:
            for entry in self.array[key_hash]:
                # If the package ID is in the hash table, return the contents
                # of the package 
                if entry[0] == package_id:
                    return entry[1]
        return None 
    
# ht = HashTable()
# pk1 = Package(0, 'a', 'a', 'a', 1, 1, 'a')
# ht.insert(0, pk1)
# print(ht.get(0))
# pk2 = Package(1, 'b', 'b', 'b', 2, 2, 'b')
# ht.insert(0, pk2)
# print(ht.get(0))
# pk3 = Package(3, 'c', 'c', 'c', 2, 2, 'b')
# ht.insert(40, pk3)
# print(ht.array[0])
# print(ht.get(40))