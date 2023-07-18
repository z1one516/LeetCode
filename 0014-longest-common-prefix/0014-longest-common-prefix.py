class Solution:
    def longestCommonPrefix(semf,strs):
        if not strs: return''
        s1=min(strs)
        s2=max(strs)

        for idx, key in enumerate(s1):
            if key != s2[idx]:
                return s1[:idx]
        return s1