'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: s = "anagram", t = "nagaram"
Output: true

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# My self
class Solution_1:
    def isAnagram(self, s, t):
        wordMap = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in wordMap:
                    wordMap[s[i]] += 1 
                else:
                    wordMap[s[i]] = 1

            for j in range(len(t)):
                if t[j] in wordMap:
                    wordMap[t[j]] -=1
                else:
                    return False    
            for k, v in wordMap.items():
                v += v
            if v == 0:
                return True        
        
# Hash table
class Solution_2:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        
        for c in t:
            if c not in cnt or cnt[c] == 0:
                return False
            else:
                cnt [c] -=1
                     
        return True
        
if __name__ == '__main__':
    
    s1 = Solution_1()
    print(s1.isAnagram('alinyiwen','alinyiwen'))     
    
    s2 = Solution_2()
    print(s2.isAnagram('alinyiwen','alinyiwen'))                      