BLANK = object()

class Hashtable:

    def __init__(self, size = 1024):
        self.size = size
        self.values = size * [BLANK]
        self.pairs = size * [(None, None)]


    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index
    


    def __getitem__(self, key, value):
        value = self.values[self.index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value
    

    def __len__(self):
        return len(self.values)
       
    def set(self, key, value):
        index = self.hash(key)
        self.pairs[index] = (key, value)

    def get(self, key):
        index = self.hash(key)
        pair = self.pairs[index]
        if pair[0] == key:
            return pair[1]
        else:
            return None
    
    def __rep__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    hash1 = Hashtable(1024)
    hash1.set("ahmad", 30)
    hash1.set("silent", True)
    hash1.set("listen", "to me")