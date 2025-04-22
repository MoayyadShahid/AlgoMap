class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = len(strs[0])
        for i in strs:
            if len(i) < shortest:
                shortest = len(i)
        
        if shortest == 0:
            return prefix

        fail = False

        for i in range(shortest):
            char = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != char:
                    return prefix
            
            prefix += char
        
        return prefix
