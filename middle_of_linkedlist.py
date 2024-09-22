class Node:
    def __init__(self, data, next=None):  # Provide default value for 'next'
        self.data = data
        self.next = next

class Solution:
    def middle(self, head):
        count = 0
        curr = head
        # Step 1: Count the total number of nodes
        while curr is not None:
            count += 1
            curr = curr.next
        
        # Step 2: Find the middle index
        mid = count // 2
        curr = head
        # Step 3: Traverse to the middle node
        for i in range(mid):
            curr = curr.next
        
        return curr.data  # Return the data of the middle node

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create an instance of Solution and find the middle
sol = Solution()
mid = sol.middle(head)
print("Middle element of the linked list is:", mid)
