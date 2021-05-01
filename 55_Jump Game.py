'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
which makes it impossible to reach the last index.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Greedy algorithm
class Solution:
    def canJump(self, nums):
        
        for i in range(len(nums)-2, -1, -1): # 從尾巴看回來, 找0來看看前面有沒有人可以跳過坑到達最後一格
            if nums[i] == 0:
                gap = 1                      # 遇到一個坑了, 把它設為1
                while gap > nums[i]:         # 當往前找的值, 還是跨不過坑時
                    gap = gap + 1            # 將要跨過的程度加1 
                    i = i - 1                # 再往前
                    if i < 0:
                        return False         # 若找到頭了都跨不過, 即為False
        return True        
           
if __name__ == '__main__':
    nums = [3,2,1,0,4]
    s = Solution()
    print(s.canJump(nums))     
  