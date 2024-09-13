from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    if not root:
        return True  # An empty tree is a valid BST
    
    # Initialize a queue for level-order traversal
    queue = deque([(root, float('-inf'), float('inf'))])  # Store node and valid range (min, max)
    
    # Iterate through the tree
    while queue:
        node, min_value, max_value = queue.popleft()
        
        if node:
            # Check if the current node's value violates the BST property
            if node.val <= min_value or node.val >= max_value:
                return False
            
            # Add the left child to the queue with updated bounds (left subtree < node.val)
            queue.append((node.left, min_value, node.val))
            
            # Add the right child to the queue with updated bounds (right subtree > node.val)
            queue.append((node.right, node.val, max_value))
    
    return True  # If we finished the traversal without violations, it's a BST

# Example usage
# Creating a sample binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Checking if the tree is a BST
print(isBST(root))  # Output: True or False depending on the tree's structure
