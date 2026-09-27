class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        #res_dict_s = {'r':2, 'a':2, 'c':2, 'e':1}
        #res_dict_t = {'c':2, 'r':2, 'a':2, 'e':1}

        res_dict_s = {}
        res_dict_t = {}

        for i in range(len(s)):
            res_dict_s[s[i]] = 1 + res_dict_s.get(s[i], 0)
            res_dict_t[t[i]] = 1 + res_dict_t.get(t[i], 0)

        for c in res_dict_s:
            if res_dict_s[c] != res_dict_t.get(c, 0):
                return False
        return True



        