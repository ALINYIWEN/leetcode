'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: 

namely, if two adjacent bits will always have different values.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        n = n ^ (n >> 1)
        return n & (n + 1) == 0         

if __name__ == '__main__':

    s = Solution()
    answer = s.hasAlternatingBits(7)
    print("answer: " + str(answer))