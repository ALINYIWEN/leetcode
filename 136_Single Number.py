'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: nums = [4,1,2,1,2]
Output: 4

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

class Solution:
    def singleNumber(self, nums):

        new_list = []              
        for i in nums:
            if i in new_list:
                new_list.remove(i)
            else:    
                new_list.append(i)

        return new_list.pop()            

if __name__ == '__main__':
    list = [4,1,2,1,2]
    s = Solution()
    answer = s.singleNumber(list)
    print("answer: " + str(answer))