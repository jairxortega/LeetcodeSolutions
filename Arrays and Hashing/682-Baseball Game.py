# Easy
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # initialize an empty stack

        for ops in operations: # iterate through the operations
            if ops == 'C':
                stack.pop() # remove the last element from the stack
            elif ops == 'D':
                stack.append(stack[-1] * 2) # append the last element of the stack multiplied by 2
            elif ops == '+':
                stack.append(stack[-1] + stack[-2]) # append the sum of the last two elements of the stack
            else:
                stack.append(int(ops)) # append the integer value of the string to the stack
        return sum(stack) # return the sum of the stack

# Time complexity: O(n)
# The run time is O(n) because we are only iterating through the operations list once.
# Space complexity: O(n)
