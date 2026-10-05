# Time Complexity: O(n log n)
# Space Complexity: O(n)

def isAnagram(s, t):
    # An anagram must have the exact same sorted characters
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Test Executions
print("Test A (anagram, nagaram):", isAnagram("anagram", "nagaram")) # Expected: True
print("Test B (rat, car):", isAnagram("rat", "car")) # Expected: False