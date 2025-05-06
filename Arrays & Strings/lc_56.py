class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in range(len(intervals) - 1):
            interval = intervals[i]
            if interval[-1] >= intervals[i+1][0]:
                new_interval = [interval[0], intervals[i+1][0]]
                merged.append(new_interval)

        merged.append(intervals[-1])
        return merged
