'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

926. Flip String to Monotone Increasing

A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), 

followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
  
        
# String 
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        f0, f1 = 0, 0 # 各自代表0與1的翻轉次數
        for ch in S:
            if ch == "0":
                f1 += 1
            else:
                f1 = min(f0, f1)
                f0 += 1
        return min(f0, f1)
                
if __name__ == '__main__':
    
    s = Solution()
    print(s.minFlipsMonoIncr("010110"))     
                    