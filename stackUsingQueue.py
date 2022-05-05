class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)  
        for i in range(len(self.queue)-1):
            self.queue.append(self.pop()) 

    def pop(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def top(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        return None

    def empty(self) -> bool:
        return len(self.queue) == 0

    def test(self):
        obj = MyStack()
        obj.push(1)
        obj.push(2)
        assert obj.top() == 2
        assert obj.empty() == False
        assert obj.pop() == 2
        assert obj.top() == 1
        assert obj.empty() == False 
        
          

    
if __name__ == "__main__":
  MyStack().test()
  print("Everything passed")

# Your MyStack object will be instantiated and called as such:
