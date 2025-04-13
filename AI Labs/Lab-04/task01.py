# Implementation of Stack

class Stack:
    def __init__(self):
        self.stack = []  # initializing stack with empty list
       
     
        # Push Function
    def push(self, item):
        self.stack.append(item)
        print(f"{item} added to the stack.")
     

        # Pop Function
    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"{removed} removed from the stack.")
            return removed
        else:
            print("Stack is empty.")
       

         # Top Function
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
        

          # Empty Function
    def is_empty(self):
        return len(self.stack) == 0
       
       
         # Display Function
    def display(self):
        print("Current Stack:", self.stack)


# Making object of the class Stack and calling functions
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
print("Top element is:", s.top())

s.display()

if s.is_empty():
    print("Stack is empty.")
else:
    print("Stack is not empty.")
