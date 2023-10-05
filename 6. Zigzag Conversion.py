class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        if numRows == 1:
            return s
        
        for i in range(numRows):
            if len(ans) == len(s):
                return ans
            index = i
            direction = "down"
            
            ans += s[index]
            while True:
                if direction == "down":
                    if i == numRows - 1:
                        direction = "up"
                    else:
                        index += (2 * (numRows - 1 - i))
                        direction = "up"
                        if index < len(s):
                            ans += s[index]
                        else:
                            break
                else:
                    if i == 0:
                        direction = "down"
                    else:
                        index += (2 * (i))
                        direction = "down"
                        if index < len(s):
                            ans += s[index]
                        else:
                            break
        return ans
