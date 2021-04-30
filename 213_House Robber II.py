'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

213. House Robber II

You are a professional robber planning to rob houses along a street. 

Each house has a certain amount of money stashed, 

All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 

Meanwhile, adjacent houses have a security system connected, 

and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 

return the maximum amount of money you can rob tonight without alerting the police.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

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
        
        # 不偷第0棟 --> result = rob[length - 1]
        # rob[i] = max(nums[i] + rob[i-2], rob[i-1])
        previous, current = 0, nums[1]
        for i in range(2, length):
             temp, previous = previous, current
             current = max(nums[i] + temp, previous)
        
        result = current
        # 偷第0棟 --> result = rob[0-2]
        previous, current = nums[0], nums[0]
        for i in range(2, length-1):
             temp, previous = previous, current
             current = max(nums[i] + temp, previous)

        return max(result, current)
        
if __name__ == '__main__':

    s = Solution()
    print(s.rob([1,2,3,1]))