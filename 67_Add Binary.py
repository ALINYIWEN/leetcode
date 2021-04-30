'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

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