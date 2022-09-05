class HashMap:
    def __init__(self):
        self.size = 10;
        self.map = [None] * self.size

    def __get_hashindex(self, key):
        hashindex = int(key) % self.size
        return int(hashindex)

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

    def lookup(self, key):
        key_hash = self.__get_hashindex(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        key_hash = self.__get_hashindex(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
