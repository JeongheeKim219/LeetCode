class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            word = words[i]
            for j in range(len(words)):
                if i == j:
                    continue
                if word in words[j]:
                    if word not in res: 
                        res.append(word)
                        
        return res
        