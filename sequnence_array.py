import math

def calculate_cost(arr):
    total_cost = 0
    
    while len(arr) > 1:
        print("arr------",arr)
        min_ele = min(arr)
        max_ele = max(arr)
        
        # Calculate the cost of the operation
        cost = math.ceil((min_ele + max_ele) / (max_ele - min_ele + 1))
        print("cost------",cost)
        total_cost += cost
        print("total_cost------",total_cost)
        # Remove one occurrence of min and max elements from the array
        arr.remove(min_ele)
        arr.remove(max_ele)
        
        # Add their sum back to the array
        new_ele = min_ele + max_ele
        arr.append(new_ele)
    
    return total_cost    

# Example usage
arr = [2, 3, 4, 5, 7]
print(calculate_cost(arr)) 
