class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = (1000, 'M')
        CM = (900, 'CM')
        D = (500, 'D')
        CD = (400, 'CD')
        C = (100, 'C')
        XC = (90, 'XC')
        L = (50, 'L')
        XL = (40, 'XL')
        X = (10, 'X')
        IX = (9, 'IX')
        V = (5, 'V')
        IV = (4, 'IV')
        I = (1, 'I')

        roman_roms = [M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]

        string = ""


        for i, rr in enumerate(roman_roms):
            num_of_rr = num // rr[0]
            if num_of_rr > 0:
                string += rr[1] * num_of_rr

            num -= rr[0] * num_of_rr
            if num == 0:
                return string

        return string
