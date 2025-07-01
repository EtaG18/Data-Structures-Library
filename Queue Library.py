class Queue:
    def __init__(self):
        self.container = []

    def enqueue(self,item):
        self.container.append(item)

    def dequeue(self):
        if self._is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.container.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.container[0]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return "Front ->" + "->".join(str(x) for x in self.container) + "<- Rear"