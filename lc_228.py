class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
             
        ranges = []
        first = nums[0]
        last = nums[0]
        for i in range(len(nums) - 1):

            if nums[i] + 1 != nums[i + 1]:
                last = nums[i]
                if first == last:
                    ranges.append(str(last))
                else:
                    ranges.append(f'{first}->{last}')
                first=nums[i+1]
            

        if nums[-1] - 1 != nums[len(nums) - 2]:
            ranges.append(str(nums[-1]))
        else: 
            ranges.append(str(first) + "->" + str(nums[-1]))

        print(first)
        
        return ranges
