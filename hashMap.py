# Time complexity = O(n)
# Space complexity = O(n)
class HashMap:
    # HashMap constructor doesn't take any other arguments
    # Time complexity = O(1)
    def __init__(self):
        self.size = 10;
        self.map = [None] * self.size

    # Calculates a hash index from the key provided
    # Time complexity = O(1)
    def __get_hashindex(self, key):
        hashindex = int(key) % self.size
        return int(hashindex)

    # Inserts a new item into the HashMap at the hash index
    # Time complexity = O(n)
    def insert(self, key, value):
        key_hash = self.__get_hashindex(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                else:
                    self.map[key_hash].append(key_value)
                    return True

    # Removes an item from the HashMap at given key
    # Time complexity = O(n)
    def remove(self, key):
        key_hash = self.__get_hashindex(key)
        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # Retrives item information at a given key
    # Time complexity = O(n)
    def lookup(self, key):
        key_hash = self.__get_hashindex(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

# Citation
# Author: Joe James
# Video title: Python: Creating a HASHMAP using Lists
# Date accessed: 9/4/2022


