class Stack:
    def __init__(self):
        self.container = []

    def push(self,item):
        self.container.append(item)

    def pop(self):
        if self._is_empty():
            raise IndexError("Popo from empty Stack")
        return self.container.pop()
    
    def peek(self):
        if self._is_empty():
            raise IndexError("Peek from Empty Stack")
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return "Top ->" + "->".join(reversed([str(x) for x in self.container]))
    