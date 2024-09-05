class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_kth_node(head, k):
    current = head
    count = 0
    
    # Traverse the list until you reach the k-th node
    while current:
        if count == k:
            return current.data
        count += 1
        current = current.next
    
    # If k is greater than the number of nodes in the list
    return None

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2
print(f"The data at the {k}-th node is: {find_kth_node(head, k)}")
