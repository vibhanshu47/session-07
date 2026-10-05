# Time Complexity: O(n)
# Space Complexity: O(n)

def containsDuplicate(nums):
    # If the set length is smaller, duplicates were removed
    return len(set(nums)) != len(nums)

# Test Executions
print("Test A ([1,2,3,1]):", containsDuplicate([1,2,3,1])) # Expected: True
print("Test B ([1,2,3,4]):", containsDuplicate([1,2,3,4])) # Expected: False