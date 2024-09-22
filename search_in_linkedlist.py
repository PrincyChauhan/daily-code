class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Solution:
    def search(self,n,head,key):
        curr=head
        while curr is not None:
            if curr.data==key:
                return True
            curr=curr.next
        return False            
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)

n=4
key=5

print("key to be searched is:",key)   

sol=Solution() 
if sol.search(n, head, key):
    print(f"Key {key} found in the linked list")
else:
    print(f"Key {key} not found in the linked list")