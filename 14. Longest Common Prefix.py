class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        s1 = min(strs)
        s2 = max(strs)
        
        for i, char in enumerate(s1):
            if char != s2[i]:
                break
            answer += char
        return answer
            
