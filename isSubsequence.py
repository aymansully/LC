class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i_iter = 0
        j_iter = 0
        
        new_string = ""
        while i_iter < len(s) and j_iter < len(t):
            if s[i_iter] == t[j_iter]:
                new_string += s[i_iter]
                i_iter += 1
            j_iter += 1
        return new_string == s
