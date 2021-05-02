'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Input: n = 0
Output: 0

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import math

class Solution:
    def countPrimes(self, n):
        
        if n < 2:    # 2以下一定沒有質數
            return 0                            
        
        prime = [1]* n                          # 建立一個陣列, 質數代表1 , 其餘為0
        prime[0] = prime[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1): # 從2到根號n
            if prime[i] == 1:
                for j in range(i + i, n, i):      # 將倍數去掉
                    prime[j] = 0
        return sum(prime)                    
                            
if __name__ == '__main__':
    nums = 10
    s = Solution()
    print(s.countPrimes(nums))     
  