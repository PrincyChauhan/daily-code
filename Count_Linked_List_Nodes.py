class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class solution:
    def getcount(self,head):
        curr=head   
        count=0
        while curr is not None:
            count+=1
            curr=curr.next
        return count
    
# Example to create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Create an instance of Solution and call the method
sol = solution()
print("Count of nodes in linked list is:", sol.getcount(head))