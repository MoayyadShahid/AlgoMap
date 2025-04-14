class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = len(word1) if len(word1) <= len(word2) else len(word2)
        w1_big = True if len(word1) >= len(word2) else False
        merged = ""

        for i in range(min_len):
            merged += word1[i]
            merged += word2[i]
        
        if w1_big:
            merged += word1[min_len:]
        else:
            merged += word2[min_len:]
        
        return merged