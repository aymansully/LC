class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        newList = [""]*len(s)
        charDict = {}
        
        for i in range(len(s)):
            if s[i] not in charDict and t[i] not in charDict.values():
                charDict[s[i]] = t[i]
            if s[i] in charDict.keys():    
                newList[i] = charDict[s[i]] 
        newWord = "".join(newList)
        if newWord == t:
            return True
        else:
            return False
