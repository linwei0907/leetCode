class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key = lambda x: x[0])
        output = []
        output.append(intervals[0])
        n = len(intervals)

        for i in range(1, n):
            inner_val1 = output[-1][1]
            inner_val2 = intervals[i][0]

            if inner_val1 >= inner_val2:
                max_index = max(inner_val1, intervals[i][1])
                combine = [output[-1][0], max_index]
                output[-1] = combine
            else:
                output.append(intervals[i])
        return output
