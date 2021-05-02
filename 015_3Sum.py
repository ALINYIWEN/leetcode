'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 

such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Two pointer
class Solution:
    def threeSum(self, nums):
        
        nums.sort() # 先將串列排序好
        result = []
        
        for i in range(len(nums) - 2): # 從最左邊開始, 到倒數第三個
            if i == 0 or (i>0 and nums[i] != nums[i-1]): # 檢查i是否重複 
                j, k, target = i + 1, len(nums)-1, 0 - nums[i]     # nums[i],nums[j],nums[k]加起來要等於0
                while j < k: # 等待交會 j, k 是two pointer 等待交會 
                    if nums[j] + nums[k] == target: # 若找到一組解
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:       # 
                            j = j + 1
                        while j < k and nums[k] == nums[k - 1]:       #     
                            k = k - 1
                        j = j + 1
                        k = k - 1    
                    elif nums[j] + nums[k] < target:
                        j = j + 1
                    else:
                        k = k - 1
        return result                            
                            
                            
if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))     
  