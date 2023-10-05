class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        reverse_x = ""
        negative = False
        for char in str_x[::-1]:
            if char == "-":
                negative = True
                continue
            reverse_x += char
        
        
        int_reverse_x = int(reverse_x)
        if negative:
            int_reverse_x *= -1
        
        if int_reverse_x > (2 ** 31) - 1 or int_reverse_x < (-(2 ** 31)):
            return 0

        return int_reverse_x
        
