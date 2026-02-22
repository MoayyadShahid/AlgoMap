class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        check = False

        if len(s1) > len(s2):
            return False

        for i in s1:
            count1[ord(i) - ord('a')] += 1
            
        for r in range(len(s2) - len(s1) + 1):

            count2 = [0] * 26 
            for i in range(r, r + len(s1)):
                count2[ord(s2[i]) - ord('a')] += 1
            
            if count2 == count1:
                check = True
        
        return check
