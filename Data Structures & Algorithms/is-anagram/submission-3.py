class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 0
            s_hash[c] += 1
        for d in t:
            if d not in t_hash:
                t_hash[d] = 0
            t_hash[d] += 1
        return s_hash == t_hash



        
        