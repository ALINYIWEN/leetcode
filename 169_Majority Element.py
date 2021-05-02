'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import math

class Solution:
    def majorityElement(self, nums):
        
        result, count, length =  nums[0], 1, len(nums)   # 先預設 第一個就是result
        for i in range(1, length):
            if result == nums[i]:  
               count = count + 1
            elif count > 0:         # 若發現一個不一樣的, 就假裝他們相消, count -1 又只剩一個
               count = count - 1 
            else:
                result = nums[i]
                count = 1  
        return result 
    
                             
if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    s = Solution()
    print(s.majorityElement(nums))     
  