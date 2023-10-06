# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        if n < 3:
            return -1

        left = 0
        right = n - 1
        max_index = 0

        while left <= right:
            mid = (right + left) // 2
            num = mountain_arr.get(mid)
            next_num = mountain_arr.get(mid + 1)
            if num < next_num:
                left = mid + 1
            else:
                right = mid - 1
        
        max_index = left
        print(max_index)

        left = 0
        right = max_index

        while left <= right:
            mid = (right + left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        left = max_index + 1
        right = n - 1
        
        while left <= right:
            mid = (right + left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


            
