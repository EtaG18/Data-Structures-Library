import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self._make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            raise IndexError('Index out of Bounds!')
        return self.A[k]
    
    def append(self,item):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_cap):
        B = self._make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    
    def __str__(self):
        return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"


# Demo
arr = DynamicArray()
arr.append(10)
arr.append(20)
arr.append(30)
print('Manual Dynamic Array:',arr)
print('Length:',len(arr))
print("Item at index 1:", arr[1])