def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    def expand(index):
        i = index
        j = index
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
            
        return (i+1, j-1)
    
    ''' find the longest palindrome that starts at index 0 (Could use manacher's algorithm to do so) '''
    best = ''
    for i in range(len(s)):
        idxs = expand(i)
        if idxs[0] == 0 and idxs[1]-idxs[0]+1 > len(best):
            best = s[idxs[0]:idxs[1]+1]
    
    return s[len(best):][::-1] + s

print(shortestPalindrome("abcd"))