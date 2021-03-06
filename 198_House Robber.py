'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

198. House Robber

You are a professional robber planning to rob houses along a street. 

Each house has a certain amount of money stashed, 

the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 

and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 

return the maximum amount of money you can rob tonight without alerting the police.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Dynamic Programming
class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 0:       # 若房子數為0 則回傳0
            return 0          
        if length == 1:       # 若房子數為1 則回傳唯一值
            return nums[0]
        
        # 初始化偷的陣列
        rob = [0] * length
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        
        for i in range(2, length): # 從2開始 
            rob[i] = max(nums[i] + rob[i-2], rob[i-1])
        
        return rob[-1] # 或rob[length-1]
                 
if __name__ == '__main__':

    s = Solution()
    print(s.rob([1,2,3,1]))