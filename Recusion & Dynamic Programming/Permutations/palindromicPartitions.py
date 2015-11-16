''' https://leetcode.com/problems/palindrome-partitioning/
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
  [
    ["aa","b"],
    ["a","a","b"]
  ]

'''
def partition(s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPali(string):
            return string == string[::-1]
            
        res = []
        def paliPart(string, palis):

            if len(string) <= 0:
                res.append(palis)
                return
            
            else:
                for i in range(1,len(string)+1):
                    if isPali(string[:i]):
                        paliPart(string[i:],palis + [string[:i]])
        
        paliPart(s, [])
        return res

print(partition('aabb'))