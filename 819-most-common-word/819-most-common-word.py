from collections import Counter 

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.compile(r'\w+')
        paragraph = p.findall(paragraph)
        ls = list()
        for s in paragraph:
            if s.lower() not in banned:
                ls.append(s.lower())   

        return Counter(ls).most_common(1)[0][0]
        