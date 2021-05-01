'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: "aba"
Output: True

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
  
        
# String 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isp(s: str, l: int, r: int) -> bool:  # 建立一個檢查的函式
            while  l < r: # 交會之前檢查
                if s[l] != s[r]: # 
                    return False
                l, r = l + 1 , r - 1
            return True
        
        i, j = 0, len(s) - 1  
        while  i < j: # 交會之前檢查
                if s[i] != s[j]:        # 若發現有一個字元不同, 有一次豁免權可以省略
                    return isp(s, i+1, j) or isp(s, i, j-1) # 只要兩者之一可以回傳True 那就對了
                i, j = i + 1 , j - 1
        
        return True
          
if __name__ == '__main__':
    
    s = Solution()
    print(s.validPalindrome('alinyiwen','alinyiwen'))     
                    