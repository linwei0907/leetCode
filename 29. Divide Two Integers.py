class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        ans = 0
        sign = 1

        # exclusive or.
        if (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        keepGoing = True
        while keepGoing:
            temp_dvs = divisor
            keepGoing_ = True
            shifts = 1
            while keepGoing_:
                if temp_dvs <= dividend:
                    temp_dvs <<= 1
                    shifts <<= 1
                else:
                    keepGoing_ = False
                    temp_dvs >>= 1
                    shifts >>= 1
            dividend -= temp_dvs
            ans += shifts
            if divisor > dividend:
                keepGoing = False


        ans = ans * sign
        
        if ans > MAX_INT:
            return MAX_INT
        elif ans < MIN_INT:
            return MIN_INT

        return ans
