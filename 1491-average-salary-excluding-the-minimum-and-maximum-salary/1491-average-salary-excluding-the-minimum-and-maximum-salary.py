class Solution:
    def average(self, salary: List[int]) -> float:
        maxi = 1000
        mini = 10**6
        tot = 0
        
        for i in salary:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
            tot += i
        
        return (tot - maxi - mini)/ (len(salary)-2)