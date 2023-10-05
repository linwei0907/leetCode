class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToInt = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M":1000}
        answer = 0;
        previousValue = 0;
        for char in s:
            value = romanToInt[char]
            if value > previousValue:
                answer = answer + (value - 2*previousValue);
            else:
                answer = answer + value;
            previousValue = value;
        return answer
    
