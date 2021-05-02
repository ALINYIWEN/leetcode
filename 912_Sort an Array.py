'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

912. Sort an Array

Given an array of integers nums, sort the array in ascending order.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
        
# Sort
class Solution:
    def sortArray(self, nums):
        
        # 氣泡排序
        length = len(nums)
        for i in range(length):
            for j in range(length - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                            
        return nums
            
if __name__ == '__main__':
    
    list = [2,7,4,1,8,1]
    s = Solution()
    print(s.sortArray(list))     
                    