# Implementation of Queue


class Queue:
    # Deafult Constructor
    def __init__(self):
        self.queue = []  
    

    # Enqueue Function
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")


    # Dequeue Function
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"{removed} removed from the queue.")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
    

    # Front Function
    def front(self):
        if not self.is_empty():
            print(f"Front item is: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty.")


     # Empty Function
    def is_empty(self):
        return len(self.queue) == 0
    

    # Display Function
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.queue)



# Object Creation
q = Queue()

# Calling Functions
print(q.is_empty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()     
q.dequeue()     
q.front()        
q.display()    

print(q.is_empty())