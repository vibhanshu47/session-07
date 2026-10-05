# Time Complexity: O(n)
# Space Complexity: O(n)

def isPalindrome(x):
    # Negative numbers are not palindromes due to the minus sign
    if x < 0:
        return False
    
    # Convert to string and check if it equals its reverse
    str_x = str(x)
    return str_x == str_x[::-1]

# Test Executions
print("Test A (121):", isPalindrome(121)) # Expected: True
print("Test B (-121):", isPalindrome(-121)) # Expected: False