class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we create dictionaries / hashmaps for the strings to pair the letter with their counts
        sMap = {}
        tMap = {}
        # we go through each string and get the count of each letter 
        for i in s:
            sMap[i] = sMap.get(i, 0) + 1
        for j in t:
            tMap[j] = tMap.get(j, 0) + 1

        # 1st check is to see if the number of unique letters is the same, if not then they're not anagrams
        if len(sMap.keys()) != len(tMap.keys()):
            return False
        # otherwise if the number of unique letters is the same then we check if the letters are the same 
        # and the counts of those same letters are the same, if we have mismatching counts or letters then return False
        for k in sMap.keys():
            if tMap.get(k, 0) != sMap.get(k, 0):
                return False
        # all checks have passed, return true
        return True

        # Run Time: O(max(m, n)), where m and n are the sizes of the strings s and t respectively
        