class Solution:
    def moveZeroes(self, nums):
        """
        type nums: List[int]
        rtype: None
        """
        temp = []
        while 0 in nums:
            nums.remove(0)
            temp.append(0)
        nums += temp
        return nums

data = [0,1,0,3,12]
s = Solution()

print(s.moveZeroes(data))                