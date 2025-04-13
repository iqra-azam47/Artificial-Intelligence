# Implementation Of Binary Search

class BinarySearch:

    def __init__(self,data):
        self.data = sorted(data)

    def search(self,element):
        start = 0
        end = len(self.data)-1
        

        while start<=end:
            mid = (start + end)//2
          
            if element < self.data[mid]:
                end = mid-1

            elif element > self.data[mid]:
                start = mid + 1

            elif element == self.data[mid]:
                print("Element found at index ",mid)
                return 
            

        print("Element not found!")
        



list1 = [1,2,3,6,7,9,10]
print("List is given: ",list1)
target = int(input("Enter element you want to search."))

bs = BinarySearch(list1)
bs.search(target)


            