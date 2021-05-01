'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: s = "()"
Output: true

Input: s = "{[]}"
Output: true

Input: s = "([)]"
Output: false

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
  
        
# Stack
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dictionary = {"(":")","[":"]","{":"}"}
        
        for c in s:
            if stack and dictionary.get(stack[-1]) == c: # 若堆疊內有東西, 且取到字典內的左括號的對應: 右括號 就把原先的左括號pop
                stack.pop()
            else:
                stack.append(c)    
        return not stack # 若裡面還有東西就是False 不然就是True

if __name__ == '__main__':
    
    list = "{[]}"
    s = Solution()
    print(s.isValid(list))     
                    