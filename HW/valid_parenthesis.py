
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the top element if stack isn't empty, else assign a dummy
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

# Test Executions
print("Test A ( '()' ):", isValid("()")) # Expected: True
print("Test B ( '()[]{}' ):", isValid("()[]{}")) # Expected: True
print("Test C ( '(]' ):", isValid("(]")) # Expected: False