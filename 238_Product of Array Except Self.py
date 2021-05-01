'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of 

all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
  
        
# String 
class Solution:
    def productExceptSelf(self, nums):
        
        n = len(nums)
        result = [0] * n
        result[0] = 1  # 因為要用乘的, 所以用1初始化
        
        # 先處理左邊
        for i in range(1, n):
           result[i] = result[i-1] * nums[i-1] # 第i個 = 前一個乘上  
        
        # 再處理右邊   
        r = 1
        for i in range(n-1, -1, -1): # 往回
           result[i] *= r
           r *= nums[i]    
        
        return result
           
if __name__ == '__main__':
    
    list = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.productExceptSelf(list))     
                    