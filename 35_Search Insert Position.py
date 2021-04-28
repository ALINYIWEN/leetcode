'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

1. Two Sum

Given a sorted array of distinct integers and a target value, return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Binary Search
class Solution_2:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif  nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return low            
            
if __name__ == '__main__':
    
    s2 = Solution_2()
    print(s2.searchInsert([1, 3, 5], 0))              