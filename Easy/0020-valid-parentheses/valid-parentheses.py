class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {')':'(','}':'{',']':'['}

        for char in s:
            if char in hmap:
                # Ensuring the stack is not empty.
                # Ensuring that stack top char is 
                # mapped bracket for the map.
                if stack and stack[-1] == hmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                # We can append as many new parantheses as needed.
                stack.append(char)
        # Ensuring the stack is empty.
        if not stack:
            return True
        else:
            return False