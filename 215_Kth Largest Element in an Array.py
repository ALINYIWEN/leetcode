'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

class Solution:
    def findKthLargest(self, nums, k):
        nums = nums
        result = sorted(nums)
        answer = result[len(nums) - k]
        return answer
            
if __name__ == '__main__':
    
    list_1 = [3,2,1,5,6,4]
    k = 2
    s = Solution()
    print(s.findKthLargest(list_1, k))     
                    