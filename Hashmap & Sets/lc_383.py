class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # have a hashmap for the magazine string called big, and for ransomNote called small
        big = {}
        small = {}
        # go through both strings and map their characters to occurrences
        for i in magazine:
            big[i] = big.get(i, 0) + 1
        for j in ransomNote:
            small[j] = small.get(j, 0) + 1

        # going through the hashmap that represents the ransomNote string (small hashmap)
        # we will see if the specific char is in big hashmap (representing the magazine string)
        for k in small:
            # if the char is not in the big hashmap, or if the big hashmap has less occurrences of char k
            # in big than in the small hashmap THEN we will return False
            if k not in big or big[k] < small[k]:
                return False
    
        # otherwise we didn't reach a fail condition so return True
        return True

    