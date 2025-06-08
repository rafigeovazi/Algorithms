def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
if __name__ == "__main__":
    arr = [34,6,4,3,54,65,75,34,75]
    target = 4
    result = sequential_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")