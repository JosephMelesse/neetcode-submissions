class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        sorted_s = sorted(s_list)
        sorted_t = sorted(t_list)
        return sorted_s == sorted_t

        
        