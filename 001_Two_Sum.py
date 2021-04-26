'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Given nums = 2, 7, 11, 15, target = 9,

Because nums0 + nums1 = 2 + 7 = 9, return 0, 1.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# My self
class Solution_1:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            value = target - nums[i]
            for j in range(len(nums)-1):
                if value == nums[j+1] and j+1 != i:    
                    return i, j+1       
                else:
                    j+=1


# Hash table
class Solution_2:
    def twoSum(self, nums, target):
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [numMap.get(target-nums[i]), i]
            else:
                numMap[nums[i]] = i
           
                
            
    
if __name__ == '__main__':

    #s1 = Solution_1()
    #print(s1.twoSum([2, 5, 5, 11], 10))     
    
    s2 = Solution_2()
    print(s2.twoSum([2, 5, 5, 11], 10))         