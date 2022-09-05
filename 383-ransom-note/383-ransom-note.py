class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = True
        r_d = dict()
        m_d = dict()
        
        for i in ransomNote:
            r_d[i] = r_d.get(i, 0) + 1
        
        for j in magazine:
            m_d[j] = m_d.get(j, 0) + 1
        
        print(r_d)
        print(m_d)
        
        for key, val in r_d.items():
            if m_d.get(key, 0) < val:
                res = False
                break
                
        return res
