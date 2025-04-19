class Solution:    
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True
        elif t_len == 0:
            return False

        for i in range(t_len):
            if s_ptr == s_len - 1 and s_ptr > 0:
                return True
            elif t[i] == s[s_ptr]:
                s_ptr += 1
        
        return False
