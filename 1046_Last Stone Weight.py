'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

1046. Last Stone Weight

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  

Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import heapq  
        
# Heap
class Solution:
    def lastStoneWeight(self, stones):
        
        h = [-x for x in stones]  # heap 默認是min heap , 因為要取最大值出來, 所以代負號硬轉
        heapq.heapify(h)          # 強制將list轉成min heap
        while len(h) > 1:         # list內還有超過一個的時候做
            y = heapq.heappop(h)   # 取出最小的(因為加負號,所以其實是最大的) 就是最前面那個
            x = heapq.heappop(h)   # 取出第二大的
            if y != x:
                heapq.heappush(h, y-x) # 若取出的兩者數值不同, 則相減並push回去
        if len(h) == 0:
            return 0
        else:
            return -h[0]        
            
            
if __name__ == '__main__':
    
    list = [2,7,4,1,8,1]
    s = Solution()
    print(s.lastStoneWeight(list))     
                    