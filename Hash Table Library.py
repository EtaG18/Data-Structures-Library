class HashTable:
    def __init__(self,size=10):
        self.size=size
        self.table = [[] for _ in range(size)]

    def hash(self,key):
        return hash(key) % self.size
    
    def insert(self,key, value):
        index = self.hash(key)
        bucket = self.table[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))

    def get(self,key):
        index =self._hash(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k ==key:
                return v
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"{i}: {bucket}")
        return "\n".join(result) 
    